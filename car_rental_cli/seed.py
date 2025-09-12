
from db import Database
from auth import hash_password

def seed():
    db = Database().conn
    cur = db.cursor()
    # Seed admin
    cur.execute("SELECT id FROM users WHERE email = 'admin@car.com'")
    if not cur.fetchone():
        cur.execute(
            "INSERT INTO users(name,email,password_hash,role) VALUES(?,?,?,?)",
            ("Admin", "admin@car.com", hash_password("admin123"), "admin"),
        )
    # Seed cars
    cur.execute("SELECT COUNT(*) as cnt FROM cars")
    if cur.fetchone()['cnt'] == 0:
        cars = [
            ("Toyota", "Corolla", 2020, 45000, 1, 1, 30, 55.0),
            ("Honda", "Civic", 2019, 52000, 1, 1, 21, 50.0),
            ("Tesla", "Model 3", 2022, 12000, 1, 2, 14, 120.0),
        ]
        cur.executemany(
            "INSERT INTO cars(make,model,year,mileage,available,min_days,max_days,daily_rate) VALUES(?,?,?,?,?,?,?,?)",
            cars
        )
    db.commit()

if __name__ == "__main__":
    seed()
    print("Seed complete.")
