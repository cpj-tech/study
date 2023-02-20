weekdays = ["日", "月", "火", "水", "木", "金", "土"]


def get_dates_of_month(year, month):
    '''
    年/月に対応する日付一覧を取得する
    '''
    # 指定された月の日数
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # うるう年の場合は2月の日数を変更する
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        days_in_month[1] = 29

    # 指定された年と月の日付を格納する配列
    dates = [day for day in range(1, days_in_month[month-1]+1)]

    return dates


def get_first_day_of_month(year, month):
    '''
    初日に対応する曜日の添え字を返却
    0: 日, 1: 月...
    '''

    # 日曜日=0, 月曜日=1, ..., 土曜日=6
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= (month < 3)
    first_day = (year + year // 4 - year // 100 + year // 400 + t[month - 1]) % 7

    return first_day + 1


def get_last_day_of_month(year, month):
    '''
    終日に対応する曜日の添え字を返却
    0: 日, 1: 月...
    '''
    dates = get_dates_of_month(year, month)
    last_day = (len(dates) + get_first_day_of_month(year, month)) % 7
    # last_day_str = weekdays[last_day]

    return last_day - 1


def pre_fix_year_month(year, month):
    '''
    前月のyear, monthを取得
    '''

    if month == 0:
        return year - 1, 12
    else:
        return year, month


def ex_calendar_pre_dates(index_first_dates, pre_dates):
    '''
    カレンダーに表示する前月の日付を取得
    '''
    print(index_first_dates)
    if (index_first_dates == 7):
        return None
    else:
        return pre_dates[index_first_dates * -1:]


def ex_calendar_next_dates(index_last_dates, tmp_dates):
    '''
    カレンダーに表示する翌月の日付を取得
    '''

    if (index_last_dates == 6):
        return None
    else:
        return tmp_dates[:6 - index_last_dates]


def main():
    # 年と月を受け取る
    year = int(input("year = "))
    month = int(input("month = "))

    # 日付の配列を取得する
    dates = get_dates_of_month(year, month)
    # 前月の日付の配列を取得する
    pre_year, pre_month = pre_fix_year_month(year, month-1)
    pre_dates = get_dates_of_month(pre_year, pre_month)

    # 初日/終日の曜日の添え字を取得する
    index_first_day = get_first_day_of_month(year, month)
    index_last_day = get_last_day_of_month(year, month)

    # カレンダーに表示する前月の日付を配列で取得
    ex_pre_dates = ex_calendar_pre_dates(index_first_day, pre_dates)
    tmp_days = [1, 2, 3, 4, 5, 6, 7]
    ex_next_dates = ex_calendar_next_dates(index_last_day, tmp_days)

    # 前月と翌月の配列を結合
    calendar_dates = dates
    if ex_pre_dates is not None:
        calendar_dates = ex_pre_dates + dates
    if ex_next_dates is not None:
        calendar_dates = calendar_dates + ex_next_dates

    calendar = []
    for i in range(0, len(calendar_dates), 7):
        week = calendar_dates[i:i+7]
        calendar.append(week)

    for index, dow in enumerate(weekdays):
        crlf = '\n' if index == len(weekdays) - 1 else ''
        print(f'{dow :4}', end=crlf)
    # 各週を表示する
    for week in calendar:
        for day in week:
            print(f'{day}'.ljust(5), end='')
        print('')


if __name__ == '__main__':
    main()
