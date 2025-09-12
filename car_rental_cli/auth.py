
import hashlib, secrets

# Simple deterministic hashing with per-user salt.
# For production, use argon2/bcrypt/scrypt. This demo uses stdlib only.
def hash_password(password: str, salt: str = None) -> str:
    if salt is None:
        salt = secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100_000)
    return f'{salt}${digest.hex()}'

def verify_password(password: str, stored: str) -> bool:
    try:
        salt, hexdigest = stored.split('$', 1)
    except ValueError:
        return False
    check = hash_password(password, salt)
    return check == stored
