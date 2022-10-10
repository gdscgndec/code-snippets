#include<bits/stdc++.h>
using namespace std;

void swap (int arr[], int i, int j)
{
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

void waveSort(int arr[], int n)
{
    for (int i=1;i<n;i+=2)
    {
        if (arr[i]>arr[i-1])
        {
            swap (arr,i,i-1);
        }
        if (arr[i]>arr[i+1])
        {
            swap(arr,i,i+1);
        }
    }
}

int main ()
{
    int n = 7;
    int arr[7] = {1,3,4,7,5,6,2};
    waveSort(arr,7);

    for (int i=0;i<n;i++)
    {
        cout<<arr[i];
    }
    cout<<endl;

    return 0;
}