#include<iostream>
using namespace std;
int main(){
 int N;
 cin>>N;
 int previous=1, current=1, next=1;
 if (N>=3){
     for (int i=3; i<=N;i++){
         next=previous+current;
        //  cout<<"----"<<endl;
         previous=current;
        //  cout<<previous<<endl;
         current=next;
        //  cout<<current<<endl;
        //  cout<<"----"<<endl;
        
 }
 }
 cout<<next<<endl;
 
 
}