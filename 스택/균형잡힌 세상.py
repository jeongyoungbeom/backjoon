while True:
    a = input()
    List = []
    isTrue = True
    if a == '.':
        break

    for i in a:
        if i == '(' or i == '[':
            List.append(i)
        elif i == ')':
            if not List or List[-1] == '[':
                isTrue = False
                break
            elif List[-1] == '(':
                List.pop()
        elif i == ']':
            if not List or List[-1] == '(':
                isTrue = False
                break
            elif List[-1] == '[':
                List.pop()

    if isTrue == True and not List:
        print('yes')
    else:
        print('no')
