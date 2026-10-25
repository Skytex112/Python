import re
from pathlib import Path


VOWELS = "aeiouаеєиіїоуюя"


def read_text(path):
    try:
        return Path(path).read_text(encoding="utf-8")
    except OSError as error:
        print(f"Не вдалося прочитати файл: {error}")
        return None


def save_text(path, text):
    try:
        Path(path).write_text(text, encoding="utf-8")
        print("Результат збережено.")
        return True
    except OSError as error:
        print(f"Не вдалося записати файл: {error}")
        return False


def compare_files():
    first_path = input("Шлях до першого файлу: ").strip().strip('"')
    second_path = input("Шлях до другого файлу: ").strip().strip('"')
    first_text = read_text(first_path)
    second_text = read_text(second_path)

    if first_text is None or second_text is None:
        return

    first_lines = first_text.splitlines()
    second_lines = second_text.splitlines()

    if first_lines == second_lines:
        print("Рядки файлів збігаються.")
        return

    print("Рядки, що не збігаються:")
    for index in range(max(len(first_lines), len(second_lines))):
        first_line = first_lines[index] if index < len(first_lines) else "(рядка немає)"
        second_line = second_lines[index] if index < len(second_lines) else "(рядка немає)"
        if first_line != second_line:
            print(f"Рядок {index + 1}:")
            print(f"Перший файл: {first_line}")
            print(f"Другий файл: {second_line}")


def file_statistics():
    path = input("Шлях до текстового файлу: ").strip().strip('"')
    text = read_text(path)
    if text is None:
        return

    letters = [character.lower() for character in text if character.isalpha()]
    vowels = sum(character in VOWELS for character in letters)
    consonants = len(letters) - vowels
    digits = sum(character.isdigit() for character in text)

    statistics = (
        f"Кількість символів: {len(text)}\n"
        f"Кількість рядків: {len(text.splitlines())}\n"
        f"Кількість голосних літер: {vowels}\n"
        f"Кількість приголосних літер: {consonants}\n"
        f"Кількість цифр: {digits}\n"
    )
    result_path = input("Шлях для файлу зі статистикою: ").strip().strip('"')
    save_text(result_path, statistics)


def remove_last_line():
    path = input("Шлях до текстового файлу: ").strip().strip('"')
    text = read_text(path)
    if text is None:
        return

    lines = text.splitlines(keepends=True)
    result_path = input("Шлях для нового файлу: ").strip().strip('"')
    save_text(result_path, "".join(lines[:-1]))


def longest_line():
    path = input("Шлях до текстового файлу: ").strip().strip('"')
    text = read_text(path)
    if text is None:
        return

    length = max((len(line) for line in text.splitlines()), default=0)
    print(f"Довжина найдовшого рядка: {length}")


def count_word():
    path = input("Шлях до текстового файлу: ").strip().strip('"')
    text = read_text(path)
    if text is None:
        return

    word = input("Введіть слово для пошуку: ").strip()
    if not word:
        print("Слово не може бути порожнім.")
        return

    matches = re.findall(rf"\b{re.escape(word)}\b", text, flags=re.IGNORECASE)
    print(f"Слово «{word}» зустрічається {len(matches)} разів.")


def replace_word():
    path = input("Шлях до текстового файлу: ").strip().strip('"')
    text = read_text(path)
    if text is None:
        return

    old_word = input("Слово, яке потрібно замінити: ").strip()
    new_word = input("Нове слово: ")
    if not old_word:
        print("Слово для пошуку не може бути порожнім.")
        return

    result, count = re.subn(
        rf"\b{re.escape(old_word)}\b",
        lambda match: new_word,
        text,
        flags=re.IGNORECASE,
    )
    if save_text(path, result):
        print(f"Замінено слів: {count}")


def main():
    while True:
        print("\nОберіть завдання:")
        print("1 — порівняти два файли")
        print("2 — зберегти статистику файлу")
        print("3 — видалити останній рядок")
        print("4 — знайти найдовший рядок")
        print("5 — порахувати слово")
        print("6 — замінити слово")
        print("0 — вихід")
        choice = input("Ваш вибір: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            compare_files()
        elif choice == "2":
            file_statistics()
        elif choice == "3":
            remove_last_line()
        elif choice == "4":
            longest_line()
        elif choice == "5":
            count_word()
        elif choice == "6":
            replace_word()
        else:
            print("Оберіть число від 0 до 6.")


if __name__ == "__main__":
    main()