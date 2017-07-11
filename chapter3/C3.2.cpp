/*******************************************************************************
*                                                                              *
* File : C3.2.cpp                                                              *
*                                                                              *
* Author: Ravi Kiran Chadalawada                                               *
*                                                                              *
* Description: This file has the solution for the 2nd problem of chapter-3 of  *
* Cracking the coding interview                                                *
*                                                                              *
* Problem Statement : Design a stack which, in addition to push and pop, also  *
                      has a function min which returns the minimum element.    *
*                     push,pop and min should operate in O(1) time             *
*******************************************************************************/


#include<iostream>
using namespace std;


#define STACK_EMPTY -1;
#define STACK_FULL 500;


class node
{
	public:
	int number;
	int local_min;
	node *next;
};

class stack
{
	public:
	node* top;
	int min_value;

	void init();
	void push(int number);
	int pop();
	int min();
};

void stack::init()
{
	top = NULL;
	min_value = 0;
	return;
}

// As stack is being implemented with nodes, not checking for STACK_FULL.
void stack::push(int number)
{
	if (NULL == top)
	{
		//create new node and start the stack
		node* new_node = new node; // Not checking for any NO_MEM error for now.

		new_node->number = number;
		new_node->next = NULL;
		new_node->local_min = number;

		top = new_node;
		min_value = number;
	}
	else 
	{
		//create new node and append the stack

		node* new_node = new node; // Not chekcing for any error for now

		new_node->number = number;
                new_node->next = top;

		// Updation of minimum element
		if (number < min_value)
		{
                new_node->local_min = number;
		min_value = number;
		}
		else
		{
			new_node->local_min = min_value;
		}
		top = new_node;

	}
	 cout << "Pushed " << number << " on to Stack" << endl;
	return;
}
int stack::pop()
{
	if (NULL == top)
	{
		cout << " Stack is Empty";
		return STACK_EMPTY;
	}
	else 
	{
		int temp = top->number;
		node* to_delete = top;

		top = top->next;

		if (temp == min_value)
		{
			min_value = top->local_min;
		} 
		delete to_delete;
		return temp;
	}
}
int stack::min()
{
	return min_value;
}
int main()
{
	stack s1;
	s1.init();
	s1.push(5);
	cout << "Min is " << s1.min() << endl;
	s1.push(4);
	cout << "Min is " << s1.min() << endl;
	s1.push(7);
	cout << "Min is " << s1.min() << endl;
	s1.push(2);
	cout << "Min is " << s1.min() << endl;
	cout << s1.pop() << endl;
	cout << "Min is " << s1.min() << endl;
	
	return 0;
}
