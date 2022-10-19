#include<iostream>
using namespace std;
int main(){
    int arr[100], lengthPrev=1, length=5;
    for(int i=0; i<length; i++){
        int temp[50], count=0, index=0;
        for(int j=0; j<lengthPrev; j++){
            temp[j]=arr[j];
        }
        while(count<(length-1-i)){
            cout<<" ";
            count++;
        }
        cout<<"1 ";
        count+=2;
        arr[index++]=1;
        if(i>0){
            if(lengthPrev>1){
                while(count<(length-1-i)+i+i){
                    arr[index]+=temp[index-1];
                    cout<<arr[index++]<<" ";
                    count+=2;
                }
            }
            cout<<"1";
            arr[index++]=1;
            count++;    
        }
        lengthPrev=index;
        cout<<endl;
    }


}
/*
    1
   1 1
  1 2 1
 1 3 3 1*/