import datetime


def day_computed(x):
    year, month, day = map(int, str(x).split('-'))
    dt_now = datetime.date.today()
    d_target = datetime.date(year, month, day)
    td = d_target - dt_now
    td_days = d_target - dt_now

    return td_days.days

# day_computed('2022-01-18')