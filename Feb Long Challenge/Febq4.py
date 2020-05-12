# cook your dish here
def check():
    t= int(input())
    for x in range(t):
        n=list(map(int,input().strip().split()))[:2]
        m=list(map(int, input().split()))
        for i in range(0,n[0]):
            flag=0
            if(n[1]%m[i]!= 0): 
                flag=1
                break
        for i in range(0,(n[0]-1)):
            for j in range(i+1,n[0]):
                if(m[j]%m[i]!=0):
                    flag=1
                    break
        if(flag==0):
            print("NO")
        else:
            findMin(n[0],n[1],m)   

def findMin(n,q,m): 
    result=[0]*n
    i=n-1
    while q>0 and i>=0:
        if q%m[i]==0:
            tem=int(q/m[i])-1
            result[i]=tem
            q=q-(tem*m[i])
        else:
            tem=int(q/m[i])+1
            result[i]=tem
            q=q-(tem*m[i])  
        i-=1      
    print("YES",end=' ')
    print(" ".join(map(str,result)))


     

check()
#t= int(input())
#for x in range(t):
    #n=list(map(int,input().strip().split()))[:2]
    #m=list(map(int,input().strip().split()))[:n[0]]
    #if(check(n[1],n[0],m))==1:
        #print("NO")
    #else: 
        #findMin(n[1],n[0],m)
