# def matrix(n=1, m=None, value=0):
#     result = []
#     # if m != 0:
#     #     for i in range(n):
#     #         result.append([value] * m)
#     # else:
#     #     for i in range(n):
#     #         result.append([value] * n)
#     # return result
#     if m is None:
#         m = n
#     for i in range(n):
#         result.append([value] * m)
#     return result
#
# print(matrix())
# print(matrix(3))
# print(matrix(2, 5))
# print(matrix(3, 4, 9))
# print(matrix(3, 1))
words = ['apple', 'banana', 'cherry', 'date']
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)