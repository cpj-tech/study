# メールアドレス判定アルゴリズム

## 問題

- 入力した文字列がメールアドレスとして正しいか検証する。
- メールアドレスは「ローカル部@ドメイン部」という形式になっている
- kasama@gmail.comの場合、kasama がローカル部で gmail.com がドメイン部
- ドメイン部はメールサーバーを識別する文字列
- ローカル部はそのメールサーバーに登録しているユーザーを識別する文字列
- ローカル部とドメイン部の区切りには必ず「@」が一つある。
- インターネットの世界には RFC(Request For Comments)と呼ばれる文書がある。
  - RFC5321(Simple Mail Transfer Protocol)および RFC5322(Internet Message Format)という文書の中で、メールアドレスのローカル部とドメイン部で使用できる文字の種類が以下のように定義されています。
  - ローカル部で使用できる文字列：
    - 大小の英字(A~Z,a~z)
    - 数字(0~9)
    - 記号(!#$#%&'\*+-/=?^\_`{|}~)
    - ""で囲めば、()<>[]:;@,.スペースも使用できる
    - \"とすれば" を使用できる
  - ドメイン部で使用できる文字：
    - 大小の英字(A~Z,a~z)
    - 数字(0~9)
    - ハイフン(先頭以外)
    - ドット(先頭と末尾以外であり、2 個以上連続しない)
    - []で囲まれた IP アドレス

## 条件

- 本章のメールアドレス判定ルール:
  - 「ローカル部@ホスト部」という形式である
  - 「ローカル部」と「ホスト部」では大小の英字、数字、ドットが使える
  - ドットは先頭と末尾以外であり、2 個以上連続して使わない

## 出力例

```
kasamayoshiki@kasamakichitakanoMacBook-Pro NikkeiSW % python emailcheck1.py
文字列-->kasama.yoshiki@gmail.com
メールアドレスです。
kasamayoshiki@kasamakichitakanoMacBook-Pro NikkeiSW %
```

## アルゴリズム

### 参考画像

- <img width="867" alt="image" src="https://github.com/cpj-tech/study/assets/61643054/834c968e-0f4d-4c4c-b450-be078ce418ef">
- <img width="538" alt="image" src="https://github.com/cpj-tech/study/assets/61643054/639fcf08-d6ec-48a5-931a-7b723cf0271a">

### tips

- python では re モジュールを用いて文字列が形式あっているか簡単に判定できますが、ここではアルゴリズムを理解するために re モジュールを使わずに手作りします。
- python には isalnum 関数が用意されていますがあえて手作りします。

## 発展系

- プログラムの可読性が低くなる場合は、マジックナンバーに定数を割り当てる。
- 郵便番号や電話番号などの形式をチェックするプログラムも試して見てね。
