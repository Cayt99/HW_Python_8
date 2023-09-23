import os

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return [line.strip().split(';') for line in f]
    return []

def save_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for entry in data:
            f.write(';'.join(entry) + '\n')

def find_entry(data, keyword):
    return [entry for entry in data if keyword in entry]

def edit_entry(data, index, new_entry):
    data[index] = new_entry

def delete_entry(data, index):
    del data[index]

filename = "Справочник.txt"
phonebook = load_data(filename)

while True:
    action = input("1: Показать, 2: Добавить, 3: Найти, 4: Редактировать, 5: Удалить, 6: Выйти\n")
    if action == '1':
        for i, entry in enumerate(phonebook):
            print(i, entry)
    elif action == '2':
        new_entry = []
        new_entry.append(input("Введите фамилию:\n"))
        new_entry.append(input("Введите имя:\n"))
        new_entry.append(input("Введите отчество:\n"))
        new_entry.append(input("Введите номер телефона:\n"))
        phonebook.append(new_entry)
        save_data(phonebook, filename)
        keyword = input("Введите ключево слово для поиска:\n")
        results = find_entry(phonebook, keyword)
        print(results)
    
    elif action == '4':
        for i, entry in enumerate(phonebook):
            print(f'{i}: {entry}')
        index = int(input('Выберите индекс для редактирования:'))
        new_entry = []
        new_entry.append(input("Введите фамилию:\n"))
        new_entry.append(input("Введите имя:\n"))
        new_entry.append(input("Введите отчество:\n"))
        new_entry.append(input("Введите номер телефона:\n"))
        edit_entry(phonebook, index, new_entry)
    elif action == '5':
        for i, entry in enumerate(phonebook):
            print(f'{i}: {entry}')
        index = int(input('Выберите индекс для удаления:'))
        delete_entry(phonebook, index)
        save_data(phonebook, filename)
    elif action == '6':
        break
