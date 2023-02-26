vote = [
    "山田太郎", "鈴木花子", "佐藤三郎", "鈴木花子",
    "鈴木花子", "佐藤三郎", "鈴木花子", "佐藤三郎",
    "鈴木花子", "鈴木花子", "山田太郎", "山田太郎"
]


def count_person_vote():
    '''
    配列のそれぞれの要素数を数える
    '''
    vote_counts = {}
    for v in vote:
        if v in vote_counts:
            vote_counts[v] += 1
        else:
            vote_counts[v] = 1
    return vote_counts


def main():
    vote_counts = count_person_vote()
    # 結果を表示
    exist_winner = False
    for candidate, count in vote_counts.items():
        if len(vote) / 2 <= count:
            exist_winner = True
            print(f'{candidate}が過半数を取りました。')

    if not exist_winner:
        print('当選者はいませんでした。')


if __name__ == '__main__':
    main()
