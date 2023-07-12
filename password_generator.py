import secrets
import string


similar_chars = 'il1Lo0O'
ambigous_chars = '{}[\\]()/\'"`~,;:.<>|'
alphabet = string.ascii_letters + string.digits + string.punctuation


def char_count():
    while True:
        pwd_length = input("Enter a desired character count: ")
        try:
            pwd_length = int(pwd_length)
        except ValueError:
            print(
                "Please enter integer number as a"
                "desired password character count: "
            )
            continue
        if pwd_length < 1:
            print("Password character count must be greater than zero: ")
            continue
        return pwd_length


def exclusion_choice(chars):
    while True:
        yes_no = input(f"Exclude characters like '{chars}' ? Enter yes/no: ")

        if yes_no == 'yes':
            return True
        elif yes_no == 'no':
            return False
        else:
            continue


def char_exclusion(alphabet, chars):
    excl_chars = exclusion_choice(chars)

    if excl_chars is True:
        for i in chars:
            alphabet = alphabet.replace(i, '')

    return alphabet


def pwd_generator(pwd_length, alphabet):
    pwd = ''

    for _ in range(pwd_length):
        pwd += secrets.choice(alphabet)

    return pwd


def main():
    pwd = pwd_generator(
        char_count(),
        char_exclusion(char_exclusion(alphabet, similar_chars), ambigous_chars)
    )
    print("Your password is: ", pwd)


if __name__ == "__main__":
    main()
