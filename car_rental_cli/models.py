
from dataclasses import dataclass
from typing import Literal

Role = Literal['admin','customer']

@dataclass
class User:
    id: int | None
    name: str
    email: str
    password_hash: str
    role: Role

class UserFactory:
    @staticmethod
    def create(name: str, email: str, password_hash: str, role: Role = 'customer') -> User:
        return User(id=None, name=name, email=email, password_hash=password_hash, role=role)

@dataclass
class Car:
    id: int | None
    make: str
    model: str
    year: int
    mileage: int
    available: bool
    min_days: int
    max_days: int
    daily_rate: float

class CarFactory:
    @staticmethod
    def create(make: str, model: str, year: int, mileage: int, available: bool, min_days: int, max_days: int, daily_rate: float) -> Car:
        return Car(id=None, make=make, model=model, year=year, mileage=mileage, available=available, min_days=min_days, max_days=max_days, daily_rate=daily_rate)
