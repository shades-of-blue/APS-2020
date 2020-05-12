# cook your dish here
t=int(input())
for x in range(t):
    b=list(map(int,input().strip().split()))[:2]
    a=list(map(int,input().strip().split()))[:b[0]]
    print(sum(a)%b[1])