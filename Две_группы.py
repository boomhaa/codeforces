#https://codeforces.com/contest/1747/problem/A

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s1=0
    s2=0
    for j in a:
        if j<0:
            s1+=j
        else:
            s2+=j
    print(max(abs(s1),abs(s2))-min(abs(s1),abs(s2)))