# Задача №25. Решение в группах
# Напишите  программу,  которая  принимает  на  вход
# строку,  и  отслеживает,  сколько  раз  каждый  символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для  решения  данной  задачи  используйте  функцию .split()

# str1 = input().split()
import time

str1 = ['a', 'a', 'a', 'b', 'c', 'a', 'a', 'd', 'c', 'd', 'd']

star_time = time.perf_counter()
for i in range(len(str1)):
    k = 0
    for j in range(i + 1, len(str1)):
        if str1[i] == str1[j]:
            k += 1
            # str1[j] += f'_{k}'
            str1[j] += "_%(position)s" % {'position': k}
end_time = time.perf_counter()
print(' '.join(str1))

print(f'end_time - start_time = {end_time - star_time}')


# 2
str1 = ['a', 'a', 'a', 'b', 'c', 'a', 'a', 'd', 'c', 'd', 'd']
str2 = {}
output = []
k = 0
for x in str1:
    if x in str2:
        k += 1
        str2[x] = x + f'_{k}'
        output.append(str2[x])
    else:
        str2[x] = x
        output.append(str2[x])
print(*output)

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов.  Определите,  сколько  различных  слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
# Input: She sells sea shells on the sea shore;The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore,I'm sure that the shells are sea
# shore shells.
# Output: 19

# str2 = '''She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells'''
# str2 = 'a a a b c a a d c d d'
str2 = '''She sells sea shells on the sea shore; The shells 
that she sells are sea shells I'm sure. So if she sells sea 
shells on the sea shore, I'm sure that the shells are sea 
shore shells.'''

# 1
n = str2.lower().split()
print(n)
sum_count = len(n)
count = 0
for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[i] == n[j]:
            count += 1
            n[j] += f'{count}'
print(n)
print(len(n) - count)

# 2

words = set(str2.split())
print(words)
print(len(words))

# 3
import re

a = '''She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.'''

print(len({x for x in re.findall(r'\w', a)}))



# 4

import sys

f = open('01.txt')
# for line in f.read():
#     print(line, end=' ')
print(len(set(f.read().split())))
f.close()
# ---------------------------------
# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2  друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих
# слайдах

# Ваня:
# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#    n = int(input())
#    if max_number < n:
#        n = max_number
# print(n)

max1 = 0
while n != 0:
    n = int(input())
    if n > max1:
        max1 = n
print(max1)
