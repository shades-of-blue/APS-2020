def func(a):
    m=1000000007
    s = 0
    for i in range(len(a)):
        if(a[i]-i<=0):
            s=s+0
        else:
            s= s+(a[i]-i)
    print(s%m)


def driver():
    t=int(input())
    for x in range(t):
        n = int(input())
        a =list(map(int, input().split()))
        a.sort(reverse=True)
        func(a)
        
driver()        