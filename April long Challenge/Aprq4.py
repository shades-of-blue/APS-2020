# cook your dish here
import math
import os

def case1(n):
    print(1)
    print(*[1,1])

def case2(n):
    print(int(n/2))
    for k in range(1,n+1,2):
        print(*[2,k,k+1])
def case3(n):
    print(n//2)
    print(*[3,1,2,n])
    for i in range(3,n,2):
        print(*[2,i,i+1])

def func(n):
    if n==1:
        case1(n)
    if n%2==0:
        case2(n)
    else:
        case3(n)

   

def driver():
    for t in range(int(input())):
        n = int(input())
        func(n)

driver()