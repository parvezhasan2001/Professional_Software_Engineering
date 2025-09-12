
from datetime import date

def compute_days(start: date, end: date) -> int:
    delta = (end - start).days + 1  # inclusive
    return max(delta, 0)

def compute_total(daily_rate: float, days: int) -> float:
    base = daily_rate * days
    # Simple discount: 10% off for rentals longer than a week
    discount = 0.10 * base if days >= 7 else 0.0
    return round(base - discount, 2)
