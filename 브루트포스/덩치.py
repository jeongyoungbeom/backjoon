N = int(input())
list = [[int(i) for i in input().split()] for j in range(N)]
ans = []
for i in list:
    count = 1
    for j in list:
        if i[0] < j[0] and i[1] < j[1]:
            count+=1
    ans.append(count)

for i in ans:
    print(i, end=" ")
