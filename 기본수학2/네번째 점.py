import sys

x = []
y = []

for i in range(3):
    a, b = map(int, sys.stdin.readline().split())
    x.append(a)
    y.append(b)

for i in range(3):
    if x.count(x[i]) == 1:
        q = x[i]
    if y.count(y[i]) == 1:
        w = y[i]
print(q, w)