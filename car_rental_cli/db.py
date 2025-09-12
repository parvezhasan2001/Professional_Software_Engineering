
import sqlite3
from pathlib import Path
from typing import Optional

DB_PATH = Path('car_rental.db')

class Database:
    _instance: Optional['Database'] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_connection()
        return cls._instance

    def _init_connection(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row
        self._create_schema()

    def _create_schema(self):
        cur = self.conn.cursor()
        # users
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                role TEXT NOT NULL CHECK(role IN ('admin','customer'))
            )
        ''')
        # cars
        cur.execute('''
            CREATE TABLE IF NOT EXISTS cars(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                make TEXT NOT NULL,
                model TEXT NOT NULL,
                year INTEGER NOT NULL,
                mileage INTEGER NOT NULL,
                available INTEGER NOT NULL DEFAULT 1,
                min_days INTEGER NOT NULL DEFAULT 1,
                max_days INTEGER NOT NULL DEFAULT 30,
                daily_rate REAL NOT NULL
            )
        ''')
        # bookings
        cur.execute('''
            CREATE TABLE IF NOT EXISTS bookings(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                car_id INTEGER NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                days INTEGER NOT NULL,
                status TEXT NOT NULL CHECK(status IN ('pending','approved','rejected')) DEFAULT 'pending',
                total_fee REAL NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(car_id) REFERENCES cars(id)
            )
        ''')
        self.conn.commit()

    def cursor(self):
        return self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()
