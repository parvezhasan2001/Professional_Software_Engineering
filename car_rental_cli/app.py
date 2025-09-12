
from services import UserService, CarService, BookingService
from seed import seed
from observer import bus

def on_booking_event(payload):
    print(f"[EVENT] booking event: {payload}")

# subscribe console logger
bus.subscribe('booking.created', on_booking_event)
bus.subscribe('booking.approved', on_booking_event)
bus.subscribe('booking.rejected', on_booking_event)

def main():
    seed()  # ensure admin & cars exist
    user_svc = UserService()
    car_svc = CarService()
    booking_svc = BookingService()

    current_user = None

    while True:
        if not current_user:
            print("""
            ===== Car Rental System =====
            1) Register
            2) Login
            3) Exit
            """)
            choice = input("Choose: ").strip()
            if choice == '1':
                name = input("Name: ")
                email = input("Email: ")
                pwd = input("Password: ")
                ok, msg = user_svc.register(name, email, pwd, role='customer')
                print(msg)
            elif choice == '2':
                email = input("Email: ")
                pwd = input("Password: ")
                u = user_svc.login(email, pwd)
                if u:
                    current_user = u
                    print(f"Welcome, {u.name} ({u.role})!\n")
                else:
                    print("Invalid credentials.\n")
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid option.\n")
            continue

        # Logged in
        if current_user.role == 'admin':
            print("""
            ===== Admin Menu =====
            1) List cars
            2) Add car
            3) Update car
            4) Delete car
            5) View bookings
            6) Approve booking
            7) Reject booking
            8) Logout
            """)
            ch = input("Choose: ").strip()
            if ch == '1':
                cars = car_svc.list_all()
                for c in cars:
                    print(f"[{c.id}] {c.make} {c.model} {c.year} | mileage:{c.mileage} | available:{c.available} | days {c.min_days}-{c.max_days} | ${c.daily_rate}/day")
            elif ch == '2':
                make = input("Make: ")
                model = input("Model: ")
                year = int(input("Year: "))
                mileage = int(input("Mileage: "))
                available = input("Available now? (y/n): ").lower().startswith('y')
                min_days = int(input("Min days: "))
                max_days = int(input("Max days: "))
                rate = float(input("Daily rate: "))
                # quick inline object matching Car's attributes
                cid = car_svc.add_car(type('Car', (), {'make':make,'model':model,'year':year,'mileage':mileage,'available':available,'min_days':min_days,'max_days':max_days,'daily_rate':rate,'id':None}))
                print(f"Added car id={cid}")
            elif ch == '3':
                cid = int(input("Car ID: "))
                print("Leave field blank to keep current value.")
                fields = {}
                for k in ["make","model","year","mileage","available","min_days","max_days","daily_rate"]:
                    val = input(f"{k}: ").strip()
                    if val != '':
                        if k in ("year","mileage","min_days","max_days"): val = int(val)
                        elif k in ("daily_rate",): val = float(val)
                        elif k=="available": val = 1 if val.lower().startswith('y') else 0
                        fields[k]=val
                ok = car_svc.update_car(cid, **fields)
                print("Updated" if ok else "No changes.")
            elif ch == '4':
                cid = int(input("Car ID: "))
                ok = car_svc.delete_car(cid)
                print("Deleted" if ok else "Not found.")
            elif ch == '5':
                rows = booking_svc.list_all_bookings()
                for r in rows:
                    print(f"[#{r['id']}] {r['make']} {r['model']} | {r['start_date']}→{r['end_date']} ({r['days']}d) | ${r['total_fee']} | {r['status']} | by {r['user_name']} <{r['user_email']}> ")
            elif ch == '6':
                bid = int(input("Booking ID to approve: "))
                ok = booking_svc.set_status(bid, 'approved')
                print("Approved" if ok else "Failed.")
            elif ch == '7':
                bid = int(input("Booking ID to reject: "))
                ok = booking_svc.set_status(bid, 'rejected')
                print("Rejected" if ok else "Failed.")
            elif ch == '8':
                current_user = None
            else:
                print("Invalid option\n")

        else:
            print("""
            ===== Customer Menu =====
            1) View available cars
            2) Book a car
            3) View my bookings
            4) Logout
            """)
            ch = input("Choose: ").strip()
            if ch == '1':
                for c in car_svc.list_available():
                    print(f"[{c.id}] {c.make} {c.model} {c.year} | mileage:{c.mileage} | days {c.min_days}-{c.max_days} | ${c.daily_rate}/day")
            elif ch == '2':
                cid = int(input("Car ID: "))
                start = input("Start date (YYYY-MM-DD): ")
                end = input("End date (YYYY-MM-DD): ")
                ok, msg = booking_svc.create_booking(current_user.id, cid, start, end)
                print(msg)
            elif ch == '3':
                rows = booking_svc.list_user_bookings(current_user.id)
                for r in rows:
                    print(f"[#{r['id']}] {r['make']} {r['model']} | {r['start_date']}→{r['end_date']} ({r['days']}d) | ${r['total_fee']} | {r['status']}")
            elif ch == '4':
                current_user = None
            else:
                print("Invalid option\n")

if __name__ == "__main__":
    main()
