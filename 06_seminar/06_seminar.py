# Задача №39. Решение в группах
# Даны  два  массива  чисел.  Требуется  вывести  те  элементы
# первого  массива  (в  том  порядке,  в  каком  они  идут  в  первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число  N  -  количество  элементов  в  первом  массиве,  затем  N
# чисел  -  элементы  массива.  Затем  число  M  -  количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод:
# 3 3 2 12

n1 = [3, 1, 3, 4, 2, 4, 12]
m1 = [4, 15, 43, 1, 15, 1]
i = 0
while i < len(n1):
    if n1[i] in m1:
        del n1[i]
    i += 1
print(n1)

# import random
#
# number_n = int(input("Введите кол-во элементов первого массива: "))
# number_m = int(input("Введите кол-во элементов второго массива: "))
#
# first_list = [random.randint(0, 10) for i in range(number_n)]
# second_list = [random.randint(0, 10) for i in range(number_m)]
# third_list = []
#
# print(first_list, second_list)
#
# for i in range(len(first_list)):
#     if first_list[i] not in second_list:
#         third_list.append(first_list[i])
#
# print(*third_list)
# import random
#
# number_n = int(input("Введите кол-во элементов массива: "))
# some_list = [random.randint(0, 10) for i in range(number_n)]
# count = 0
#
#
# print(some_list)
#
# for i in range(1, len(some_list) - 1):
#     if some_list[i - 1] < some_list[i] and some_list[i + 1] < some_list[i]:
#         count += 1
#
# print(count)


# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:
# 5
# 1 2 3 4 5
# Вывод:
# 0
# Ввод:
# 5
# 1 5 1 5 1
# Вывод:
# 2

x = [1, 5, 1, 5, 1]

count = 0
for i in range(1, len(x) - 1):
    if x[i - 1] < x[i] > x[i + 1]:
        count += 1
print(count)

# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:
# 1 2 3 2 3
# Вывод:
# 2

numbers = [1,2,3,2,3,1,1]



# Задача №45. Решение в группах
# Два  различных  натуральных  числа  n  и  m  называются
# дружественными,  если  сумма  делителей  числа  n
# (включая  1,  но  исключая  само  n)  равна  числу  m  и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает  на  вход  одно  натуральное  число  k,  не
# превосходящее  10^5 .  Программа  должна  вывести    все
# пары  дружественных  чисел,  каждое  из  которых  не
# превосходит  k.  Пары  необходимо  выводить  по  одной  в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена  только  один  раз  (перестановка  чисел  новую
# пару не дает).
# Ввод:
# 300
# Вывод:
# 220 284

n = 10000
def find_friends(n):
    lst = []
    for j in range(1, n):
        if n % j == 0:
            lst.append(j)
    # print(lst, sum(lst))
    return sum(lst)


for friends in range(1, n):
    l = find_friends(friends)
    if friends < l <= n and friends == find_friends(l):
        print(friends, l)



# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
# Теперь он использует их в качестве серверов "Пегого дудочника".
# Помогите владельцу фирмы отыскать все зараженные холодильники.
#
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы
#
# Формат входных данных
# В первой строке подаётся число
# n
# n – количество холодильников. В последующих
# n
# n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от
# 5
# 5 до
# 100
# 100 символов.
#
# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.
#
# Формат входных данных
# В первой строке подаётся число
# n
# n – количество холодильников. В последующих
# n
# n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от
# 5
# 5 до
# 100
# 100 символов.
#
# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.
#
#
# Sample Input 1:
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
# Sample Output 1:
# 1 2 3
# Sample Input 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
# 1 2 7 8
# Подвиг 7. Вводятся номера телефонов в одну строчку через пробел с разными кодами стран: +7, +6, +2, +4 и т.д. Необходимо составить словарь d, где ключи - это коды +7, +6, +2 и т.п., а значения - список номеров (следующих в том же порядке, что и во входной строке) с соответствующими кодами. Полученный словарь вывести командой:
#
# print(*sorted(d.items()))
#
# Sample Input:
# +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
# Sample Output:
# ('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) ('+6', ['+61234576890']) ('+7', ['+71234567890', '+71234567854', '+71232267890'])



def compress_recursive(string):
    if len(string) == 0:
        return []
    elif len(string) == 1:
        return [(string, 1)]
    else:
        compressed = compress_recursive(string[1:])
        if string[0] == compressed[0][0]:
            compressed[0] = (string[0], compressed[0][1] + 1)
        else:
            compressed.insert(0, (string[0], 1))
        return compressed