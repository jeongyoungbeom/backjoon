import string

s = input()
b = string.ascii_lowercase

for i in b:
        print(s.find(i), end=" ")

# SYS = 'abcdefghijklmnopqrstuvwxyz'
#
# word = input()
# for char in SYS:
#     print(word.find(char), end=' ')


# a = input()
# print(*[a.find(chr(i)) for i in range(97,123)])