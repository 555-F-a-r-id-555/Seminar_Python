# with open('example.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     for letter in text:
#         print(letter)


# with open('example.txt', 'r', encoding='utf-8') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line[:-1])

# with open('example.txt', 'r', encoding='utf-8') as file:
#     line = file.readline()
#     while line:
#         print(line[:-1])
#         line = file.readline()


# with open('example.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     print(text.splitlines())

# with open('example.txt', 'r', encoding='utf-8') as file:
#     text = file.readlines()
#     print(text)



with open('example.txt', 'w', encoding='utf-8') as file:
    some_list = ['hello', 'world', 'how', 'are', 'you']
    for el in some_list:
        file.write(el + '\n')


with open("article.txt", 'r', encoding = 'utf-8') as text:
  value = list(text.read().split())
  max = 0
  long_word = list()
  for i in value:
    if len(i)>max:
      long_word = list()
      max = len(i)
      long_word.append(i)
    if len(i)==max:
      long_word.append(i)
  print(f"max = {max}, {long_word}")


  # 1 ������������ ������ ���-�� �����, ����� ���� ������. ����� ��������
  # � ����� ��������� ���� ��� ��� ������
  #
  # line = int(input('enter lines quantity: '))
  # text = []
  # for i in range(line):
  #     text.append(input("enter line: "))
  #
  # with open('text.txt', 'w', encoding='utf-8') as file:
  #     for el in text:
  #         file.write(el + '\n')
  #
  # temp_symbol = input("please enter your symbol: ")
  #
  # with open('text.txt', 'r', encoding='utf-8') as file:
  #     text = file.read()
  #     print(text.count(temp_symbol))

  # 2 ����� ������������ ������ ������, ����� ����� ���-�� ����� ������� � ����� �����.

  # # �������� ������� read_last(lines, file), ������� ����� ��������� ������������
  # ���� file �
  # # �������� �� ������ ��������� ��������� ������ � ���������� lines
  # # (�� ������ ������ ��������, ��� ������ ������������� ����� �����).
  # # ������������ ������� �� ����� �article.txt� �� ��������� ����������:
  # #
  # # ��������
  # # ������� ����
  # # ������ �������
  # # ������ ���� � �������
  # # ������ �������� �� ����
  # # ������� ������
  # # ���� ���������
  # # ������ ��������
  #
  # def read_last(lines, file):
  #     with open(file, 'r', encoding='utf-8') as f:
  #         l = f.read().splitlines()
  #         for i in range(len(l) - lines, len(l)):
  #             print(l[i])
  #
  #
  # read_last(3, 'article.txt')

  #
  # #3 �������� �article.txt� �������� ��������� �����:

  # # ��������
  # # ������� ����
  # # ������ �������
  # # ������ ���� � �������
  # # ������ �������� �� ����
  # # ������� ������
  # # ���� ���������
  # # ������ ��������
  # #
  # # ��������� ����������� ������� longest_words(file), ������� ������� �����,
  # # ������� ������������ ����� (��� ������ ����, ���� ������� ���������).

  def longest_words(file):
      with open(file, 'r', encoding='utf-8') as f:
          text = f.read().lower().split()
          print(text)
          max = 0

          for i in range(len(text)):
              if len(text[i]) > max:
                  max = i
          newlist = []

          for y in range(len(text)):
              if len(text[y]) == len(text[max]):
                  newlist.append(text[y])
          print(newlist)


  longest_words('article.txt')


  #1 ������������ ������ ���-�� �����, ����� ���� ������.
  # ����� �������� � ����� ��������� ���� ��� ��� ������
  # ����� ������������ ������ ������,
  # ����� ����� ���-�� ����� ������� � ����� �����.

  # with open('test.txt', 'w') as test:
  #     n = int(input())
  #     for i in range(n):
  #         test.write(input() + '\n')
  #
  # simbol = input()
  # with open('test.txt', 'r') as test1:
  #     data = test1.readline()
  #     # print(data)
  #     sum = 0
  #     while data:
  #         # print(data)
  #         sum += data.count(simbol)
  #         data = test1.readline()
  # print(sum)

  # print('sdddfdd'.count('s'))

  # lst = []
  # for i in range(n):
  #     a = input()
  #     lst.append(a)
  # for i in lst:
  #     test.write(str(i) +'\n')
  # print(lst)

  # with open('task_1.txt', 'r', encoding='utf-8') as file:
  #     while True:
  #         line = file.readline()
  #         if not line:
  #             break
  #         print(line[:-1])

  #2  �������� ������� read_last(lines, file),
  # ������� ����� ��������� ������������ ���� file �
  # �������� �� ������ ��������� ��������� ������ � ���������� lines
  # (�� ������ ������ ��������, ��� ������ ������������� ����� �����).
  # ������������ ������� �� ����� �article.txt� �� ��������� ����������:
  #
  # ��������
  # ������� ����
  # ������ �������
  # ������ ���� � �������
  # ������ �������� �� ����
  # ������� ������
  # ���� ���������
  # ������ ��������

  # def read_last(lines, file):
  #     with open(file, 'r') as article:
  #         line = article.readline()
  #         while line:
  #             temp = line
  #             line = article.readline()
  #
  #         print((temp + '\n')*lines)
  #
  #
  # read_last(lines=5, file='article.txt')

  #3 �������� �article.txt� �������� ��������� �����:
  #
  # ��������
  # ������� ����
  # ������ �������
  # ������ ���� � �������
  # ������ �������� �� ����
  # ������� ������
  # ���� ���������
  # ������ ��������
  #
  # ��������� ����������� ������� longest_words(file), ������� ������� �����,
  # ������� ������������ ����� (��� ������ ����, ���� ������� ���������).

  def read_last(file):
      with open(file, 'r') as article:
          line = article.readline()
          while line:
              temp = len(line)
              line = article.readline()

              if temp < len(line):
                  temp = len(line)

              print(line)
              print(temp)


  read_last(file='article.txt')