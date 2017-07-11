#include<iostream>
#include<string>
#include<stdlib.h>
using namespace std;

void is_substring(string str1, string str2);

int main()
{
	string str1 = "waterbottle";
	string str2 = "erwatbottle";
	is_substring(str1,str2);
	return 0;
}

void is_substring(string str1, string str2)
{
	int i = 0;
	int char_sum1 = 0;
	int char_sum2 = 0;
	int index = 0;
	// Check for lengths
	if (str1.length() != str2.length())
	{
		cout << "Strings of Different lengths.Exiting" << endl;		
		exit(1);
	}
	
	//check for characters
	for (i = 0; i < str1.length(); i++)
	{
		cout <<  str1.at(i);
		char_sum1 += str1.at(i);
		char_sum2 += str2.at(i);
	}
	if (char_sum1 != char_sum2)
	{
		cout << "Strings are with different characters. Exiting" << endl;
		exit(1);
	}
	cout << endl;
	
	//Confirmed that its a permuted string. Check for order.
	for (i = 0; i < str1.length(); i++)
	{
		if (str1.at(0) == str2.at(i))
		{
			index = i;
			break;
		}
	}
	cout << "Index : " << index << endl;

	// Checking for rotation ! May need to optimise later !!
	for (i = 0; i < str1.length(); i++)
	{
		if (str1.at(i) != str2.at(index))
		{
			cout << "Not a rotated string" << endl;
			exit(1);
		}
		index++;
		if (index > (str1.length()-1) && i < str1.length()) 
		{
			index = 0;
		}
	}
	
	cout << "Yo ravi !! It's a Rotated string" << endl;
}
	
