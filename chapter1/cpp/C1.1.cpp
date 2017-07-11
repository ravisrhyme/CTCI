/*******************************************************************************
*                                                                              *
* File : C1.1.cpp                                                              *
*                                                                              *
* Author: Ravi Kiran Chadalawada                                               *
*                                                                              *
* Description: This file has the solution for the 1st problem of chapter-1 of  *
* Cracking the coding interview                                                *
*                                                                              *
* Problem Statement : Implement an algorithm to determine if a string has all  *
                      unique characters                                        *
*                                                                              *
*******************************************************************************/

#include<iostream>
#include<string>
using namespace std;

int uniqueness_of_string(string input_string);

int main()
{
        string input_string;
	int unique = 0;
	cout << "Enter input string:";
	cin >> input_string;
	unique = uniqueness_of_string(input_string);
	if (unique == 1)
	{
		cout << "Yo Ravi !! String is unique" << endl;
	}
	else
	{
		cout << "No Ravi !! String is not unique. Good luck next time!";
                cout << endl;
	}
	return 0;
}

/*******************************************************************************
* Functionality: Determines the uniqueness of a string                         *
* Input        : An ascii string                                               *
* Output       : 0 or 1                                                        *
* caveat       : Works only for lowercase for now :P                           *
* To do        : using maps instead of normal arrays                           *
********************************************************************************/

int uniqueness_of_string(string input_string)
{
	int alphabets[26] = { };
	int i = 0;
	for (i = 0; i < input_string.length(); i++)
	{
		if (alphabets[(input_string.at(i)) - 97] == 0)
		{
			alphabets[input_string[i] - 97]++;
		}
		else 
		{
			return 0;
		}
	}
	return 1;
}
