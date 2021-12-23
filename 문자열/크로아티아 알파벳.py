A = input()
B = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'dz=', 'z=']
for i in B:
    if i in A:
        A = A.replace(i, "A")
print(len(A))