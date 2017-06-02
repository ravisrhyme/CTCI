/*
	Problem : Write a program to swap odd and even bits of a given integer
	Author  : Ravi Kiran Chadalawada
*/

#include<iostream>
using namespace std;


int main()
{
	int a = 10;
	/* 
		Assuming integer to be 32 bit number, 
		a.to set all even bits to zero, AND with 10101010101010.. 
		  each 1010 is 'a' in Hex and left shift by 1
		b.to set all odd bits to ero, AND with 0101-0101-0101..   
		  each 0101 is '5' in Hex and right shift by 1
		c. Do OR of a,b
		
	*/
	int c = ((a & 0xaaaaaaaa) >> 1) |  ((a & 0x55555555) << 1);	
	cout << "new number is " << c << endl;
}
