/*******************************************************************************
*                                                                              *
* File : C1.4.cpp                                                              *
*                                                                              *
* Author: Ravi Kiran Chadalawada                                               *
*                                                                              *
* Description: This file has the solution for the 4th problem of chapter-1 of  *
* Cracking the coding interview                                                *
*                                                                              *
* Problem Statement : write a method to replace all spaces in strings with %20 *
                                                                               *
*                                                                              *
*******************************************************************************/

#include<iostream>
#include<string>
using namespace std;

void replace_space(string input);

int main()
{
	string input;
	cout << "Enter string :";
	getline(cin, input);
	cout << "String is " << input << endl;
	replace_space(input);
	return 0;
}

void replace_space(string input)
{
	string output;
	int i = 0;
	for (i = 0; i < input.length(); i++)
	{
		if (input.at(i) == ' ')
		{
			output += "%20";
		}
		else
		{
			output += input.at(i);
		}
	}

	cout << "Given string : " << input << endl;
	cout << "Reversed string : " << output << endl;
	return;
}
