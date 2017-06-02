/*
	Problem : Write a function to determine the number of bits required to convert
		      Integer A to integer B.
	Author  : Ravi Kiran Chadalawada
*/

#include<iostream>
using namespace std;


int main()
{
	int a = 10;
	int b = 7;
	int count = 0;
	int c = a ^ b; // XOR of a,b. All bits with same values is set to zero
	while (c != 0) {
		count++;
		c = (c & (c-1)); // sets the left most '1' as '0'
	}
	cout << "Count is " << count << endl;
}
