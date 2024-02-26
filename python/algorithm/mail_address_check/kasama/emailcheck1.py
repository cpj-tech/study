def is_alphanumeric_mixed_case(letter):
    return "0" <= letter <= "9" or "A" <= letter <= "Z" or "a" <= letter <= "z"


def main():
    input_address = input("文字列-->")
    print(input_address)
    state = "HEAD"
    count = 0
    for letter in input_address:
        count += 1
        if state == "HEAD":
            if letter == "." or not is_alphanumeric_mixed_case(letter):
                state = "NG"
                break
            elif is_alphanumeric_mixed_case(letter):
                state = "LOCAL"
                continue
        elif state == "LOCAL":
            if letter == ".":
                state = "LOCAL_DOT"
                continue
            elif is_alphanumeric_mixed_case(letter):
                continue
            elif letter == "@":
                state = "HOST"
            else:
                state = "NG"
                break
        elif state == "LOCAL_DOT":
            if letter == "." or not is_alphanumeric_mixed_case(letter):
                state = "NG"
                break
            else:
                state = "LOCAL"
                continue
        elif state == "HOST":
            if letter == ".":
                if count == len(input_address):
                    state = "NG"
                    break
                state = "HOST_DOT"
                continue
            elif is_alphanumeric_mixed_case(letter):
                continue
        elif state == "HOST_DOT":
            if letter == "." or not is_alphanumeric_mixed_case(letter):
                state = "NG"
                break
            else:
                state = "HOST"
                continue

    if state == "HOST":
        print("メールアドレスです。")
    else:
        print("メールアドレス形式に誤りがあります。")


if __name__ == "__main__":
    main()
