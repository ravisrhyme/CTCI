/*
	Problem : Write a program to check if a number is power of 2
	Author  : Ravi Kiran Chadalawada
*/

#include<iostream>
using namespace std;


int main()
{
	int a = 8;

	int result = (a & (a-1));// Bit Operation that helps with oer of two

	if (result == 0){
		cout << "Yes. Power of two" << endl;
	}
	else {
		cout << "No. Not a Power of two" << endl;
	}
	return 0;
}
