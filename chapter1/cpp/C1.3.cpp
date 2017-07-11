/*******************************************************************************
*                                                                              *
* File : C1.3.cpp                                                              *
*                                                                              *
* Author: Ravi Kiran Chadalawada                                               *
*                                                                              *
* Description: This file has the solution for the 3rd problem of chapter-1 of  *
* Cracking the coding interview                                                *
*                                                                              *
* Problem Statement : Given two strings, write a method to decide if one is a  *
                      permutation of other                                     *
*                                                                              *
*******************************************************************************/

#include<iostream>
#include<string>
using namespace std;


void string_compare(string first_string,string seccond_string);

int main()
{
	string first_string,second_string;
	cout << "Enter First string :";
	cin >> first_string;
	cout << "Enter second string :";
	cin >> second_string;
	
	string_compare(first_string,second_string);
	return 0;
}


void string_compare(string first_string,string second_string)
{
	int temp_first = 0;
	int temp_second = 0;
	int i = 0;
	for (i = 0; i < first_string.length(); i++)
	{
		temp_first += first_string.at(i);
	}

	for (i = 0; i < second_string.length(); i++)
        {
                temp_second += second_string.at(i);
        }
	
	if (temp_first == temp_second)
	{
		cout << "Yo RK ! One is permutation of other" << endl << endl;
	}
	else {
		cout << "No RK !! No permutation business here ;)" << endl << endl;
	}
}
