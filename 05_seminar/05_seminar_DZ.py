# № 6 Доп. задание:
# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE,
# которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла
# невалидная строка.
# Пояснения: Если символ встречается 1 раз,
# он остается без изменений; Если символ
# повторяется более 1 раза, к нему
# добавляется количество повторений.

def rle(input_string):
    import re
    if not re.match(r'^[A-Z]+$', input_string):
        raise Exception('Невалидная строка')
    k = 1
    res = []
    for i in range(len(input_string) - 1):
        if input_string[i] == input_string[i + 1]:
            k += 1
        else:
            res.append(f'{input_string[i]}{k}' if k > 1 else f'{input_string[i]}')
            k = 1
    if input_string[-1] == input_string[-2]:
        res.append(f'{input_string[i]}{k}' if k > 1 else f'{input_string[i]}')
    else:
        res.append(f'{input_string[i + 1]}')
    print(''.join(res))
    return ''.join(res)


rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB')
rle('FAAAABBBCCXYZDDDDEEEFFFAAAAAABBBAAAAAAAAAAAAAAAAAAAF')


# rle('FAAAABBBCCXYZDDDDEEEFFFAAAAAABBBAAAAAAAAAAAAAAAAAAAF8')

# Задача 26:  Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
# 1 вариант
def pow1(a, b, temp=1):
    if b <= 0:
        return 1
    elif b == 1:
        return a
    else:
        return pow1((a * a) // temp, b - 1, temp=a)


print(pow1(2, 9))
print(pow1(3, 5))


# 2 вариант

def pow2(a, b):
    if b <= 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * pow2(a, b - 1)


print(pow2(2, 9))
print(pow2(3, 5))


# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

def sum1(a, b):
    if b <= 0:
        return a
    else:
        return sum1(a + 1, b - 1)


print(sum1(10, 0))
print(sum1(0, 10))
print(sum1(4, 8))
print(sum1(10, 5))


# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.
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