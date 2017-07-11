/*******************************************************************************
*                                                                              *
* File : C1.5.cpp                                                              *
*                                                                              *
* Author: Ravi Kiran Chadalawada                                               *
*                                                                              *
* Description: This file has the solution for the 5th problem of chapter-1 of  *
* Cracking the coding interview                                                *
*                                                                              *
* Problem Statement : Implement a method to perform basic string compression by*
                      using counts of repeated characters                      *
*                                                                              *
*******************************************************************************/



#include<iostream>
#include<string>
using namespace std;

void  compress_string(string input_string);

int main()
{
	string input_string;
	cout << "Enter input string : ";
	cin >> input_string;
	compress_string(input_string);
	return 0;
}

void  compress_string(string input_string)
{
	string compressed_string;
	int i = 0;
	char c = input_string.at(0);
	int count_character = 0;

	// Logic for compression technique specified
	for (i = 0; i < input_string.length(); i++)
	{
		if (input_string.at(i) == c)
		{
			count_character++;
		}
		else
		{
			compressed_string += c;
			compressed_string += std::to_string(count_character);
			
			c = input_string.at(i);
			count_character = 1;
		}
	}
	compressed_string += c;
	compressed_string += std::to_string(count_character);

	cout << "Compressed String : " << compressed_string << endl;

	if (compressed_string.length() >= input_string.length())
	{
		cout << "Final String : " << input_string << endl;
	}
	else 
	{
		cout << "Final string : " << compressed_string << endl;
	}
	return;
}
