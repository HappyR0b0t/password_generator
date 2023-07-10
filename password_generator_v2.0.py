import secrets
import string


def char_count():
    while True:
        PWD_LENGTH = input("Enter a desired character count: ")
        try:
            PWD_LENGTH = int(PWD_LENGTH)
        except:
            print("Please enter integer number as a desired password character count: ")
            continue
        if PWD_LENGTH < 1:
            print("Password character count must be greater than zero: ")
            continue
        return PWD_LENGTH

def exclusion_choice(m, chars):
    while True:
        m = input(f"Exclude characters like '{chars}' ? Enter yes/no: ")
        try:
            m = str(m)
        except:
            print("Please enter yes/no: ")
            continue
        if m == 'yes':
            return True
        elif m == 'no':
            return False
        else:
            continue

def pwd_generator(PWD_LENGTH):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    similar_characters = 'il1Lo0O'
    ambigous_chars =  '{}[\\]()/\'"`~,;:.<>|'
    alphabet = letters + digits + special_chars

    EXCL_SMLR_CHARS = False
    EXCL_AMBGS_CHARS = False
    PWD = ''

    EXCL_SMLR_CHARS = exclusion_choice(EXCL_SMLR_CHARS, similar_characters)
    EXCL_AMBGS_CHARS = exclusion_choice(EXCL_AMBGS_CHARS, ambigous_chars)

    def char_exclusion(alphabet, chars):
        for i in chars:
            alphabet = alphabet.replace(i, '')
        return alphabet

    if EXCL_SMLR_CHARS == True:
        alphabet = char_exclusion(alphabet, similar_characters)

    if EXCL_AMBGS_CHARS == True:
        alphabet = char_exclusion(alphabet, ambigous_chars)

    for i in range(PWD_LENGTH):
        PWD += ''.join(secrets.choice(alphabet))

    print("Your password is:")
    print(PWD)

def main():
    pwd_generator(char_count())

main()
