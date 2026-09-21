import datetime
import random
import re


def get_days_from_today(date: str) -> int:
    try:
        date_object = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        return (date_object - datetime.datetime.today().date()).days
    except ValueError:
        return 0

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if min > max or quantity > max - min + 1 or min < 0 or quantity < 1 or max > 1000:
        return []
    numbers = sorted(random.sample(range(min, max + 1), quantity))
    return numbers

def normalize_phone(phone_number: str) -> str:
    phone_number = phone_number.strip()
    sanitized_number = re.sub(r'[^\d]', '', phone_number)
    if len(sanitized_number) == 10:
        return f"+38{sanitized_number}"
    elif len(sanitized_number) == 12 and sanitized_number.startswith("38"):
        return f"+{sanitized_number}"
    else:
        return f"+{sanitized_number}"

def get_upcoming_birthdays(users) -> list:
    today = datetime.datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year = today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year = today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year
            if congratulation_date.weekday() == 5:
                congratulation_date += datetime.timedelta(days = 2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += datetime.timedelta(days = 1)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y-%m-%d")
            })

    return upcoming_birthdays
