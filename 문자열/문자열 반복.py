import sys

T = int(input())
for i in range(T):
    C = ""
    R, S, = map(str, sys.stdin.readline().split())
    for i in S:
        C += i * int(R)
    print(C)


