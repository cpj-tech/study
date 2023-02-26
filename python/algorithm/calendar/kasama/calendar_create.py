import datetime
import calendar

calendar.setfirstweekday(calendar.SUNDAY)


def main():

    year = int(input("西暦を入力してください: "))

    month = int(input("月を入力してください: "))

    # 指定された年月の最初の日を取得
    first_day = datetime.date(year, month, 1)
    # 前月の日数を取得
    prev_month_days = calendar.monthrange(year, month - 1)[1] if month != 1 else calendar.monthrange(year - 1, 12)[1]

    # 月の日数を取得
    # calendar.monthrange: return 月の最初の曜日, 月の日数
    days = calendar.monthrange(year, month)[1]
    # 最終日をdate型に変換
    last_day = datetime.date(year, month, days)

    # カレンダーを作成
    cal = calendar.monthcalendar(year, month)
    print("cal:", cal)
    # cal: [[0, 0, 0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11],
    # [12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25],
    #  [26, 27, 28, 0, 0, 0, 0]]
    # 前月の日付の埋め方
    # 0:月=1埋める,
    # 1:火=2埋める,
    # 2:水=3埋める,
    # 3:木=4埋める,
    # 4:金=5埋める,
    # 5:土=6埋める,
    # 6:日=0埋める
    roop_range = 1 + first_day.weekday() if first_day.weekday() != 6 else 0
    # 前月の日付を埋める
    for _ in range(roop_range):
        cal[0].insert(0, prev_month_days)
        prev_month_days -= 1
    # 次月の日付けの埋め方
    # 0:月=5埋める,
    # 1:火=4埋める,
    # 2:水=3埋める,
    # 3:木=2埋める,
    # 4:金=1埋める,
    # 5:土=0埋める,
    # 6:日=6埋める
    roop_range = 5 - last_day.weekday() if last_day.weekday() != 6 else last_day.weekday()
    # 次月の日付を埋める
    for i in range(roop_range):
        print(i + 1)
        cal[-1].append(i + 1)
    # カレンダーを出力
    print("cal:", cal)
    print("days(末日):", days)
    print("日  月  火  水  木  金  土")
    # cal: [[26, 27, 28, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11],
    # [12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25],
    #  [26, 27, 28, 29, 30, 31, 1]]
    for week in cal:
        week = [i for i in week if i != 0]
        for day in week:
            print("{:2d} ".format(day), end=" ")
        print("")


if __name__ == "__main__":
    main()
