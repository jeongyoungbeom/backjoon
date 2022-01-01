import sys

while True:
    a = list(map(int, sys.stdin.readline().split()))
    if sum(a) == 0:
        break
    Max = max(a)
    a.remove(max(a))
    if a[0]**2 + a[1]**2 == Max**2:
        print("right")
    else:
        print("wrong")