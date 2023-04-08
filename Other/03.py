size = int(input())
x = [0] * (size)

for i in range(0, size - 1 + 1, 1):
    x[i] = int(input())

print(x)

x_new =[0]* (size)
for i in range(size-1, -1, -1):
    x_new[(size-1)-i] = x[i]

print(x_new)



