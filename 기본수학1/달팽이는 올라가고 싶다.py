A, B, V = map(int, input().split())
K = (V-B)/(A-B)
if K == int(K):
    print(int(K))
else:
    print(int(K)+1)

# 너무어렵다..