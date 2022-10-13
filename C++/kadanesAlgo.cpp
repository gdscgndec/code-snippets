/*
Input:
5
-1 2 3 -2 4

Expected Output: 
7
*/

#include <iostream>
using namespace std;

long long maxSubarraySum(int arr[], int n){
    long long sum = 0, maxi = arr[0];
    for(int i=0; i<n; i++) {
        sum += arr[i];
        if(sum > maxi)
            maxi = sum;
        if(sum < 0)
            sum = 0;
    }
    return maxi;
}

int main() {
    int n;
    cin >> n;
    int arr[n];
    for(int i=0; i<n; i++)
        cin >> arr[i];

    cout << maxSubarraySum(arr, n);
}
