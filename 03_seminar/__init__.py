# 11- Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# num = int(input())
# a, b = 0, 1
# count = 1
# while a <= num:
#     if a == num:
#         print(count, end=" ")
#         break
#     a, b = b, a + b
#     count += 1
# else:
#     print(f'число {num} -1 => не число Фибоначи')


# eagle_tails = list(map(int, input('Вводите 0 или 1 через пробел: ').split()))
# eagle = eagle_tails.count(1)
# tails = eagle_tails.count(0)
# print(eagle if eagle < tails else tails)

# Выведите таблицу размером
# n×n, заполненную числами от
# 1 до n^2 по спирали, выходящей из левого верхнего угла
#и закрученной по часовой стрелке,
# как показано в примере (здесь n=5):

size = int(input('Введите размер массива: '))

matrix = [[0] * size for _ in range(size)]
matrix[0] = [(col + 1) for col in range(size)]

index = size
y = 0
x = size - 1
r = size
while index < size * size:
    r -= 1
    for _ in range(r):  # вертикаль
        y += 1
        index += 1
        matrix[y][x] = index
    for _ in range(r):  # горизонталь
        x -= 1
        index += 1
        matrix[y][x] = index
    if index >= size * size:
        break
    else:
        r -= 1
        for _ in range(r):  # вертикаль
            y -= 1
            index += 1
            matrix[y][x] = index
        for _ in range(r):  # горизонталь
            x += 1
            index += 1
            matrix[y][x] = index

        if index >= size * size:
            break
        else:
            r -= 1
            for _ in range(r):
                y += 1
                index += 1
                matrix[y][x] = index
            for _ in range(r):
                x -= 1
                index += 1
                matrix[y][x] = index
            if index >= size * size:
                break
            else:
                r -= 1
                for _ in range(r):
                    y -= 1
                    index += 1
                    matrix[y][x] = index
                for _ in range(r):
                    x += 1
                    index += 1
                    matrix[y][x] = index
                if index >= size * size:
                    break
for i in matrix:
    print(*i)




































