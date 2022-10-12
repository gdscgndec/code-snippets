#include<stdio.h>
int main()
{
int age;
printf("enter your age");
scanf("%d",age);

switch(age)// Defining switch case

{ case 3; //applying different conditions 
printf("the age is 3");// output according to condition
break;// using break to exit loop else the program will print all unnecessary results

case 13;
printf("the age is 13");
break;

case 23
printf("the is 23");
break;
default:
	printf("age is not 3,13 or 23");
	break;
}
return 0;
}
