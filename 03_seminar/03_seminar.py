# 17 Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# 1 вариант
# num = [1, -1, 2, 0, 1, 3, 4, 4]
# # num = list(map(int, input().split()))
# num = set(num)
# print(num, len(num))

# 2 вариант
# unique_element_count = 0
# for unique_element in num:
#     for unique_element2 in num:
#         if unique_element == unique_element2:
#             unique_element_count += 1
# print(f'Количество уникальных элементов = {unique_element_count}')

# 19 Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо,  K –
# положительное число.
# Input:   [1, 2, 3, 4, 5] k = 3
# Output:  [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# 1
num = [1, 2, 3, 4, 5]
k = 2
n = len(num)
for i in range(n // 2):
    temp = num[i]
    num[i] = num[n - i - 1]
    num[n - i - 1] = temp

for i in range(k // 2):
    temp = num[i]
    num[i] = num[k - i - 1]
    num[k - i - 1] = temp
print(num)
for i in range(k, k + (n - k) // 2):
    # print(num[i], end=" ")
    temp = num[i]
    num[i] = num[n + k - i - 1]
    num[n + k - i - 1] = temp
print()
print(num)

# 2

array1 = [1, 2, 3, 4, 5]
k = 3
for i in range(k):
    for j in range(len(array1)):
        # temp = array1[j]
        # array1[j] = array1[-1]
        # array1[-1] = temp
        array1[j], array1[-1] = array1[-1], array1[j]

print(array1)

# 3

array1 = [1, 2, 3, 4, 5]
k = 2
part1 = array1[-k:]
# print(part1)
part2 = array1[:-k]
# print(part2)
array1_2 = part1 + part2
print(array1_2)

# 4

# def shift(lst, steps):
#     if steps < 0:
#         steps = abs(steps)
#         for i in range(steps):
#             lst.append(lst.pop(0))
#     else:
#         for i in range(steps):
#             lst.insert(0, lst.pop())
#
#
# shift(num, k)
# print(num)


# 21 - Напишите программу для печати всех уникальных
# значений в словаре.
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит


dict_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
          {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "},
          {" VIII": " S007 "}]

x = set()
for i in dict_1:
    # print(list(i.values())[0].strip())
    x.add(list(i.values())[0].strip())
print(x)



# 23 Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.


list_1 = [0, -1, 5, 2, 3, 1, 2, 0]
count = 0
elem_n = list_1[0]
x = []
for elem in list_1:
    if elem > elem_n:
        count += 1
        x.append(f'{elem_n} < {elem}')
    elem_n = elem

print(count, tuple(x))
