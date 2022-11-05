# https://codeforces.com/contest/1747/problem/C

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    j = 0
    a[0] -= 1
    h = a.index(min(a[1:]))
    a[0], a[h] = a[h], a[0]
    j += 1
    if a[0] <= min(a[1:]):
        j += a[0] * 2
    else:
        j += min(a[1:]) * 2 + 1
    if j % 2 == 0:
        print('bob')
    else:
        print('alice')
