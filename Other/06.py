size = int(input())
x = [0] * (size)

i = 0
while i < size:
    x[i] = int(input())
    if i < 1:
        max1 = x[0]
        min1 = x[0]
        iMax = 0
        iMin = 0
    else:
        if x[i] > max1:
            max1 = x[i]
            iMax = i
        else:
            if x[i] < min1:
                min1 = x[i]
                iMin = i
    i = i + 1
sum = 0
if iMax > iMin:
    for i in range(iMin + 1, iMax - 1 + 1, 1):
        sum = sum + x[i]
else:
    for i in range(iMax + 1, iMin - 1 + 1, 1):
        sum = sum + x[i]
print(sum)
