
def is_alphanumeric_mixed_case(letter):
    return "0" <= letter <= "9" or "A" <= letter <= "Z" or \
    "a" <= letter <= "z"

def main():
    input_address = input("文字列-->")
    print(input_address)
    state = "HEAD"
    for letter in input_address:
        if state == "HEAD":
                if letter == ".":
                    print("NG")
                elif state == "HEAD" and is_alphanumeric_mixed_case(letter):
                    state = "LOCAL"
                    continue
        elif state == "LOCAL":
                if letter == ".":
                    state == "LOCAL_DOT"


if __name__ == "__main__":
    main()