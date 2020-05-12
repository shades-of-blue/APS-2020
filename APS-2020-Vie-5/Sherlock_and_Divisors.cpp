#include<bits/stdc++.h>
using namespace std;


int divisors(int n) {
    /*
     * Write your code here.
     */
    int count=0;
    for (int i=1;i<=sqrt(n);i++)
    {
        if (n%i==0)
        {
            if (i%2==0) count++;
            if ((n/i)%2==0) count++;
        }
    }
    if ((n%2==0) && (pow((int)sqrt(n), 2) == n))  count--;
    return count;
}

int main(){
    int t,n;
    cin>>t;
    while(t--){
        cin>>n;
        cout<<divisors(n)<<endl;
    }

}