N, M = map(int, input().split())
list = list(map(int, input().split()))
result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = list[i] + list[j] + list[k]
            if sum <= M:
                result = max(result, sum)
print(result)