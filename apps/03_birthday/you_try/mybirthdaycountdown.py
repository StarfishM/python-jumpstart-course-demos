import datetime


def print_header():
    print('-------------------------')
    print('   Birthday Countdown')
    print('-------------------------')
    print()


def get_birthday_from_user():
    print('When where you born?')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(year=target_date.year, month=original_date.month, day=original_date.day)
    dt = this_year - target_date
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print('You had your birthday {} days ago this year'.format(-days))
    elif days > 0:
        print('Your birthday is {} days from now'.format(days))
    else:
        print('Yayyyyyy, today is your special day, HAPPY BIRTHDAY')


def main():
    print_header()
    bday = get_birthday_from_user()
    print(bday)
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days)

main()
