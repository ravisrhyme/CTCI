/*******************************************************************************
*                                                                              *
* File : C1.2.cpp                                                              *
*                                                                              *
* Author: Ravi Kiran Chadalawada                                               *
*                                                                              *
* Description: This file has the implementation for the 2nd problem of         *
*              chapter-1 of Cracking the coding interview                      *
*                                                                              *
* Problem Statement : Implement a function void reverse(char *str) in C or C++ *
*                     which reverses a null terminated string                  * 
*                                                                              *
*******************************************************************************/
#include<iostream>
#include<string>
using namespace std;

void reverse(string input_string);

int main()
{
 
	string input_string;
	cout << "Enter string to be reversed :";
	cin >> input_string;
 	reverse(input_string);
	return 0;
}

void reverse(string input_string)
{
	int i = 0;
	cout << "reverse_string is :";
	for (i = input_string.length()-1; i >= 0; i--)
	{
		cout << input_string.at(i);
	}
	cout << endl;
	
}
