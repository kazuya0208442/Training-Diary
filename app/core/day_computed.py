import datetime

# 大会の日程が入力されるので、今日の日付から何日後に大会があるのかを計算する。
# day_computed('2022-01-18')
def day_computed(x):
    # 大会の日付を受け取る。
    year, month, day = map(int, str(x).split('-'))
    # 今日の日付を取得
    dt_now = datetime.date.today()
    # 大会の日付を取得
    d_target = datetime.date(year, month, day)
    # (大会の日付) - (今日の日付) = 残り日数
    td = d_target - dt_now
    return td.days

