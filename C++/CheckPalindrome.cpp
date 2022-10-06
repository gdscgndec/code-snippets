#include<iostream>
using namespace std;
int checkPalindrome(char input[]){
  int last_index;
  for(last_index=0; input[last_index]!='\0'; last_index++){
  }
  last_index=last_index-1;
  for(int i=0, j=last_index; input[i]!='\0', j>=0; i++, j--){
      
        if (input[i]!=input[j]){
            return 0;
        }

  }
  return 1;
}
int main(){
 char a[20];
 cin>>a;
 if (checkPalindrome(a)){
     cout<<"YES"<<endl;
 }
 else{
     cout<<"NO"<<endl;
 }
}