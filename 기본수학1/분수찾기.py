n = int(input())
max = 0
line = 0
while n > max:
    line += 1
    max += line
gap = max - n

if line%2 == 0:
    top = line - gap
    bottom = gap + 1
else:
    top = gap + 1
    bottom = line - gap
print(f'{top}/{bottom}')