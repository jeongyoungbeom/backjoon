n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))
result = 0
first = price[0]
for i in range(n-1):
    if price[i] < first:
        first = price[i]
    result += first * length[i]

print(result)