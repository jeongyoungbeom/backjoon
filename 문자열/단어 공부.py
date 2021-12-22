# A = input().upper()
# a = list(set(A))
# cnt = 0
# m = ""
# for i in a:
#     if A.count(i) > cnt:
#         cnt = A.count(i)
#         m = i
#     elif A.count(i) == cnt:
#         m = "?"
# print(m)

A = input().upper()
a = list(set(A))
cnt = [A.count(i) for i in a]
if cnt.count(max(cnt)) >=2:
    print("?")
else:
    print(a[cnt.index(max(cnt))])