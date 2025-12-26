import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Описание программы',  # Описание в help
        epilog=''  # Текст в конце help
    )

    # Добавление аргументов...
    parser.add_argument('a', type=int, help='первая цифра')
    parser.add_argument('b', type=int, help='вторая цифра')
    parser.add_argument('--operation', type=str, choices=['add', 'subtract', 'multiply', 'divide'], help='тип операции')

    args = parser.parse_args()  # Парсинг аргументов

    if args.operation == "add":
        print(args.a + args.b)
    if args.operation == "subtract":
        print(args.a - args.b)
    if args.operation == "multiply":
        print(args.a * args.b)
    if args.operation == "divide":
        print(args.a / args.b)


if __name__ == "__main__":
    main()
