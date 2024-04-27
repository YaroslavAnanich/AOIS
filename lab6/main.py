import table

def main():
    hash_table = table.HashTable(20)

    while True:
        print("\nХеш-таблица")
        print("1. Вставить элемент")
        print("2. Найти элемент")
        print("3. Удалить элемент")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            key = input("Введите ключ: ")
            value = input("Введите значение: ")
            hash_table.insert(key, value)
        elif choice == '2':
            key = input("Введите ключ: ")
            value = hash_table.search(key)
            if value is not None:
                print(f"Значение для ключа {key}: {value}")
            else:
                print(f"Элемент с ключом {key} не найден")
        elif choice == '3':
            key = input("Введите ключ: ")
            hash_table.delete(key)
        elif choice == '4':
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main()