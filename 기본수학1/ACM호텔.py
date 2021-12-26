import sys

T = int(input())
for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    if N%H == 0:
        first = H
        second = (N // H)
    else:
        first = N%H
        second = (N // H) + 1
    if second < 10:
        second = "0"+str(second)
    print(f'{first}{second}')