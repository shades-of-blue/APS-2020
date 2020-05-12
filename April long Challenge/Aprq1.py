def min_dis(a,n):
    k=[]
    for i in range(len(a)):
        val=a[i]
        if val==1:
            k.append(a.index(val)+1)
            a[a.index(val)]=0
    flag=0
    for i in k:
        if(i+1 in k):
            flag=flag+1
            break
        elif(i+2 in k):
            flag=flag+1
            break
        elif(i+3 in k):
            flag=flag+1
            break
        elif(i+4 in k):
            flag=flag+1
            break
        elif(i+5 in k):
            flag=flag+1
            break
    if flag==1:
        print("NO")
    else:
        print("YES")

def driver():
    t=int(input())
    for x in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        min_dis(a,n)
            
driver()

    
    
