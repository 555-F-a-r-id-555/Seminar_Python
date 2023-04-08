size = int(input())
x = [0] * (size)

for i in range(0, size - 1 + 1, 1):
    x[i] = int(input())
xnew = [0] * (size)

for i in range(size - 1, 0 - 1, -1):
    xnew[size - 1 - i] = x[i]
print(xnew)
