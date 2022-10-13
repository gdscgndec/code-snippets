<!-- Wave sorting is not like other sorting that is it will be printed only in increasing order of the number, it will print in wave format. -->

<!-- The expected output is:  3 1 7 4 6 2 5-->

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
    for (int i=0;i<n;i+=2)
    {
        if (i>0 && arr[i-1] > arr[i])
        {
            swap (arr[i], arr[i-1]);
        }
        if (arr[i+1] > arr[i] && i <= n-2)
        {
            swap(arr[i], arr[i+1]);
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


