# определить простое число или нет рекурсией

# def prime_number(n):
#     d = 2
#     while d * d <= n and n % d != 0:
#         d += 1
#     return 'yes' if d * d > n else 'no'


def prime(n, d=2):
    if d * d >= n:
        # print('prime number')
        return True
    elif n == 2:
        return True
    elif n % d == 0:
        # print('not prime')
        return False
    else:
        # print('prime')
        return prime(n, d + 1)


print(prime(57))


# 2 - Версия

def is_prime(num, i=2):
    if num < 2:
        return False
    elif i == num:
        return True
    elif num % i == 0:
        return False
    else:
        return is_prime(num, i + 1)


print(is_prime(17))  # Output: True


# эта функция не самая оптимальная
# с точки зрения производительности, и для больших чисел возможно,
# что программа будет выполняться слишком долго.

# палиндром или нет рекурсией

# def reverse(n, list1):
#     if n <= 0:
#         #print(list1[0], end=' ')
#         return list1[0]
#     else:
#         print(list1[n-1], end=' ')
#         return reverse(n - 1, list1)
#
#
# n =[11, 21, 31, 21, 11]
# reverse(5, n)
#
# def pol(revers,n,k =0):


# def lst_print(n, lst, k=0):
#     if k >= n - 1:
#         print(lst[n - 1], end=' ')
#         return lst[n - 1]
#     else:
#         print(lst[k], end=' ')
#         return lst_print(n, lst, k + 1)
#
# lst_print(6, [33, 44, 55, 66, 77, 88])


def palindrome(str):
    if len(str) < 1:
        return True
    else:
        if str[0] == str[-1]:
            return palindrome(str[1:-1])
        else:
            return False


some_str = "абба"

if palindrome(some_str):
    print("Данная строка палиндром!")
else:
    print("Данная строка не палиндром!")
