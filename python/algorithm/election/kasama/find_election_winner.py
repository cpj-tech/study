from collections import Counter


def main():
    vote = ["山田太郎", "鈴木花子", "佐藤三郎", "鈴木花子", "鈴木花子", "佐藤三郎", "鈴木花子", "佐藤三郎", "鈴木花子", "鈴木花子", "山田太郎", "山田太郎"]

    vote_count = Counter(vote)  # Counterオブジェクトを作成する
    majority_count = len(vote) // 2 + 1  # 過半数のカウントを計算する

    for candidate, count in vote_count.items():
        print(candidate, count)
        if count >= majority_count:
            print(f"{candidate}さんが過半数を獲得しました。")


if __name__ == "__main__":
    main()
