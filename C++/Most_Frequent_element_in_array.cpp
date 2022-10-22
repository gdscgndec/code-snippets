// C++ code to find the most frequent element in the array
// We will use an efficient approach to solve the problem by using hashmaps for finding the frequency of each element in the array.

#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cout<<"Enter the size of array: "; 
    cin>>N;  //size of array
    cout<<endl;
    int arr[N]; 
    unordered_map<int , int> Map;
    cout<<"Enter the elements of array: "<<endl;
    for(int i=0 ; i<N; i++){
        cin>>arr[i]; // user will enter the elements of the array
        Map[arr[i]]++; // map to count the frequency of particular element and storing it as a key value pair
    }
    int max_freq = 0 , answer = -1;
    for(auto x: Map){
        if(max_freq < x.second){
            answer = x.first; //most frequent element
            max_freq = x.second; //maximum frequency of element
        }
    }
    cout<<"The most frequent element in the array is: "<<answer<<" and its frequency is: "<<max_freq<<endl;
    
    return 0;
    
}
