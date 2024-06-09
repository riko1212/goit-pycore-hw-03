from datetime import datetime, timedelta
import random
import re

def get_days_from_today(date):
    try:
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        today_date = datetime.today().date()
        difference = today_date.toordinal() - target_date.toordinal()
        return difference
    
    except ValueError:
        print("Incorrect date format, should be YYYY-MM-DD")
        return None
    
print(get_days_from_today("2023-11-09"))


def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= 1000 and 1 <= max <= 1000 and min <= max and min <= quantity <= max - min + 1):
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)


def normalize_phone(phone_number):
    phone_number = re.sub(r'[^\d+]', '', phone_number)
    
    if phone_number.startswith('380'):
        phone_number = '+' + phone_number
    elif not phone_number.startswith('+'):
        phone_number = '+38' + phone_number

    return phone_number

# Приклад використання функції
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)



def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        name = user["name"]
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        days_until_birthday = (birthday_this_year - today).days
        if 0 <= days_until_birthday <= 7:
            if birthday_this_year.weekday() >= 5: 
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            
            upcoming_birthdays.append({
                "name": name,
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "2017.06.13"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
