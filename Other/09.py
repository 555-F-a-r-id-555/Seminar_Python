# Определение количества максимальных чисел;
numbers = [1, 8, 3, 8, 2, 6, 8, 8]
index = 0
count_maximal = 0
maximum = numbers[index]
while index < len(numbers):
    if numbers[index] > maximum:
        maximum = numbers[index]
        count_maximal = 1
    elif numbers[index] == maximum:
        count_maximal = count_maximal + 1
    index = index + 1
print(f'count_maximal = {count_maximal}')