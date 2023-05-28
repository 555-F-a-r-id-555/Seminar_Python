# Задача No49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1.Программа должна выводить данные
# 2.Программа должна сохранять данные в текстовом файле
# 3.Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4.Использование функций. Ваша программа
# не должна быть линейной

# Задача 38: Дополнить телефонный справочник
# возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал
# для изменения и удаления данных.


# 1.Программа должна выводить данные
# 2.Программа должна сохранять данные в текстовом файле

def import_catalog():
    with open('catalog.txt', 'a') as catalog:
        (name, surname, patronymic, telephone) = [input(
            'Введите имя: ' if i == 0 else 'Введите фамилие: ' if i == 1 else 'Введите отчество: ' if i == 2 else 'Введите телефон: ')
            for i in range(4)]
        result = (name, surname, patronymic, telephone)
        list(map(lambda x: catalog.write(x + '\n\n' if x == telephone else x + '\n'), result))
        print(result)
        return result


import_catalog()

# 3.Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4.Использование функций. Ваша программа
# не должна быть линейной

# 3.1 формируем список пользователеей и их телефонов

def export_catalog():
    with open('catalog.txt', 'r') as catalog:
        lst = [i[:-1] for i in catalog.readlines() if i != '\n']
        result = [{i // 4: lst[i:i + 4]} for i in range(0, len(lst), 4)]
        print(result)
        return result


# export_catalog()


# 3.2 находим пользователя и телефон

def find_catalog(name='', surname='', patronymic='', telephone=''):
    catalog = export_catalog()
    print('Введите любой из заданных параметров, можно ввести несколько,либо оставить их пустыми...')
    (find_name, find_surname, find_patronymic, find_telephone) = [input(
        'Поиск по имени: ' if i == 0 else 'Поиска по фамилии: ' if i == 1 else 'Поиска по отчеству: ' if i == 2 else 'Поиска по телефону: ')
        for i in range(4)]
    global input_data
    input_data = (find_name, find_surname, find_patronymic, find_telephone)
    input_data = dict((i, x) for i, x in enumerate(input_data) if x != '')
    print(input_data)
    result = [d for d in catalog if
              all(list(d.values())[0][key] == value for key, value in input_data.items())]
    print(f'Найдено {len(result)} значения/ий: ', end='')
    [print(list(i.values())[0], end=' ') for i in result]
    print()
    return result


# find_catalog()

# 5. Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал
# для изменения и удаления данных.

# 5.1 - возможность изменять данные

def change_catalog():
    catalog = export_catalog()
    find = find_catalog()
    print('Если оставить поле пустым, данные будут удалены....')
    for d in find:
        for k, v in input_data.items():
            if list(d.values())[0][k] == v:
                list(d.values())[0][k] = input(f'Введите, новое значение для {v}: ')
    for i in catalog:
        for j in find:
            if i.keys() == j.keys():
                i[list(i.keys())[0]] = list(j.values())[0]
    print(catalog)
    return catalog


# change_catalog()


# 5.2 - удаление данных пользователя

def del_user():
    catalog = export_catalog()
    find = find_catalog()
    [catalog.remove(k) for k in find if k in catalog]
    print(catalog)
    return catalog


# del_user()


# 6 - перезапись текста

def text_overwriting(result):
    with open('catalog.txt', 'w') as catalog:
        for i in result:
            (name, surname, patronymic, telephone) = list(i.values())[0]
            print((name, surname, patronymic, telephone))
            result = (name, surname, patronymic, telephone)
            list(map(lambda x: catalog.write(x + '\n\n' if x == telephone else x + '\n'), result))
        print(result)
        return result


change_catalog1 = change_catalog()
text_overwriting(change_catalog1)
#
# del_user1 = del_user()
# text_overwriting(del_user1)
