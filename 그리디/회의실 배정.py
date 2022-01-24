n = int(input())
List = []
for i in range(n):
    List.append(list(map(int, input().split())))
List.sort(key=lambda x: x[0]) # 리스트를 x[0]으로 정렬
List.sort(key=lambda x: x[1]) # 리스트를 x[1]으로 정렬
count = 0
a = b = 0

print(List)
for x, y in List:
    if x >= b:
        count += 1
        b = y
print(count)