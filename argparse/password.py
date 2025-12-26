import secrets
import string
import argparse


def parsing():
    parser = argparse.ArgumentParser(
        description='Программа генерирует пароли в зависимости от требований пользователя',  # Описание в help
        epilog='Если пользователь не указал ни один аргумент, программа генерирует самый простой пароль из текстовых символов')# Текст в конце help)

    # Добавление аргументов...
    parser.add_argument('length', default= 8, type=int, help='длина пароля в символах')
    parser.add_argument('--uppercase', action='store_true', help='добавляет в пароль заглавные буквы')
    parser.add_argument('--digits', action='store_true', help='добавляет в пароль заглавные цифры')
    parser.add_argument('--symbols', action='store_true', help='добавляет в пароль символы типа !?,')

    return parser

def generate_password(args):
    length = args.length
    characters = string.ascii_letters
    password = "".join(secrets.choice(characters) for _ in range(length))

    if args.uppercase and not args.digits and not args.symbols:
        while True:
            password = "".join(secrets.choice(characters) for _ in range(length))
            if any (s.isupper() for s in password):
                break

    if args.digits and not args.uppercase and not args.symbols:
        characters = string.ascii_letters + string.digits
        while True:
            password = "".join(secrets.choice(characters) for _ in range(length))
            if any(s.isdigit() for s in password):
                break

    if args.symbols and not args.digits and not args.uppercase:
        characters = string.ascii_letters + string.punctuation
        while True:
            password = "".join(secrets.choice(characters) for _ in range(length))
            if any(not s.isalnum() for s in password):
                break

    if args.uppercase and args.digits and not args.symbols:
        while True:
            characters = string.ascii_letters + string.digits
            password = "".join(secrets.choice(characters) for _ in range(length))
            if any(s.isupper() for s in password) and any(s.isdigit() for s in password):
                break

    if args.uppercase and args.symbols and not args.digits:
        while True:
            characters = string.ascii_letters + string.punctuation
            password = "".join(secrets.choice(characters) for _ in range(length))
            if any(s.isupper() for s in password) and any(not s.isalnum() for s in password):
                break

    if args.uppercase and args.symbols and args.digits:
        while True:
            characters = string.ascii_letters + string.punctuation + string.digits
            password = "".join(secrets.choice(characters) for _ in range(length))
            if any(s.isupper() for s in password) and any(not s.isalnum() for s in password) and any(s.isdigit() for s in password):
                break

    if args.symbols and not args.uppercase and args.digits:
        while True:
            characters = string.ascii_letters + string.punctuation + string.digits
            password = "".join(secrets.choice(characters) for _ in range(length))
            if any(not s.isalnum() for s in password) and any (s.isdigit() for s in password):
                break

    return password

def main():
    parser = parsing()
    args = parser.parse_args()
    pswd = generate_password(args)
    return print(pswd)

if __name__ == '__main__':
    main()
