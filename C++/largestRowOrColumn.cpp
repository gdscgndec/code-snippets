#include<iostream>
using namespace std;
int main(){
    int no_of_testcases;
    cin>>no_of_testcases;
    int array[50], array_numbers[50][50], row_index=0;
    for(int i=0; i<2*no_of_testcases; i=i+2){
        cin>>array[i]>>array[i+1];
        for(int j=row_index; j<row_index+array[i]; j++){
            for(int k=0; k<array[i+1]; k++){
                cin>>array_numbers[j][k];
            }
        }
        row_index=row_index+array[i];
    }

    
    // Main algo
    int max_number=INT32_MIN, index=0;
    bool what=0;
    row_index=0;
    for(int i=0; i<2*no_of_testcases; i=i+2){
        // Only for one test case
        for(int j=row_index; j<row_index+array[i]; j++){
            int sum=0;
            for(int k=0; k<array[i+1]; k++){
                sum+=array_numbers[j][k];
            }
            if (max_number<sum){
                max_number=sum;
                index=j-row_index;
                what=0;
            }
        }

        for(int k=0; k<array[i+1]; k++){
            int sum=0;
            int j;
            for(j=row_index; j<row_index+array[i]; j++){
                sum+=array_numbers[j][k];
            }
            if (max_number<sum){
                max_number=sum;
                index=j-row_index;
                what=1;
            }
        }
        if (max_number==INT32_MIN){
            cout<<"row 0 "<<INT32_MIN<<endl;
        }
        else if (what==1){
            cout<<"column "<<index<<" "<<max_number<<endl;
        }
        else{
            cout<<"row "<<index<<" "<<max_number<<endl;
        }

        row_index=row_index+array[i];
    }


    //printing
    // row_index=0;
    // for(int i=0; i<2*no_of_testcases; i=i+2){
    //     cout<<array[i]<<" "<<array[i+1];
    //     cout<<endl;
    //     for(int j=row_index; j<row_index+array[i]; j++){
    //         for(int k=0; k<array[i+1]; k++){
    //             cout<<array_numbers[j][k]<<" ";
    //         }
    //         cout<<endl;
    //     }
    //     row_index=row_index+array[i];
    // }
    
 
}