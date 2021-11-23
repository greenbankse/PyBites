from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


# def get_hundred_days_end_date():
#     """Return a string of yyyy-mm-dd"""
#     end_date = start_100days + timedelta(days=100)
#     years = str(end_date.year)
#     month = str(end_date.month) if end_date.month>9 else '0'+str(end_date.month)
#     day = str(end_date.day) if end_date.day>9 else '0'+str(end_date.day)
#     return f'{years}-{month}-{day}'
def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    return str(start_100days + timedelta(days=100))


def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    return int((pycon_date - pybites_founded).days)


print(int((pycon_date - pybites_founded).days))

