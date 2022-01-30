import sys

n = int(input())

for i in range(n):
    a = sys.stdin.readline()
    List = []
    for j in a:
        if j == "(":
            List.append(j)
        elif j == ")":
            if len(List) != 0 and List[-1] == "(":
                List.pop()
            else:
                List.append(")")
                break

    if len(List) == 0:
        print("YES")
    else:
        print("NO")
