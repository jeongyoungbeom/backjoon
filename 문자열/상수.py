A, B = map(str, input().split())
A = int("".join(reversed(A)))
B = int("".join(reversed(B)))
print(A if A>B else B)
# A = A[::-1]

