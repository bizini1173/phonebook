# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# # 1. Создать файл для записи телефонной книги.         ++++++++
# - открытие файла на дозапись.
# 2. Подготовка меню для пользователя.                  +++++++++
# # 3. Запись данных в файл по каждому контакту:
# - ввод данных пользователя,                           +++++
# - подготовка данных для записи в файл,                +++++
# - открытие файла в режиме дозаписи,                   +++++
# - запись новой строки с данными                       +++++
# # 4. Чтение данных из файла:                          +++++++
# - открытие файла в режиме чтения,                     ++++++++++
# - считать все данные и вывести их на экран.           ++++++
# 5. Поиск записей по параметрам и вывод соответствующих данных
# - ввод пользователем параметра поиска,
# - открыть файл в режиме чтения,
# - считать все данные из файла и сохранить их в программе,
# - сделать выборку нужной записи - сам поиск,
# - показать результат поиска.

def input_name():
    return input("Введите имя контакта: ")


def input_surname():
    return input("Введите фамилию контакта: ")


def input_patronymic():
    return input("Введите отчетство контакта: ")


def input_phone():
    return input("Введите телефон контакта: ")


def input_adress():
    return input("Введите адрес контакта: ")


def input_data():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    adress = input_adress()
    str_contact = f"{surname} {name} {patronymic} {phone}\n{adress}\n\n"
    with open("phonebook.txt", "a", encoding="UTF-8") as file:
        file.write(str_contact)


def read_file():
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        return file.read()


def print_data():
    print(read_file())


def search_contact():
    print("Варианты для поиска:\n"
          "1) Фамилия\n"
          "2) Имя\n"
          "3) Отчество\n"
          "4) Телефон\n"
          "5) Адрес")
    command = input("Укажите вариант поиска: ")
    while command not in ("1", "2", "3", "4", "5"):
        print("Некорректный ввод номера варианта!\n"
              "Повторите ввод")
        command = input("Укажите номер варианта: ")
    print()
    i_search_param = int(command) - 1
    search = input("Введите данные для поиска: ").title()
    contacts_list = read_file().rstrip().split("\n\n")
    # print(contacts_list)

    for contact_str in contacts_list:
        contact_lst = contact_str.replace("\n", " ").split()
        # print(contact_lst)
        if search in contact_lst[i_search_param]:
            print(contact_str + "\n")



def update_contact():
    search_term = input("Введите имя или фамилию контакта для изменения: ").title()
    contacts_list = read_file().rstrip().split("\n\n")
    found_contacts = []

    for contact_str in contacts_list:
        contact_lst = contact_str.replace("\n", " ").split()
        if search_term in contact_lst[0] or search_term in contact_lst[1]:
            found_contacts.append(contact_str)

    if not found_contacts:
        print("Контакт не найден.")
    else:
        print("Найденные контакты:")
        for i, contact_str in enumerate(found_contacts):
            print(f"{i + 1}: {contact_str}")

        choice = int(input("Выберите номер контакта для изменения: ")) - 1
        if 0 <= choice < len(found_contacts):
            selected_contact = found_contacts[choice]
            contact_data = selected_contact.split("\n")
            print("Выберите поле для изменения:")
            print("1. Фамилия")
            print("2. Имя")
            print("3. Отчество")
            print("4. Телефон")
            print("5. Адрес")
            field_choice = int(input("Введите номер поля: ")) - 1

            if 0 <= field_choice < 5:
                new_value = input(f"Введите новое значение для {contact_data[field_choice]}: ").strip()
                contact_data[field_choice] = new_value
                updated_contact = "\n".join(contact_data)
                contacts_list[contacts_list.index(selected_contact)] = updated_contact
                with open("phonebook.txt", "w", encoding="UTF-8") as file:
                    file.write("\n\n".join(contacts_list))
                print("Контакт успешно обновлен.")
            else:
                print("Некорректный выбор поля.")

        else:
            print("Некорректный выбор контакта.")

def delete_contact():
    search_term = input("Введите имя или фамилию контакта для удаления: ").title()
    contacts_list = read_file().rstrip().split("\n\n")
    found_contacts = []

    for contact_str in contacts_list:
        contact_lst = contact_str.replace("\n", " ").split()
        if search_term in contact_lst[0] or search_term in contact_lst[1]:
            found_contacts.append(contact_str)

    if not found_contacts:
        print("Контакт не найден.")
    else:
        print("Найденные контакты:")
        for i, contact_str in enumerate(found_contacts):
            print(f"{i + 1}: {contact_str}")

        choice = int(input("Выберите номер контакта для удаления: ") - 1)
        if 0 <= choice < len(found_contacts):
            deleted_contact = found_contacts.pop(choice)
            contacts_list = [c for c in contacts_list if c != deleted_contact]
            with open("phonebook.txt", "w", encoding="UTF-8") as file:
                file.write("\n\n".join(contacts_list))
            print("Контакт успешно удален.")

        else:
            print("Некорректный выбор контакта.")
def copy_contact():
    source_file_name = "phonebook.txt"
    destination_file_name = "phonebook_copy.txt"

    try:
        with open(source_file_name, "r", encoding="UTF-8") as source_file:
            contacts = source_file.read().split("\n\n")
        
        if not contacts:
            print("Справочник пуст.")
            return

        print("Список контактов:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}: {contact}")

        choice = int(input("Введите номер контакта, который необходимо скопировать: ")) - 1

        if 0 <= choice < len(contacts):
            contact_to_copy = contacts[choice]

            with open(destination_file_name, "a", encoding="UTF-8") as destination_file:
                destination_file.write(contact_to_copy + "\n\n")
            
            print("Контакт успешно скопирован.")
        else:
            print("Некорректный выбор контакта.")
    except FileNotFoundError:
        print(f"Файл {source_file_name} не найден.")

def interface():
    while True:
        print("Выберите вариант работы с телефонной книгой:")
        print("1) Запись данных")
        print("2) Вывод телефонной книги на экран")
        print("3) Поиск данных")
        print("4) Изменение данных контакта")
        print("5) Удаление контакта")
        print("6) Копирование контакта в другой файл")
        print("7) Выход")
        command = input("Введите номер операции: ")
        
        if command == "1":
            input_data()
        elif command == "2":
            print_data()
        elif command == "3":
            search_contact()
        elif command == "4":
            update_contact()
        elif command == "5":
            delete_contact()
        elif command == "6":
            copy_contact()
        elif command == "7":
            print("Приложение закрыто!")
            break

if __name__ == "__main__":
    interface()

