# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

# 1 - Вариант

n = int(input('количество монет: '))
orel, orel_count = 1, 0
rewka, rewka_count = 0, 0
for _ in range(n):
    x = int(input("Значение монеты: "))
    if orel == x:
        orel_count += 1
    else:
        rewka_count += 1
if orel_count < rewka_count and orel_count != 0:
    print(orel_count)
elif orel_count == 0:
    print(rewka_count)
elif rewka_count < orel_count and rewka_count != 0:
    print(rewka_count)
else:
    print(orel_count)


# 2 -Вариант

def coints_rotate(n, s_t_r='Задача 10'):
    print(s_t_r)
    # n = int(input('Количество монеток: '))
    eagle, count_eagle = 1, 0
    tails, count_tails = 0, 0
    amount = []
    for i in range(0, n):
        amount.append(int(input('Введите ли 0 либо 1: ')))
    for i in amount:
        if i == eagle:
            count_eagle += 1
        else:
            count_tails += 1
    print((count_eagle if count_eagle != 0 else count_tails) if count_eagle < count_tails else (
        count_tails if count_tails != 0 else count_eagle))


# coints_rotate(5)


# 3-Вариант

def func_eagle_tails(s_t_r='Задача 10 вариант №2 '):
    print(s_t_r)
    # n = int(input('Количество монеток, хотя это неважно: '))
    eagle_tails = list(map(int, input('Вводите 0 или 1 через пробел: ').split()))
    eagle = eagle_tails.count(1)
    tails = eagle_tails.count(0)
    print(eagle if eagle < tails else tails)


# func_eagle_tails()


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

# 1 -Вариант
def find_number(s_u_m, mult, s_t_r='Задача 12'):
    print(s_t_r)
    # s_u_m = int(input('Сумма чисел: '))
    # mult = int(input('Произведение чисел: '))
    b_o_o_l = None
    for i in range(0, 1001):
        if b_o_o_l:
            break
        for j in range(0, 1001):
            if i + j == s_u_m and i * j == mult:
                b_o_o_l = True
                print(i, j)
                break
    else:
        print(f'Решения нет')


find_number(4, 4)
find_number(5, 6)
find_number(19, 90)
find_number(2, 3)


# 2 -вариант


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2 k ), не превосходящие числа N.
# 10 -> 1 2 4 8


def print_2_k(s_t_r='Задача 14'):
    print(s_t_r)
    n = int(input('Введите положительное число большее 0: '))
    num = 1
    for i in range(0, n):
        if num <= n:
            print(num, end=" ")
            num *= 2

# print_2_k()
