
/*
Write a function that takes a string of arithmetic equation below and returns
a scalar as the evaluation of the equation arithmetic supports 4 operators. i.e 
+,*,&,|, where + and * are defined as usual, & and | are defined as pair wise 
max,min respectively. A & B = fmax(A,B), A | B = fmin(A,B)

priority : &, | higher than * higher than |

Your algorithm should handle space,decimal and negative numbers. For any invalid
input, output should be zero.

Author             : Ravi Kiran Chadalawada

Command to compile : g++ autox.cpp -std=c++11
*/

#include<iostream>
#include<stack>
#include<unordered_map>
#include<algorithm>
#include<cstdlib>
#include<string>
#include<sstream>
using namespace std;


unordered_map<char,int> precedence;

float calculate(float m, float n, char symbol)
{
	if (symbol == '*')
	{ return m * n;}

	else if (symbol == '+')
	{
		return m + n;
	}

	else if (symbol == '|')
	{
		return min(m,n);
	}

	else if (symbol == '&')
	{ return max(m,n);}

	else
	{ return 0.0; }
}

float string_to_float(string str)
{
    float temp = atof(str.c_str());
	return temp;
}

bool is_valid_number(string number)
{

	int length = number.length();
	
    for (int i = 0; i < length; i++)
    {
        if ((i == 0) && (number[i] == '-') && (length > 1)) {
            continue;
        }
        else if (number[i] - '0' >= 0 && number[i] - '0' <=9) {
            continue;
        }
        else if (number[i] == '.' && (length > 1)) {
            continue;
        }
        else{
            return false;
        }

    }
    return true;

}

bool validate_string(string input) 
{
	int symbols = 0;
    int numbers = 0;
    int length = input.length();
    bool operand = true;
    int i = 0;
    
    while (i < length)
    {
        if (input[i] == ' ')
        {
            i += 1;
            continue;
        }
        else if((input[i] - '0' >= 0 && input[i] - '0' <=9) || (input[i] == '-') || (input[i] == '.'))
        {
            string temp;
            temp = input[i];
            i += 1;
            while ((input[i] - '0' >= 0 && input[i] - '0' <=9) || (input[i] == '.'))
            {
                temp.append(1,input[i]);
                i += 1;
            }
            if (is_valid_number(temp) && (operand == true))
            {
                numbers += 1;
                operand = false;
            }
            else {
                return false;
            }
            
        }
        else if ((input[i] == '+' || input[i] == '*' || input[i] == '|' || input[i] == '&') && (operand == false))
        {
            symbols += 1;
            operand = true;
            i += 1;    
        }
        else
        {
            return false;
        }
                
    }
    if (numbers == symbols + 1) {
        return true;
    }
    return false;
}

float evaluate(string input)
{
	int length = input.length();
	precedence['|'] = 1;
	precedence['&'] = 1;
	precedence['*'] = 2;
	precedence['+'] = 3;


	// Validate the string first
	if (!validate_string(input))
	{
		cout << "invalid_string" << endl;
		return 0;
	}
	
	stack<char> symbol_stack;
	stack<float> number_stack;

	int i = 0;
	while (i < length)
	{
		// Ignoring white space
		if (input[i] == ' ')
		{
			i += 1;
			continue;
		}

		// Pushing numbers to stack
        else if((input[i] - '0' >= 0 && input[i] - '0' <=9) || (input[i] == '-') || (input[i] == '.'))
        {
            string temp;
            temp = input[i];
            i += 1;
            while ((input[i] - '0' >= 0 && input[i] - '0' <=9) || (input[i] == '.'))
            {
                temp.append(1,input[i]);
                i += 1;
            }
            //cout << temp << endl;
            float number = string_to_float(temp);
            //cout << number << endl;
            number_stack.push(number);
        }

		// Pushing operators to stack
		else
		{
			unordered_map<char,int>::const_iterator check = precedence.find (input[i]);
			if ( check == precedence.end() )
			{

    			cout << "operator not found" << endl;
				return 0;
			}
			else
			{
				int current_precedence = check->second;
				while(!symbol_stack.empty())
				{
					char symbol = symbol_stack.top();
					if (current_precedence >= precedence.at(symbol))
					{
						float m = number_stack.top();
						number_stack.pop();
						
						float n = number_stack.top();
						number_stack.pop();
						
						float result = calculate(m,n,symbol);
						number_stack.push(result);

						symbol_stack.pop();

					}
					else 
					{
						break;
					}

				}
				symbol_stack.push(input[i]);
				i += 1;
				//cout << check->first << " is " << check->second << endl;
			}
		}
	}
	while(!symbol_stack.empty())
	{
		char symbol = symbol_stack.top();
        
		float m = number_stack.top();
        number_stack.pop();

        float n = number_stack.top();
        number_stack.pop();

        float result = calculate(m,n,symbol);
        number_stack.push(result);

        symbol_stack.pop();

	}
	
	return number_stack.top();
}

int main()
{
	string input = "1.2 | 2.33";
	cout << evaluate(input) << endl;
	return 0;
}

