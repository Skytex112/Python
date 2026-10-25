from pathlib import Path


def show_all_files(directory, indent=""):
    try:
        for item in sorted(directory.iterdir()):
            if item.is_dir():
                print(f"{indent}Каталог: {item}")
                show_all_files(item, indent + "  ")
            else:
                print(f"{indent}Файл: {item}")
    except OSError as error:
        print(f"Не вдалося прочитати каталог: {error}")


def show_tree(directory, indent=""):
    try:
        for item in sorted(directory.iterdir()):
            if item.is_dir():
                print(f"{indent}{item.name}:")
                show_tree(item, indent + "  ")
            else:
                print(f"{indent}{item.name}")
    except OSError as error:
        print(f"Не вдалося прочитати каталог: {error}")


def main():
    while True:
        print("\n1 — показати всі файли та каталоги")
        print("2 — показати структуру деревом")
        print("0 — вихід")
        choice = input("Ваш вибір: ").strip()

        if choice == "0":
            break
        if choice not in ("1", "2"):
            print("Оберіть 1, 2 або 0.")
            continue

        directory = Path(input("Введіть шлях до каталогу: ").strip().strip('"'))
        if not directory.is_dir():
            print("Помилка: каталог не знайдено.")
            continue

        if choice == "1":
            show_all_files(directory)
        else:
            print(f"{directory.name or directory}:")
            show_tree(directory)


if __name__ == "__main__":
    main()
