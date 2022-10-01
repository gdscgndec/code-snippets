//PASCAL TRIANGLE
#include <iostream>
using namespace std;

int main() {
	long long n;
	cin>>n;
	long long coef=1;
	for(long long i=0;i<n;i++){
	    for(long long j=0;j<n-i;j++)
	        cout<<" ";
	   for(long long k = 0;k<=i;k++){
	       if(k==0 || i==0)coef = 1;
	       else
	        coef = coef*(i-k+1)/k;
	        cout<<" "<<coef;
	   }
	   cout<<endl;
	}
	return 0;
}
