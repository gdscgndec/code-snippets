#include <bits/stdc++.h>
using namespace std;

int main()
{
	int arr[] = { 5, 3, 2, 2, 7, 5, 2, 3, 4 };
	int n = sizeof(arr) / sizeof(arr[0]);
	// count the frequency
	for (int i = 0; i < n; i++) {
		arr[arr[i] % n]
			= arr[arr[i] % n] + n;
	}
	cout << "The Duplicates elements are : " << endl;
	for (int i = 0; i < n; i++) {
		if (arr[i] >= n * 2) {
			cout << i << " " << endl;
		}
	}
	return 0;
}

