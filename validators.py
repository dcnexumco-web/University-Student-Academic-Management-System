import re


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def validate_phone(phone_number):
    pattern = r"^0\d{10}$"
    return re.match(pattern, phone_number) is not None