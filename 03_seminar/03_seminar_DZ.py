# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# 5
# 1 2 3 4 5 3 -> 1

# 1 - Вариант
import random

n = int(input("Введите n = "))
x = int(input("Введите x = "))
array = []
for i in range(n):
    array.append(random.randint(1, 10))
print(*array, f'-> {array.count(x)}')

# 2 -Вариант

count = 0
for elem in array:
    if x == elem:
        count += 1
print(*array, f'-> {count}')

# 3 - Вариант
print(*(array1 := [(random.randint(1, 10)) for i in range(n)]), f'-> {array1.count(x)}')

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

# 1- Вариант
# import random

n1 = int(input("Введите n1 = "))
x1 = int(input("Введите x1 = "))

array3 = [random.randint(-10, 10) for i in range(n1)]
print(array3)
diff_min2 = abs(x1 - array3[0])
elem_min2 = array3[0]
for elem3 in array3[1:]:
    diff2 = abs(x1 - elem3)
    if diff2 < diff_min2:
        diff_min2 = diff2
        elem_min2 = elem3
print(*array3, f'-> {elem_min2}')

# 2 -Вариант

# array3 = [161, 190, 151]
# array3 = [145, 5, 7, 148]
array3 = [145, 5, 7, 148, 161, 190, 153]
x1 = 150
diff_min1 = abs(x1 - array3[0])
for elem3 in array3:
    if elem3 < x1:
        diff1 = abs(x1 - elem3)
        if diff1 < diff_min1:
            diff_min1 = diff1
            closestLeft = elem3
for elem4 in array3:
    if elem4 != elem3 and elem4 > x1:
        diff_min2 = abs(x1 - elem4)
for elem5 in array3:
    if elem5 > x1:
        diff1 = abs(x1 - elem5)
        if diff1 < diff_min2:
            diff_min2 = diff1
            closestRight = elem4

try:
    print(f'{closestLeft} ', end='')
except NameError:
    print('closestLeft - не существует ', end='')
try:
    print(f'< {x1} < {closestRight} ')
except NameError:
    print(f'< {x1} < closestRight - не существует')

# 3

n = int(input('Введите длину массива: '))
x = int(input('введите искомое значение: '))
array3 = [random.randint(-10, 10) for i in range(n)]
print(array3)
array3.append(x)
array3.sort()
print(f'{array3[array3.index(x) - 1]} < {array3[array3.index(x)]} < {array3[array3.index(x) + 1]}')

# Задача 20:  В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите  программу,  которая  вычисляет  стоимость  введенного  пользователем  слова.
# Будем  считать,  что  на  вход  подается  только  одно  слово,  которое  содержит  либо  только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12

dictionary = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
              'D': 2, 'G': 2,
              'B': 3, 'C': 3, 'M': 3, 'P': 3,
              'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
              'K': 5,
              'J': 8, 'X': 8,
              'Q': 10, 'Z': 10,
              'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
              'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
              'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
              'Й': 4, 'Ы': 4,
              'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
              'Ш': 8, 'Э': 8, 'Ю': 8,
              'Ф': 10, 'Щ': 10, 'Ъ': 10,
              }

string = ''.join(input('Введите любую строку: ').upper().strip().split())
print(string)
score = 0
for elem in string:
    for key in dictionary.keys():
        if elem == key:
            score += dictionary[key]
print(score)
