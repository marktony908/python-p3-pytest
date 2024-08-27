# lib/not_none_functions.py

def check_not_none(value):
    if value is None:
        raise ValueError("Value cannot be None")
    return value
