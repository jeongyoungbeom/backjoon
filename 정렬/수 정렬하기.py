N = int(input())
a = []
for i in range(N):
    a.append(int(input()))

for i in range(len(a)):
    a.sort()
    print(a[i])
