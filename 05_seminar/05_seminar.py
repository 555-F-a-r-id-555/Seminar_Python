# Задача №31. Решение в группах
# Последовательностью  Фибоначчи  называется
# последовательность чисел a
# 0, a1, ..., an, ..., где
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию
# 1 -вариант
x = []


def fibo(n1):
    if n1 in (0, 1):
        x.append(1)
        return 1
    else:
        r = fibo(n1 - 2) + fibo(n1 - 1)
        x.append(r)
        return r


n = int(input('Введите число Фибоначи, а то будет иначе: '))
print(fibo(n))
print(*x[-(n + 1):])


# 2 -вариант
def fibo(n):
    if n in (0, 1):
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(7))

for i in range(7 + 1):
    print(fibo(i), end=' ')
print()


# Задача №33. Общее обсуждение
# Хакер Василий получил доступ к классному журналу и
# хочет  заменить  все  свои  минимальные  оценки  на
# максимальные.  Напишите  программу,  которая
# заменяет  оценки  Василия,  но  наоборот:  все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


def lst_print(n, lst, k=0):
    if k == 0:
        print(1 if lst[0] > 3 else lst[0], end=' ')
    if k == n - 1:
        # print(1 if lst[n - 1] >= 3 else lst[n - 1], end=' ')
        return lst[n - 1]
    else:
        print(1 if lst[k + 1] > 3 else lst[k + 1], end=' ')
        return lst_print(n, lst, k + 1)


lst_print(5, [1, 3, 4, 3, 4])
print()


# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def prime_number(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return 'yes' if d * d > n else 'no'


print(prime_number(5))
print(prime_number(55))


# № 37 - Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input:    2 -> 3 4
# Output: 4 3

def reverse(n, list1):
    if n <= 0:
        #print(list1[0], end=' ')
        return list1[0]
    else:
        print(list1[n-1], end=' ')
        return reverse(n - 1, list1)


reverse(6, [11, 21, 31, 41, 51, 61])

print('\n')


def lst_print(n, lst, k=0):
    if k >= n - 1:
        print(lst[n - 1], end=' ')
        return lst[n - 1]
    else:
        print(lst[k], end=' ')
        return lst_print(n, lst, k + 1)


lst_print(6, [33, 44, 55, 66, 77, 88])
