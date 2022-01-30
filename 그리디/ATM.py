n = int(input())
List = list(map(int, input().split()))
List.sort()
sum = 0
result = 0
for i in List:
    sum += i
    result += sum
print(result)