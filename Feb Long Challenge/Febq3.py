# cook your dish here
from itertools import permutations
#from itertools import izip
def fun():
    try:
        st=[i for i in permutations([0,1,2,3]) if len(set(i))==4]
        res=[]
        dic={'A':0,'B':1,'C':2,'D':3,'12':0,'3':1,'6':2,'9':3}
        for _ in range(int(input())):
            ar=[[0]*4 for i in range(4)]
            for i in range(int(input())):
                a,c=map(str, input().split(' '))
                ar[dic[a]][dic[c]]+=1
            cn=[]
            for mv in st:
                for tm in st:
                    gain=[100,75,50,25]
                    cash=[]
                    link=zip(mv,tm)
                    for i,j in link:
                        cash.append(ar[i][j])
                        cash.sort(reverse=True)
                    s=0
                    linkb=zip(cash,gain)
                    for i,j in linkb:
                        if(i>0):
                            s+=i*j
                        else:
                            s-=100
                    cn.append(s)
            s=max(cn)
            print(s)
            res.append(s)
        print(sum(res))
    except:
        pass


      

fun() 