ans=10**13

def prv(a,b,k):
    global ans
    if a*b!=k:
        return
    n1=(a-b)//2
    n2=(a+b)//2
    if n1>=0 and n2>=0 and n2<ans:
        ans=n2

k=int(input())
if k!=0:
    i=1
    while i*i<=abs(k):
        if k%i==0:
            a=i
            b=abs(k)//i
            if a%2==b%2:
                prv(b,a,k)
                prv(-b,a,k)
                prv(b,-a,k)
                prv(-b,-a,k)
                prv(a, b, k)
                prv(-a, b, k)
                prv(a, -b, k)
                prv(-a, -b, k)


        i+=1
    if ans==10**13:
        print('none')
    else:
        print(ans)
else:
    print(0)