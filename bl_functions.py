from datetime import date, datetime


def time_passed(input_str):
    input_date = datetime.strptime(input_str, '%d/%m/%Y')
    today = date.today()
    age = today.year - input_date.year - \
        ((today.month, today.day) < (input_date.month, input_date.day))

    return age
