def bineryy(m, n_list, end):
    start = 0
    while start <= end:
        mid = (start + end) // 2
        if m == n_list[mid]:
            return True
        if m < n_list[mid]:
            end = mid - 1
        elif m > n_list[mid]:
            start = mid + 1


n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if bineryy(i, n_list, len(n_list) - 1):
        print(1)
    else:
        print(0)
