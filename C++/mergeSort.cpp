#include <iostream>
using namespace std;

// Merge two subarrays into Arr1 and Arr2
void merge(int arr[], int p, int q, int r) {
  

  int n1 = q - p + 1;
  int n2 = r - q;

  int Arr1[n1], Arr2[n2];

  for (int i = 0; i < n1; i++)
    Arr1[i] = arr[p + i];
  for (int j = 0; j < n2; j++)
    Arr2[j] = arr[q + 1 + j];

 
  int i, j, k;
  i = 0;
  j = 0;
  k = p;


  while (i < n1 && j < n2) {
    if (Arr1[i] <= Arr2[j]) {
      arr[k] = Arr1[i];
      i++;
    } else {
      arr[k] = Arr2[j];
      j++;
    }
    k++;
  }

  while (i < n1) {
    arr[k] = Arr1[i];
    i++;
    k++;
  }

  while (j < n2) {
    arr[k] = Arr2[j];
    j++;
    k++;
  }
}


void mergeSort(int arr[], int l, int r) {
  if (l < r) {
    
    int m = l + (r - l) / 2;
//  divide the array into two halves 
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);

    // Merge the sorted subarrays
    merge(arr, l, m, r);
  }
}


void printArray(int arr[], int size) {
  for (int i = 0; i < size; i++)
    cout << arr[i] << " ";
  cout << endl;
}

int main() {
  int arr[] = {10, 4, 12, 6, 8, 20, 3};
  int size = sizeof(arr) / sizeof(arr[0]);

  mergeSort(arr, 0, size - 1);

  cout << "Sorted array will be: \n";
  printArray(arr, size);
  return 0;
}