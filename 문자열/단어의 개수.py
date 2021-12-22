A = input()
B = A.strip().split(" ")
if len(B) == 1:
    if B[0] == "":
        print(0)
    else:
        print(1)
else:
    print(len(B))

# A = list(map(str, input().split()))
# print(len(A))