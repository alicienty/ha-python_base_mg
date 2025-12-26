import argparse
def main():
    parser = argparse.ArgumentParser(
        description='Описание программы',  # Описание в help
        epilog=''  # Текст в конце help
    )

    # Добавление аргументов...
    parser.add_argument('file_name', default= 'file_name.txt', type=str, help='путь к текстовому файлу')
    parser.add_argument('--words', action='store_true', help='подсчет всех слов в документе')
    parser.add_argument('--chars', action='store_true', help='подсчет всех символов в документе')
    parser.add_argument('--lines', action='store_true', help='подсчет всех строк в документе')

    args = parser.parse_args()  # Парсинг аргументов
    file_name = args.file_name
    words = args.words
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден")

    response = {}
    if args.words:
        words_count = str(len(text.split()))
        response["words"] = words_count
    if args.chars:
        chars_count = str(len(text))
        response["chars"] = chars_count
    if args.lines:
        lines_count = str(len(text.splitlines()))
        response["lines"] = lines_count

    print(response)

if __name__ == '__main__':
    main()