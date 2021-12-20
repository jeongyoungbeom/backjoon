import sys

a = list(map(int, sys.stdin.readline().split()))
def solve(a):
    # sum = 0
    # for i in range(len(a)):
    #     sum+=a[i]
    # return sum
    return sum(a)
print(solve(a))