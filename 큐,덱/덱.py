import sys
from collections import deque

n = int(input())
data = deque()
for i in range(n):
    a = sys.stdin.readline().split()

    if a[0] == 'push_front':
        data.appendleft(int(a[1]))
    elif a[0] == 'push_back':
        data.append(int(a[1]))
    elif a[0] == 'pop_front':
        if not data:
            print(-1)
        else:
            print(data.popleft())
    elif a[0] == 'pop_back':
        if not data:
            print(-1)
        else:
            print(data.pop())
    elif a[0] == 'size':
        print(len(data))
    elif a[0] == 'empty':
        if not data:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if not data:
            print(-1)
        else:
            print(data[0])
    elif a[0] == 'back':
        if not data:
            print(-1)
        else:
            print(data[-1])
