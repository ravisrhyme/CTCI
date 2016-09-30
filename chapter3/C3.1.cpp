/*******************************************************************************
*                                                                              *
* File : C3.1.cpp                                                              *
*                                                                              *
* Author: Ravi Kiran Chadalawada                                               *
*                                                                              *
* Description: This file has the solution for the 1st problem of chapter-3 of  *
* Cracking the coding interview                                                *
*                                                                              *
* Problem Statement : Describe how you could use a single array to implement   *
                      three stacks                                             *
*                                                                              *
*******************************************************************************/

#include<iostream>
using namespace std;

#define STACK_SIZE 4

void push(int stack_number, int data);
void pop(int stack_number);

int array[3 * STACK_SIZE]; // Assuming static array of fixed size for each stack
int stack_top[3] ; // Stores the index of top in all three arrays.


int main()
{
	/* As per the logic, stack_number starts from Zero and not one !! Most 
	   important note to take care while calling push and pop" */
	array[3 * STACK_SIZE]; // Assuming static array of fixed size for each stack
	stack_top[0] = 0; // Stores the index of top in all three arrays.
	stack_top[1] = 4;
	stack_top[2] = 8;
	push(0,4);
	push(1,5);
	push(2,6);
	pop(0);
	pop(1);
	pop(2);
	pop(2);
	return 0;
}

void push(int stack_number, int data)
{
	int top_index = stack_top[stack_number];
	int start_index = stack_number * STACK_SIZE;
	int end_index = start_index + STACK_SIZE-1;

	//Boundary Error checking
	if (top_index < start_index || top_index > end_index)
	{
		cout << "Something is wrong Ravi. Check logic !!";
	}
	else 
	{
		top_index++;
		if (top_index < start_index || top_index > end_index)
        	{
                	cout << " Stack is full. Can't add anything new";
			top_index--;
        	}
		else 
		{
			array[top_index] = data;
			stack_top[stack_number] = top_index;
		}

	}

}
void pop(int stack_number)
{
	int top_index = stack_top[stack_number];
        int start_index = stack_number * STACK_SIZE;
        int end_index = start_index + STACK_SIZE-1;

	// Boundary Error checking
	if (top_index < start_index || top_index > end_index)
        {
                cout << "Something is wrong Ravi. Check logic !!";
        }

	if (array[top_index] == 0)
	{
		cout << "stack " << stack_number <<" is empty!!" << endl;
		return;
	}
	cout << array[top_index] << endl;
	array[top_index] = 0;
	
	top_index--;
	if (top_index < start_index)
	{
		top_index = start_index;
	}
	stack_top[stack_number] = top_index;
}

