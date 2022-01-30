import sys

k = int(input())
List = []
for _ in range(k):
    a = int(sys.stdin.readline())
    if a == 0:
        List.pop()
    else:
        List.append(a)
print(sum(List))