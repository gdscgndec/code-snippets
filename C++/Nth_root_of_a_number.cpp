/*
2 16
mid = 9
9*9 = 81 > 16
2 9
mid = 5
25>16
2 5
mid = 3
3*3 = 9< 16
3 5
*/

#include <bits/stdc++.h>
using namespace std;
double getPow(double n,double m){
    double ans = 1.0;
    long long newNum = m;
    if(m<0)newNum = newNum*-1;
    while(newNum > 0){
        if(newNum%2==0){
            n = n*n;
            newNum /=2;
        }else{
            ans = ans*n;
            newNum = newNum-1;
        }
    }
    if(m<0)ans = (double)(1.0)/(double)(ans);
    return ans;
}
double getNth(int n,int m){
    double l = 1,h = m;
    double eps = 1e-6;
    while((h-l) > eps){
        double mid = (l+h)/2.0;
        
        if(getPow(mid,n)>m){
            h = mid;
        }else{
            l = mid;
        }
    }
    return l;
}

int main(){
    int n,m;
    cin>>n>>m;
    cout<<"Nth Root of a number : "<<getNth(n,m);
    return 0;
}
