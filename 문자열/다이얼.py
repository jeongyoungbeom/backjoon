A = input()
B = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sum = 0
for i in A:
    for j in B:
        if i in j:
            sum += B.index(j)+3
            break
print(sum)

