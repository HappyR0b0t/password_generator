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


def char_exclusion(alphabet, chars):
    if exclusion_choice(chars):
        for i in chars:
            alphabet = alphabet.replace(i, '')
    return alphabet


def pwd_generator(pwd_length, alphabet):
    return "".join(secrets.choice(alphabet) for _ in range(pwd_length))


def main(alphabet=alphabet):
    pwd_length = char_count()
    alphabet = char_exclusion(alphabet, similar_chars)
    alphabet = char_exclusion(alphabet, ambigous_chars)
    pwd = pwd_generator(pwd_length, alphabet)
    print("Your password is: ", pwd)


if __name__ == "__main__":
    main()
