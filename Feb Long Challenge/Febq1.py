# cook your dish here
t= int(input())
for x in range(t):
    n=int(input())
    count=0
    a=list(map(int,input().strip().split()))[:n]
    b=list(map(int,input().strip().split()))[:n]
    a.sort()
    b.sort()
    for i in range(n):
        count+=min(a[i],b[i])
    print(count)
