# Сложные задачи
#
# 1. Создайте список из случайных чисел.
# Найдите номер его последнего локального максимума
# (локальный максимум — это элемент, который больше любого из своих соседей).

import random

# list1 = [random.randint(0, 10) for _ in range(0, 10)]
# print(list1)
#
# for i in range(len(list1) -2, -1, -1):
#     print(list1[i], end=' ')
#     print()
#     if list1[i - 1] < list1[i] > list1[i + 1]:
#         print(f'{i} - номер, {list1[i]} - элемента')
#         break

# 2. Создайте список из случайных чисел.
# Найдите максимальное количество его одинаковых элементов.

# 1
list2 = [random.randint(0, 10) for _ in range(0, 10)]
# list2 = [1, 2, 3, 4, 5, 5, 5, 4]
print(list2)
# l = set()
# for i in range(len(list2)):
#     if list2[i] in list2[i + 1:]:
#         # print(list2[i+1:])
#         l.add(list2[i])
#
# print(len(l))

# 2

lts1 = []
for i in range(len(list2)):
    if list2[i] in list2[i + 1:]:
        lts1.append(list2[i])

print(lts1)
set(list2)
identical_elements = len(list2) - (len(set(list2)) - len(set(lts1)))
print(identical_elements)
# 3. Создайте список из случайных чисел.
# Найдите второй максимум.
# a = [1, 2, 3] # Первый максимум == 3, второй == 2

# list3 = [random.randint(0, 10) for _ in range(0, 10)]
# # list2 = [1, 2, 3, 4, 5, 5, 5, 4]
# list3.sort()
# print(list3)
# for i in range(len(list3) - 2, -1, -1):
#     if list3[i] != list3[i + 1]:
#         print(list3[i])
#         break

# 4. Создайте список из случайных чисел.
# Найдите количество различных элементов в нем.

# list2 = [random.randint(0, 10) for _ in range(0, 10)]
#
# print(list2)
# l2 = set()
# for i in range(len(list2)):
#     if list2[i] in list2[i + 1:]:
#         l2.add(list2[i])
# print('общее количество элементов', set(list2))
# print('совподающие элементы: ', set(l2))
# print('количество не совподающих элементов: ', len(set(list2)) - len(l2))
