# cook your dish here
from collections import defaultdict
for i in range(int(input())):
    n,m=input().split()
    f = list(map(int,input().strip().split()))[:int(n)]
    p = list(map(int,input().strip().split()))[:int(n)]
    d = defaultdict(int)
    for a,b in zip(f,p):
        d[a]+=b
    print(min(d.values()))    


