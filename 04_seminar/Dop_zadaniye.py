# 3 Sample Input:
# ["eat", "tea", "tan", "ate", "nat", "bat"]
# Sample Output:
# [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
# Т.е.сгруппировать слова по "общим буквам".


# y = []
# temp = []
# for j in range(len(sample_input)):
#     if sample_input[j] not in temp:
#         x = []
#         x.append(sample_input[j])
#         if j == len(sample_input) - 1:
#             y.append([sample_input[len(sample_input) - 1]])
#
#         for i in range(j + 1, len(sample_input)):
#             if sorted(x[0]) == sorted(sample_input[i]):
#                 x.append(sample_input[i])
#                 if x[0] not in temp:
#                     temp.extend(x)
#                     y.append(x)
#             elif x[0] not in sample_input[:j+1]:
#                 y.append(x)
# print(y)


# sample_input = ["eat", "bat", "tea", "tan", "ate", "nat"]
# y = []
# temp = []
# for j in range(len(sample_input)):
#     x = []
#     x.append(sample_input[j])
#     if j == len(sample_input) - 1 and sample_input[len(sample_input) - 1] not in sample_input[:-1]:
#         y.append([sample_input[len(sample_input) - 1]])
#
#     for i in range(j + 1, len(sample_input)):
#         if sorted(x[0]) == sorted(sample_input[i]):
#             x.append(sample_input[i])
#             # print(x)
#             if x[0] not in temp:
#                 temp.extend(x)
#                 y.append(x)
# print(y)


sample_input = ["eat", "bat", "tea", "tan", "ate", "nat"]

x = {}

for elem in sample_input:
    sorted_el = ''.join(sorted(elem))
    if sorted_el in x:
        x[sorted_el].append(elem)
    else:
        x[sorted_el] = [elem]

print(list(x.values()))


# dict = {1: ['1']}
# dict[1].append('2')
# print(dict)
