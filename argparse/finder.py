import argparse
import os

def find_files(path, extensions):
    found_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if any(file.lower().endswith(ext.lower()) for ext in extensions):
                found_files.append(os.path.join(root, file))
    return found_files

def main():
    parser = argparse.ArgumentParser(
        description="программа ищет файлы в папке по расширениям"
    )
    parser.add_argument("path", help="путь к папке (/path/to/search)")
    parser.add_argument("--ext", nargs='+', required=True, help="расширения файлов без точки (txt, pdf)")

    args = parser.parse_args()
    path = args.path
    extensions = args.ext

    if not os.path.isdir(path):
        return print(f"'{path}' не является папкой, задайте другой путь")


    files = find_files(path, extensions)
    if files:
        print(f"Файлы с расширениями {extensions} в папке {path}:")
        for f in files:
            print(f)
    else:
        print(f"Файлы c расширениями {extensions} не найдены")

if __name__ == "__main__":
    main()
