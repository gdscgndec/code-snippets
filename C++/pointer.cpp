
#include<iostream>
using namespace std;

int main(){
    // What is a pointer? ----> Data type which holds the address of other data types
    int a=3;
    int* b;
    b = &a;

    // & ---> (Address of) Operator
    cout<<"The address of a is "<<&a<<endl;
    cout<<"The address of a is "<<b<<endl;
    //it will print the adress of the a

    // * ---> (value at) Dereference operator
    cout<<"The value at address b is "<<*b<<endl;/*  '*' is used to show the value of whose adress is shown*/

    // Pointer to pointer is used to show the adress of the b
    int** c = &b;
    cout<<"The address of b is "<<&b<<endl;
    cout<<"The address of b is "<<c<<endl; 
    cout<<"The value at address c is "<<*c<<endl; /*  here '*' is used to show the adress of the a which is the value of the c*/
    cout<<"The value at address value_at(value_at(c)) is "<<**c<<endl; 
    //  it will show the value of the  a which is the value of the b 

    return 0;
}
