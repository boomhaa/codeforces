#https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/A

n,k=map(int,input().split())
mass=list(map(int,input().split()))
zapros=list(map(int,input().split()))

for i in range(k):
    ans='NO'
    l=0
    r=n-1
    while l<=r:
        mid=(r+l)//2
        if mass[mid]<zapros[i]:
            l=mid+1
        elif mass[mid]>zapros[i]:
            r=mid-1
        else:
            ans='YES'
            break
    print(ans)