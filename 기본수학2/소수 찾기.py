N = int(input())
so = list(map(int, input().split()))

cnt = 0
for i in so:
    isTrue = True
    if i == 1:
        continue
    for j in range(2, i):
        if i%j == 0 :
            isTrue = False
    if isTrue == True:
        cnt +=1
print(cnt)