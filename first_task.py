from datetime import datetime, timedelta

# Даты проката фильма
schedule = [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7))
]

# Функция для вывода всех дат в периодах
def print_movie_dates(schedule):
    for start_date, end_date in schedule:
        current_date = start_date
        while current_date <= end_date:
            print(current_date)
            current_date += timedelta(days=1)

# Вызываем функцию и печатаем даты
print_movie_dates(schedule)