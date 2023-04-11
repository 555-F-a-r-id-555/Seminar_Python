# 9- По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input:       5
# Output:    120

import keyword

print('factorial IS in kwlist' if 'factorial' in keyword.kwlist else 'factorial is NOT in kwlist')


# 1 Вариант
# n = int(input('Введите число: '))
# factorial = 1
# while n > 0:
#     factorial *= n
#     n -= 1
# print('Output: ', factorial)


# 2 Вариант

# def factorial(n):
#     if n > 0:
#         return n * factorial(n - 1)
#     else:
#         return 1
#
#
# print("факториал число {0}! = {1}".format(5, factorial(5)))

# 3 Вариант

# import math
#
# print(math.factorial(int(input('Введите число: '))))

# 11- Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# 1 -Вариант

def fibo1(a, s_t_r="Задача 11, 1-Вариант"):
    print(s_t_r)
    # a = int(input('Введите число: '))
    a1 = 0
    a2 = 1
    a3 = a2 + a1
    temp = a1
    n = 2
    while a3 < a:
        temp1 = a3
        a3 += temp
        temp = temp1
        n += 1

    match a:
        case 0:
            print('Output: ', 1, "- элемент ряда Фибоначи.", a, "- число Фибоначи")
        case 1:
            print('Output: ', "либо 2 либо 3", "- элемент ряда Фибоначи.", a, "- число Фибоначи")
        case _ if a3 == a:
            print('Output: ', n, "- элемент ряда Фибоначи.", a, "- число Фибоначи")
        case _ if a3 != a:
            print('Output: ', -1, a, "- не является число Фибоначи")


# fibo1(0)
# fibo1(1)
# fibo1(5)
# fibo1(13)
# fibo1(6)


# if a3 == a:
#     print('Output: ', n, "- элемент ряда Фибоначи.", a3, "- число Фибоначи")
# else:
#     print('Output: ', -1, a3, "- не является числом Фибоначи")

# 2-Вариант

def fibo2(a, s_t_r="Задача 11, 2-Вариант"):
    print(s_t_r)
    # a = int(input('Введите число Фибоначчи: '))
    x = [0, 1]
    i = 1
    temp = x[1]
    while temp < a:
        temp = x[i] + x[i - 1]
        x.append(temp)
        i += 1
    if a in x:
        print('Output: ', x.index(a) + 1)
    else:
        print('Output:', -1)


# fibo2(0)
# fibo2(1)
# fibo2(5)
# fibo2(13)
# fibo2(6)

# 3 -Вариант


# a = int(input('Введите число: '))


def fibo3(a, s_t_r="Задача 11, 3-Вариант"):
    def fibo(n):
        if n <= 1:
            return n
        else:
            return fibo(n - 1) + fibo(n - 2)

    temp, n2 = 0, 0
    while temp < a:
        temp = fibo(n2)
        n2 += 1

    print(f'Output: {n2}' if temp == a else f'Output: -1')


# fibo3(0)
# fibo3(1)
# fibo3(5)
# fibo3(13)
# fibo3(6)

# 13 -Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# 1 -Вариант
# N = int(input('Введите количество дней: '))
# count = 0
# max_count = 0
# temp = []
# for i in range(0, N):
#     temp.append(int(input(f'среднесуточная температура {i + 1} дня: ')))
#     if temp[i] > 0:
#         count += 1
#         if count > max_count:
#             max_count = count
#     else:
#         count = 0
# print('Output: ', count)

# 2-Вариант

day_count = int(input('Количество дней: '))
temp_count = 0
max_count = 0
for i_day in range(day_count):
    day_temp = int(input('Средняя темп. за день: '))
    if day_temp > 0:
        temp_count += 1
        if temp_count > max_count:
            max_count = temp_count
    else:
        temp_count = 0

print('Output: ', max_count)

# 15- Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

n = int(input('Арбузы: '))
max_arbuz = n
min_arbuz = n
for i in range(n):
    x = int(input(f'{i + 1} арбуз: '))
    if x > max_arbuz:
        max_arbuz = x
    if x < min_arbuz:
        min_arbuz = x
print('Output: ', min_arbuz, max_arbuz)

# 2 -Вариант
# N = int(input('Введите количество арбузов: '))
# watermelon = []
# for i in range(0, N):
#     watermelon.append(int(input(f'Вес {i + 1} арбуза: ')))
# m_i_n = watermelon[0]
# m_a_x = watermelon[0]
# for i in range(0, N):
#     if watermelon[i] < m_i_n:
#         m_i_n = watermelon[i]
#     if watermelon[i] > m_a_x:
#         m_a_x = watermelon[i]
# print('Output: ', m_i_n, m_a_x)

# 3 -Вариант

# N = int(input("Количество арбузов: "))
# water_melon = list(map(int, input('Вводите Вес N арбузов в строку через пробел: ').split()))
# print('Output: ', min(water_melon), max(water_melon))

# print(list(map(int, '1 2 3 4 5'.split())))
# print('1 2 3 4 5'.split())

# Вводится 2 числа a и b. Найти все простые числа в дипапзоне от a до b

a = int(input('Первое число: '))
b = int(input('Второе чсло: '))
for elem1 in range(a, b + 1):
    for elem2 in range(2, elem1):
        if elem1 % elem2 == 0:
            break
    else:
        print(elem1, end=' ')
