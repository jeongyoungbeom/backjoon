n = int(input())
data = list(map(int, input().split()))
result = []
answer = [-1] * n

for i in range(n):
    while result and data[result[-1]] < data[i]:
        answer[result.pop()] = data[i]
    result.append(i)
print(*answer)
