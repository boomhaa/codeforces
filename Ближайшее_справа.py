#https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/C

n, k = map(int, input().split())
mass = list(map(int, input().split()))
zapros = list(map(int, input().split()))
j1 = float('-inf')
j2 = float('inf')
mass = [j1] + mass
mass.append(j2)
for i in range(k):
    ans = 'NO'
    l = 0
    r = n + 1
    while l + 1 < r:
        mid = (r + l) // 2
        if mass[mid] < zapros[i]:
            l = mid
        elif mass[mid] >= zapros[i]:
            r = mid

    print(r)