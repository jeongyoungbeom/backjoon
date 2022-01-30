import sys


def stack(List, a):
    if a[0] == 'push':
        List.append(a[1])
    elif a[0] == 'top':
        if not List:
            print(-1)
        else:
            print(List[-1])
    elif a[0] == 'size':
        print(len(List))
    elif a[0] == 'empty':
        if not List:
            print(1)
        else:
            print(0)
    elif a[0] == 'pop':
        if not List:
            print(-1)
        else:
            print(List.pop())


List = []

n = int(input())
for i in range(n):
    a = sys.stdin.readline().split()
    stack(List, a)
