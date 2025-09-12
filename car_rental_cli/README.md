
# Car Rental System (CLI, Python stdlib only)

A simple, fully runnable car rental system using **Python standard library only** and **SQLite**.
No manual configuration is needed — the database is created on first run.

## Features
- User registration & login (roles: `admin`, `customer`)
- Admin: add/update/delete cars; approve/reject bookings
- Customer: browse available cars, create booking
- Pricing: daily rate × days with optional long-rental discount
- Availability checks: prevents overlaps with approved bookings
- Design patterns used:
  - **Singleton**: `Database` connection
  - **Factory Method**: `UserFactory` and `CarFactory`
  - **Observer**: simple event bus for notifications (e.g., booking status changes)

## Quick Start
```bash
# 1) Python 3.10+ recommended
python -V

# 2) (Optional) create venv
python -m venv .venv && . .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3) Install requirements (stdlib only; file included for completeness)
pip install -r requirements.txt

# 4) Run the app
python app.py
```

On first run, an admin and sample cars are seeded:
- Admin login: **admin@car.com** / **admin123**

## Files
- `app.py` — CLI entrypoint
- `db.py` — SQLite DB (Singleton) + schema creation
- `auth.py` — password hashing & verification
- `models.py` — simple dataclasses + factories
- `observer.py` — lightweight event bus
- `services.py` — user, car, and booking services
- `pricing.py` — fee calculation rules
- `seed.py` — initial admin + cars
- `requirements.txt` — empty (stdlib only)
- `architecture.txt` — high-level architecture & ASCII diagram
