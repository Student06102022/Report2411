# полное решение https://github.com/Monges/Zadacha-Goda?ysclid=m3svvd48r0668584473

from datetime import datetime

def get_weekday(day, month, year):
    # Определяем день недели для заданной даты
    date = datetime(year, month, day)
    return date.strftime("%A")  # Возвращаем название дня недели

def is_leap_year(year):
    # Определяем, является ли год високосным
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(day, month, year):
    # Рассчитываем возраст пользователя
    today = datetime.now()
    birth_date = datetime(year, month, day)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def display_date_with_stars(day, month, year):
    # Форматируем дату в виде дд мм гггг с звёздочками
    date_str = f"{day:02d} {month:02d} {year}"
    star_str = ' '.join(['*' * len(part) for part in date_str.split()])
    print(star_str)

# Запрос данных у пользователя
day = int(input("Введите день рождения (1-31): "))
month = int(input("Введите месяц рождения (1-12): "))
year = int(input("Введите год рождения (например, 1990): "))

# Определяем день недели
weekday = get_weekday(day, month, year)
print(f"Ваш день рождения выпал на: {weekday}")

# Проверяем, был ли год високосным
if is_leap_year(year):
    print(f"{year} год был високосным.")
else:
    print(f"{year} год не был високосным.")

# Рассчитываем возраст
age = calculate_age(day, month, year)
print(f"Вам сейчас {age} лет.")

# Выводим дату рождения в формате с звёздочками
print("Ваша дата рождения в формате дд мм гггг:")
display_date_with_stars(day, month, year)
