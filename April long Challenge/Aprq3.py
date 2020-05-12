# cook your dish here
import math
import os

def func(n,k):
    a =[]
    while(n%2 == 0):
        a.append(2)
        n= n//2
    cil=math.ceil(math.sqrt(n))
    for i in range(3, cil, 2): 
        while n % i == 0: 
            n = n / i; 
            a.append(i) 
    if(n>2):
        a.append(n)
    if(len(a)<k):
        return 0
    else:
        return 1    


def driver():
    t=int(input())
    for x in range(t):
        arr = list(map(int, input().split()))
        n=arr[0]
        k=arr[1]
        re=func(n,k)
        if(re==0):
            print(0)
        elif(re==1):
            print(1)    
    
driver()    