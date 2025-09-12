
from datetime import datetime, date
from typing import Optional, List, Tuple
from db import Database
from auth import hash_password, verify_password
from models import User, UserFactory, Car, CarFactory
from pricing import compute_days, compute_total
from observer import bus

DATE_FMT = "%Y-%m-%d"

class UserService:
    def __init__(self):
        self.db = Database().conn

    def register(self, name: str, email: str, password: str, role: str = 'customer') -> Tuple[bool,str]:
        cur = self.db.cursor()
        cur.execute("SELECT id FROM users WHERE email = ?", (email,))
        if cur.fetchone():
            return False, "Email already registered"
        ph = hash_password(password)
        cur.execute("INSERT INTO users(name,email,password_hash,role) VALUES(?,?,?,?)", (name, email, ph, role))
        self.db.commit()
        return True, "Registration successful"

    def login(self, email: str, password: str) -> Optional[User]:
        cur = self.db.cursor()
        cur.execute("SELECT * FROM users WHERE email = ?", (email,))
        row = cur.fetchone()
        if not row:
            return None
        if not verify_password(password, row['password_hash']):
            return None
        return User(id=row['id'], name=row['name'], email=row['email'], password_hash=row['password_hash'], role=row['role'])

class CarService:
    def __init__(self):
        self.db = Database().conn

    def list_available(self) -> List[Car]:
        cur = self.db.cursor()
        cur.execute("SELECT * FROM cars WHERE available = 1")
        rows = cur.fetchall()
        return [Car(id=r['id'], make=r['make'], model=r['model'], year=r['year'], mileage=r['mileage'], available=bool(r['available']), min_days=r['min_days'], max_days=r['max_days'], daily_rate=r['daily_rate']) for r in rows]

    def list_all(self) -> List[Car]:
        cur = self.db.cursor()
        cur.execute("SELECT * FROM cars")
        rows = cur.fetchall()
        return [Car(id=r['id'], make=r['make'], model=r['model'], year=r['year'], mileage=r['mileage'], available=bool(r['available']), min_days=r['min_days'], max_days=r['max_days'], daily_rate=r['daily_rate']) for r in rows]

    def add_car(self, car: Car) -> int:
        cur = self.db.cursor()
        cur.execute(
            "INSERT INTO cars(make,model,year,mileage,available,min_days,max_days,daily_rate) VALUES(?,?,?,?,?,?,?,?)",
            (car.make, car.model, car.year, car.mileage, int(car.available), car.min_days, car.max_days, car.daily_rate),
        )
        self.db.commit()
        return cur.lastrowid

    def update_car(self, car_id: int, **fields) -> bool:
        if not fields:
            return False
        keys = ", ".join([f"{k}=?" for k in fields.keys()])
        values = list(fields.values()) + [car_id]
        cur = self.db.cursor()
        cur.execute(f"UPDATE cars SET {keys} WHERE id = ?", values)
        self.db.commit()
        return cur.rowcount > 0

    def delete_car(self, car_id: int) -> bool:
        cur = self.db.cursor()
        cur.execute("DELETE FROM cars WHERE id = ?", (car_id,))
        self.db.commit()
        return cur.rowcount > 0

class BookingService:
    def __init__(self):
        self.db = Database().conn

    def _parse_date(self, s: str) -> date:
        return datetime.strptime(s, DATE_FMT).date()

    def _car_constraints(self, car_id: int) -> Tuple[int,int,float]:
        cur = self.db.cursor()
        cur.execute("SELECT min_days, max_days, daily_rate FROM cars WHERE id=?", (car_id,))
        row = cur.fetchone()
        if not row:
            raise ValueError("Car does not exist")
        return row['min_days'], row['max_days'], row['daily_rate']

    def _is_available(self, car_id: int, start: date, end: date) -> bool:
        # No overlap with approved bookings for the same car.
        cur = self.db.cursor()
        cur.execute(
            """
            SELECT COUNT(*) AS cnt
            FROM bookings
            WHERE car_id = ? AND status = 'approved'
              AND NOT (date(end_date) < date(?) OR date(start_date) > date(?))
            """,
            (car_id, start.isoformat(), end.isoformat()),
        )
        return cur.fetchone()['cnt'] == 0

    def create_booking(self, user_id: int, car_id: int, start_date: str, end_date: str) -> Tuple[bool,str]:
        start = self._parse_date(start_date)
        end = self._parse_date(end_date)
        if end < start:
            return False, "End date must be on/after start date"
        days = compute_days(start, end)
        mn, mx, rate = self._car_constraints(car_id)
        if days < mn or days > mx:
            return False, f"Rental length must be between {mn} and {mx} days"
        if not self._is_available(car_id, start, end):
            return False, "Car is not available for the selected dates"

        total = compute_total(rate, days)
        cur = self.db.cursor()
        cur.execute(
            """
            INSERT INTO bookings(user_id,car_id,start_date,end_date,days,status,total_fee,created_at)
            VALUES(?,?,?,?,?,'pending',?,?)
            """,
            (user_id, car_id, start.isoformat(), end.isoformat(), days, total, datetime.utcnow().isoformat()),
        )
        self.db.commit()

        bus.publish('booking.created', booking_id=cur.lastrowid, user_id=user_id, car_id=car_id, days=days, total=total)
        return True, f"Booking submitted (pending). Estimated total: ${total:.2f}"

    def list_user_bookings(self, user_id: int):
        cur = self.db.cursor()
        cur.execute(
            """
            SELECT b.*, c.make, c.model
            FROM bookings b JOIN cars c ON b.car_id=c.id
            WHERE b.user_id=?
            ORDER BY b.created_at DESC
            """,
            (user_id,),
        )
        return cur.fetchall()

    def list_all_bookings(self):
        cur = self.db.cursor()
        cur.execute(
            """
            SELECT b.*, u.name as user_name, u.email as user_email, c.make, c.model
            FROM bookings b
            JOIN users u ON b.user_id=u.id
            JOIN cars c ON b.car_id=c.id
            ORDER BY b.created_at DESC
            """
        )
        return cur.fetchall()

    def set_status(self, booking_id: int, status: str) -> bool:
        if status not in ('approved','rejected'):
            return False
        cur = self.db.cursor()
        cur.execute("UPDATE bookings SET status=? WHERE id=?", (status, booking_id))
        self.db.commit()
        if cur.rowcount:
            bus.publish(f'booking.{status}', booking_id=booking_id)
        return cur.rowcount > 0
