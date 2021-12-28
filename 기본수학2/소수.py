M = int(input())
N = int(input())
cnt = []

for i in range(M, N+1):
    flag = 0
    if i == 1:
        continue
    for j in range(2, i):
        if i%j == 0:
            flag = 1
            break
    if flag == 0:
        cnt.append(i)
if len(cnt) == 0:
    print(-1)
else:
    print(sum(cnt))
    print(min(cnt))