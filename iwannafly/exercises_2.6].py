# Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк.
# После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).

# Программа должна вывести матрицу того же размера,
# у которой каждый элемент в позиции i, j равен
# сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
# У крайних символов соседний элемент находится с противоположной стороны матрицы.

# В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

# Sample Input 1:
#
# 9 5 3
# 0 7 -1
# -5 2 9
# end
# Sample Output 1:
#
# 3 21 22
# 10 6 19
# 20 16 -1
# Sample Input 2:
#
# 1
# end
# Sample Output 2:
#
# 4


matrix = []
while True:
    row = input().split()
    if row == ['end']:
        break
    matrix.append([int(elem) for elem in row])

# print(matrix)

n = len(matrix)
m = len(matrix[0])
result = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        left = matrix[i][j - 1]
        if j == 0:
            left = matrix[i][-1]
        right = matrix[i][(j + 1) % m]
        up = matrix[i - 1][j]
        if i == 0:
            up = matrix[-1][j]
        down = matrix[(i + 1)%n][j]
        result[i][j] = left + right + up + down

# print(result)

for row in result:
    print(' '.join([str(elem) for elem in row]))