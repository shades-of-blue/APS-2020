#include <bits/stdc++.h>
using namespace std;
//int myXOR(int x, int y) 
//{ 
//   return x ^ y; 
//}
bool getParity(unsigned int n) 
{ 
    bool parity = 0; 
    while (n) 
    { 
        parity = !parity; 
        n     = n & (n - 1); 
    }      
    return parity; 
}
void run(){
    int t,n,q;
    //vector<int> arr;
    cin>>t;
    while(t--){
        int qa,inp;
        int op=0,ep=0;
        cin>>n>>q;
        for(int i=0;i<n;i++){
           cin>>qa;
           if(getParity(qa)){op++;}
           else{ep++;}
           //if(!getParity(qa)){ep++;} 
        }
        while(q--){
            cin>>inp;
            if(getParity(inp)){cout<<op<<" "<<ep<<"\n";}
            else{cout<<ep<<" "<<op<<"\n";}
            //if(!getParity(inp)){cout<<ep<<" "<<op<<"\n";}
        }
    }
}
int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    run();
return 0;
}