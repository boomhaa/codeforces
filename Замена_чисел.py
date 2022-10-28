for i in range(int(input())):
    my_hash = {}
    n=int(input())
    digits=list(map(int,input().split()))
    letters=input()
    ans='YES'
    for j in range(n):
        if digits[j] in my_hash:
            if my_hash[digits[j]] !=letters[j]:
                ans='NO'
                break
        else:
            my_hash[digits[j]]=letters[j]
    print(ans)