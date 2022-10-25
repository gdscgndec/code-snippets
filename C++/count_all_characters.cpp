// C++ program to count the number of vowels, consonants, digits, white spaces and special characters in a string.

#include<iostream>
using namespace std;

int main()
{
    char str[300];
    int i, vow=0, cons=0, dig=0, wspace=0, specialsymb=0;
    cout<<"Enter the string:"<<endl;
    cin.getline(str, 300);
    for(i=0; str[i] != '\0'; i++){
        if ( str[i]=='a'||str[i]=='e'||str[i]=='i'||str[i]=='o'||str[i]=='u'||str[i]=='A'||str[i]=='E'||str[i]=='I'||str[i]=='O'||str[i]=='U'){
            vow++;
        }
        else if((str[i]>='a'&&str[i]<='z')||(str[i]>='A'&&str[i]<='Z')){
            cons++;
        }
        else if((str[i]>='0'&&str[i]<='9')){
            dig++;
        }
        else if(str[i]==' '){
            wspace++;
        }
        else{
            specialsymb++;
        }
    }
    cout<<"Vowels :"<<vow<<endl;
    cout<<"Consonants :"<<cons<<endl;
    cout<<"Digits :"<<dig<<endl;
    cout<<"White Spaces :"<<wspace<<endl;
    cout<<"Special Characters :"<<specialsymb<<endl;
    return 0;
}
