n, k = map(int, input().split())
list = []
for i in range(n):
    list.append(int(input()))

list.sort(reverse=True)
count = 0
for i in list:
    if i <= k:
        count += k // i
        k = k % i
    if i == 1:
        break
print(count)