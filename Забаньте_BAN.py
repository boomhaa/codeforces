#https://codeforces.com/contest/1747/problem/B

for i in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
        print(1, 3)
    else:
        print(n//2+n%2)
        k1=1
        k2=n*3
        while k1<k2:
            print(k1,k2)
            k1+=3
            k2-=3