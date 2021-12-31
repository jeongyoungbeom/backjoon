sieve = [True] * 10000
m = int(10000**0.5)
for i in range(2, m + 1):
    if sieve[i] == True:
        for j in range(i+i, 10000, i):
            sieve[j] = False

T = int(input())

for i in range(T):
    n = int(input())
    a = n//2
    for j in range(a, 1, -1):
        if sieve[j] and sieve[n-j]:
            print(j, n-j)
            break