n = int(input())
v = list(map(int, input().split()))
l = list(map(int, input().split()))
m = int(input())
if m != 1:
    a = list(map(int, input().split()))
else:
    a = input()
f = list(map(int, input().split()))
q = int(input())
p = 0
for j in range(n):
    p += l[j] / v[j]
for i in range(q):
    s, t = map(int, input().split())

    if m != 1:
        a.append(a[-1] + 1)
        if s + p > t:
            for j in range(m):
                h = 0
                for k in range(n):
                    h += l[k] / (v[k] + a[j])
                if h + s <= t:
                    print(f[j])
                    break

        else:
            print(0)
    else:
        if s + p > t:
            print(f[0])
        else:
            print(0)
