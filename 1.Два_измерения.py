l = int(input())
r = int(input())
a = int(input())
big = (r - l + 1) % a
small = a - big
k = (r - l + 1) // a
ans = big * k * (k + 1) // 2 + small * k * (k - 1) // 2
print(ans)