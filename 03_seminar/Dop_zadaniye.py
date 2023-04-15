# 1 Напишите функцию, которая
# переворачивает строку.

# 1 -Вариант
def func():
    n = input('Введите строку: ')
    new_n = ''
    for i in range(len(n) - 1, -1, -1):
        new_n += n[i]
    return new_n


print(func())


# 2- Вариант

def func2():
    n = list(input('Введите строку: '))
    for i in range(0, len(n) // 2):
        n[i], n[len(n) - i - 1] = n[len(n) - i - 1], n[i]
    return ''.join(n)


print(func2())

# 2 Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3] (порядок неважен)

list1 = [1, 2, 3, 2, 0]
list2 = [5, 1, 2, 7, 3, 2]


def func_intersection(l1, l2):
    list3 = []
    for elem1 in l1:
        if elem1 in l2:
            list3.append(elem1)
    return list3


print(func_intersection(list1, list2))



# 3 Sample Input:
# ["eat", "tea", "tan", "ate", "nat", “bat"]
# Sample Output:
# [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
# Т.е.сгруппировать слова по "общим буквам".


# 7 Слияние отрезков:
# Вход: [1, 3] [100, 200] [2, 4]
# Выход: [1, 4] [100, 200]
