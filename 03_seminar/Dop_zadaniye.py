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
    print(list3)
    return list3


func_intersection(list1, list2)

# 3 Sample Input:
# ["eat", "tea", "tan", "ate", "nat", “bat"]
# Sample Output:
# [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
# Т.е.сгруппировать слова по "общим буквам".

# работает некорректно

lst1 = ['eat', 'tea', 'tan', 'ate']  # , 'nat', 'bat']

lst3 = []
for i in range(len(lst1)):
    x1 = lst1[i]
    lst2 = []
    for j in range(i, len(lst1)):

        t = True
        for i in x1:
            l = len(lst1[j])
            while l > 0:
                if i in lst1[j]:
                    l -= 1
                else:
                    t = False
                    break
        if t:
            lst2.append(lst1[j])

    lst3.append(lst2)

print(lst3)

# 7 Слияние отрезков:
# Вход: [1, 3] [100, 200] [2, 4]
# Выход: [1, 4] [100, 200]

lst1 = [1, 3]
lst2 = [100, 200]
lst3 = [2, 4]


lst1 = {i for i in range(lst1[0], lst1[1]+1)}
lst2 = {i for i in range(lst2[0], lst2[1]+1)}
lst3 = {i for i in range(lst3[0], lst3[1]+1)}

if lst1 & lst3 != set():
    x1 = lst1.union(lst3)
    print(lst_out1 := [min(x1), max(x1)])
if lst1 & lst2 != set():
    x2 = lst1.union(lst2)
    print(lst_out2 := [min(x2), max(x2)])
if lst2 & lst3 != set():
    x3 = lst2.union(lst3)
    print(lst_out3 := [min(x3), max(x3)])
if lst3 & lst2 == set() and lst1 & lst2 == set():
    print(lst_out4 := [min(lst2), max(lst2)])

