from bisect import insort

def median(a):
    if len(a)%2==0:
        l=a[len(a)//2];r=a[(len(a)//2)-1]
        med=(l+r)/2.0
        
    elif len(a)%2 !=0:
        med=a[len(a)//2]
    return med

if __name__ =='__main__':
    heap=[]
    for _ in range(int(input())):
        insort(heap,int(input()))
        print(float(median(heap)))