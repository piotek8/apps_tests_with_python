import datetime
import calendar


def compute_days_between_dates(date1, date2):
    delta = date2 - date1
    return delta.days


def check_is_int(param):
    if not isinstance(param, int):
        raise ValueError('Faulty format. Input must be an integer. param: {}'.format(param))


def check_is_in_range(param, begin, end):
    if param not in range(begin, end):
        raise ValueError('Value {} not in range({},{})'.format(param, begin, end))
    pass


def check_year(year):
    check_is_int(year)
    check_is_in_range(year, 0, 2023 + 1)


# test na 0,2023 i , -1 2024

def check_month(month):
    check_is_int(month)
    check_is_in_range(month, 1, (12 + 1))


# def check_day(day, year, month):
#    check_is_int(day)
#    max_day = calendar.monthrange(year, month)[1]
#    check_is_in_range(day, 1, max_day)

def check_day(day, year, month):
    check_is_int(day)
    max_day = calendar.monthrange(year, month)[1]
    if not 1 <= day <= max_day:
        raise ValueError('Invalid day value. Day must be between 1 and {} for month {}.'.format(max_day, month))


def get_user_input():
    print('Write all information in integers')
    year = int(input("What year were you born? "))
    check_year(year)
    month = int(input("What month were you born? "))
    check_month(month)
    day = int(input("What day were you born? "))
    check_day(day, year, month)
    return datetime.date(year, month, day)


def main():
    today = datetime.date.today()
    birthdate = get_user_input()

    days_until_birthday = compute_days_between_dates(today, datetime.date(today.year, birthdate.month, birthdate.day))

    if days_until_birthday < 0:
        next_birthday = datetime.date(today.year + 1, birthdate.month, birthdate.day)
        days_until_birthday = compute_days_between_dates(today, next_birthday)

    print("Looks like you were born on", birthdate.strftime("%B %d, %Y"))
    print("Looks like your birthday is in", days_until_birthday, "days.")
    print("Hope you're looking forward to it!")


if __name__ == '__main__':
    main()
