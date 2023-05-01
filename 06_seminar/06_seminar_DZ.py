# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def arithmetic_progression(a1=7, d=2, n=5):
    # a1 = int(input())
    # d = int(input())
    # n = int(input())
    print(*list(range(a1, (a1 + (n - 1) * d) + 1, d)))


arithmetic_progression()


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод:  [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

def find_index(m_i_n=5, m_a_x=15):
    lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
    # print(len(lst), min(lst), max(lst))
    # m_i_n = int(input())
    # m_a_x = int(input())
    res = [i for i in range(len(lst)) if m_i_n <= lst[i] <= m_a_x]
    print(*res)


find_index()


# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
# Теперь он использует их в качестве серверов "Пегого дудочника".
# Помогите владельцу фирмы отыскать все зараженные холодильники.
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
# и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы,
# главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника,
# нумерация начинается с единицы
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
# Программа должна вывести номера зараженных холодильников через пробел.
# Если таких холодильников нет, ничего выводить не нужно.
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
# Программа должна вывести номера зараженных холодильников через пробел.
# Если таких холодильников нет, ничего выводить не нужно.
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
#
def Anton(n, lst=[]):
    # n = int(input('Число холодильников: '))
    # lst = []
    answer = []
    for i in range(n):
        # lst.append(input().lower())
        for j in 'anton':
            if j not in lst[i]:
                break
            elif lst[i].count('n') < 2:
                break
        else:
            answer.append(i + 1)
    print('Вот такие вот, номера холодильников: ', *answer)


lst = ['222anton456',
       'a1n1t1o1n1',
       '0000a0000n00t00000o000000n',
       'gylfole',
       'richard',
       'ant0n']
Anton(6, lst)

lst = ['osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen',
       'anton',
       'aoooooooooontooooo',
       'elelelelelelelelelel',
       'ntoneeee',
       'tonee',
       '253235235a5323352n25235352t253523523235oo235523523523n',
       'antoooooooooooooooooooooooooooooooooooooooooooooooooooon',
       'unton']
Anton(9, lst)


# рекурсия


# -Поиск наибольшего общего делителя.
# Напишите функцию, которая находит наибольший общий делитель
# двух чисел с помощью рекурсии.

# 1 -Вариант
def NOD(n1, n2, temp=200):
    if n1 % temp == 0 and n2 % temp == 0:
        return temp
    else:
        return NOD(n1, n2, temp - 1)


print(NOD(4, 16))
print(NOD(28, 64))
print(NOD(84, 90))


# 2 -Вариант

def n_o_d(n1, n2):
    if n2 == 0:
        return n1
    else:
        return n_o_d(n2, n1 % n2)


print(n_o_d(84, 90))
print(n_o_d(64, 28))

# 3 -Вариант

temp = n1 if (n2 := int(input('Введите первое число: '))) > (n1 := int(input('Введите второе число: '))) else n2


def nod(n1, n2, temp):
    if n1 % temp == 0 and n2 % temp == 0:
        return temp
    else:
        return NOD(n1, n2, temp - 1)


print('NOD = ', nod(n1, n2, temp))


# Разбиение числа на сумму слагаемых.
# Напишите функцию, которая разбивает заданное число на сумму слагаемых
# с помощью рекурсии. Например,
# число 4 можно разбить на сумму слагаемых 1+1+1+1, 1+1+2, 2+2 и 4.

# 1 - Вариант
def sum_num(n, temp=[]):
    if n == 0:
        print(*temp)
    else:
        for i in range(1, n + 1):
            if not temp:
                sum_num(n - i, temp + [i])
            elif temp[-1] <= i:
                sum_num(n - i, temp + [i])


sum_num(4)


# 2 - Вариант
def split_sum(n, current_sum=[], start=1):
    if n == 0:
        print('+'.join(map(str, current_sum)))

    else:
        for i in range(start, n + 1):
            split_sum(n - i, current_sum + [i], i)


split_sum(5)
