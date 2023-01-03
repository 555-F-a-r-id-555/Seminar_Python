import random
number = random.randint(1, 100)
min1 = 1
max1 = 100
print(number)
while True:
     n = input('Введите символ: > или < или =\n')
     if n == '>':
         min1 = number
         number = random.randint(min1,max1)
         print(number)
     elif n == '<':
         max1 = number
         number = random.randint(min1,max1)
         print(number)
     elif n == '=':
         break
     else:
         print(random.randint(min1, max1))
