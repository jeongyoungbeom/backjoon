A, B, C = map(int, input().split())

while True:
     if B >= C:
          print(-1)
          break
     else:
          print((A//(C-B))+1)
          break