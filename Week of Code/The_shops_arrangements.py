for _ in range(int(input())):
    n = int(input())
    shops = list(map(int, input().split()))
    for i in range(int(input())):
        k = list(map(int, input().split()))
        if k[0]==0:
            m = shops[k[1]-1:k[2]]
            m.sort()
            print(m[k[3]-1])
        if k[0]==1:
            shops[k[1]-1]=k[2]
            #print(shops[k[1]-1])