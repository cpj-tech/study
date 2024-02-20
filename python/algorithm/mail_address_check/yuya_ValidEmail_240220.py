def is_valid_dot(input):
    """ドットが 先頭 末尾 2連続 だったら False"""
    is_valid = True
    if input[0] == ".":
        is_valid = False
    elif input[-1] == ".":
        is_valid = False
    for a in input:
        cnt = 0
        if a == ".":
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            is_valid = False
    return is_valid

def is_valid_char(input_char):
    """大小の英字、数字、ドット 以外False"""
    return "0" <= input_char <= "9" or \
           "A" <= input_char <= "Z" or \
           "a" <= input_char <= "z" or \
           "." == input_char

def is_email(mail_str: str):
    mail_part_list = mail_str.split("@")
    if len(mail_part_list) != 2:
        return False
    for mail_part in mail_part_list:
        if is_valid_dot(mail_part):
            for part_char in mail_part:
                if not is_valid_char(part_char):
                    return False
        else:
            return False
    return True



def main():
    # ver 切り替えしたい
    # テストコード書きたい
    input_str = input()
    result = is_email(input_str)
    if result:
        print("success!")
    else:
        print("Fail..")


if __name__ == "__main__":
    main()