n = int(input())
a = []
b = []
count = 1
temp = True
for _ in range(n):
    num = int(input())
    while count <= num:
        a.append(count)
        b.append('+')
        count += 1
    if a[-1] == num:
        a.pop()
        b.append('-')
    else:
        temp = False

if not temp:
    print("NO")
else:
    for i in b:
        print(i)