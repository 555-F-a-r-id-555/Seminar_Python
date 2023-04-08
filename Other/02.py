size = int(input())
x = [0] * (size)

i = 0
while i < size:
    x[i] = int(input())
    i = i + 1
max1 = x[0]
j = 0
n = 0
while j < size:
    if x[j] > max1:
        max1 = x[j]
        n = j
    j = j + 1
print(max1)
print(n)
x[n] = x[-1]
x[-1] = max1
print(x)
