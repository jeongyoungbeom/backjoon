import sys
from collections import deque


def queue(List, words):
    if words[0] == 'push':
        List.append(int(words[1]))
    elif words[0] == 'pop':
        if not List:
            print(-1)
        else:
            print(List.popleft())
    elif words[0] == 'size':
        print(len(List))
    elif words[0] == 'empty':
        if not List:
            print(1)
        else:
            print(0)
    elif words[0] == 'front':
        if not List:
            print(-1)
        else:
            print(List[0])
    elif words[0] == 'back':
        if not List:
            print(-1)
        else:
            print(List[-1])


n = int(sys.stdin.readline())
data = deque([])
for _ in range(n):
    word = sys.stdin.readline().split()
    queue(data, word)
