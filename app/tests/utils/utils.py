import random
import string
from datetime import datetime

def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"

def random_int(length: int) -> int:
    digits = '0123456789'
    random_number = ''.join(random.choice(digits) for i in range(length))
    return int(random_number)

def reandom_datetime() -> datetime:
    return f'{random_int()}/{random_int()}/{random_int()}'