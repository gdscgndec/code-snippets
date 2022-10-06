#include<iostream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

/*
 Sample input
 2 3     => 2 is number of variable length array and 3 is number of queries
 3 6 20 32    => 3 is size of array and than element of array
 4 9 19 55 24    => 4 is size of array and than element of array
 0 2        => query 1: index number of arrays.
 1 2        => query 2: index number of arrays.
 0 1        => query 3: index number of arrays.
*/

int main() {
    int x, y, s=0;
       cin >> x >> y;
       int* arr[x];
       
    while (x--) 
    {
        int n;
        cin>>n;
       
        arr[s]=new int[n];
       
        for (int i=0; i<n; i++) {
            cin>>arr[s][i];
            
       }
        s++;
       
       }
       while (y--) {
            int a,b;
            cin>>a>>b;
       
            cout<<arr[a][b]<<endl;
       }
    return 0;
}