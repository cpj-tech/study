import datetime
import calendar


def main():

    year = int(input("西暦を入力してください: "))

    month = int(input("月を入力してください: "))

    # 指定された年月の最初の日を取得
    first_day = datetime.date(year, month, 1)
    # 前月の日数を取得
    prev_month_days = calendar.monthrange(year, month - 1)[1] if month != 1 else calendar.monthrange(year - 1, 12)[1]
    # 月の日数を取得
    days = calendar.monthrange(year, month)[1]
    last_day = datetime.date(year, month, days)

    # カレンダーを作成
    cal = calendar.monthcalendar(year, month)
    # 次月の日数を取得
    # 前月の日付を埋める
    for _ in range(first_day.weekday()):
        cal[0].insert(0, prev_month_days)
        prev_month_days -= 1
    # 次月の日付を埋める
    for i in range(last_day.weekday()):
        cal[-1].append(i + 1)
    cals = []

    for week in cal:
        week = [i for i in week if i != 0]
        cals.append(week)

    print(cals)
    # カレンダーを出力
    print("日  月  火  水  木  金  土")
    for week in cals:
        week = [i for i in week if i != 0]
        for day in week:
            if day == 0:
                continue
            elif day > days:
                print("{:2d} ".format(day), end=" ")
            elif day <= (31 if days >= 31 else 30):
                print("{:2d} ".format(day), end=" ")
            else:
                print(" {:2d}".format(day), end=" ")
        print("")


if __name__ == "__main__":
    main()
