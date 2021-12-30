import sys


sieve = [True] * 300000
m = int(300000**0.5)
for i in range(2, m + 1):
    if sieve[i] == True:
        for j in range(i+i, 300000, i):
            sieve[j] = False

while True:
    N = int(sys.stdin.readline())
    cnt = 0
    if N == 0:
        break
    for i in range(N+1, (2*N)+1):
        if sieve[i] == True:
           cnt+=1
    print(cnt)