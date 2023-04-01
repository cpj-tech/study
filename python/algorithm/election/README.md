# 選挙で過半数取った人を探し出すアルゴリズム

## 問題

- あなたは生徒会長選挙の票を数える選挙管理委員になりました。票の過半数を取った人が当選です。
- 当選者を選定するアルゴリズムを考えてみましょう。
- sample 配列：

```
vote = [
    "山田太郎","鈴木花子","佐藤三郎","鈴木花子",
    "鈴木花子","佐藤三郎","鈴木花子","佐藤三郎",
    "鈴木花子","鈴木花子","山田太郎","山田太郎"
]
```

## 条件

- 特になし

## 出力例

```
(base) kasamayoshiki@kasamakichitakanoMacBook-Pro kasama % python find_election_winner.py
鈴木花子が過半数を取りました。
(base) kasamayoshiki@kasamakichitakanoMacBook-Pro kasama %

(base) kasamayoshiki@kasamakichitakanoMacBook-Pro kasama % python find_election_winner.py
過半数を取得した人はいませんでした。
(base) kasamayoshiki@kasamakichitakanoMacBook-Pro kasama %
```

## アルゴリズム

### ボイヤーとムーアのレポート

### list の sort()
