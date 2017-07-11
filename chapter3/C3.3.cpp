

#include<iostream>
#include<stack>
#include<vector>
using namespace std;

#define STACK_SIZE 2
#define STACK_EMPTY -1000000
#define BAD_INDEX -1000001
class set_of_stacks
{
	public:
	vector<stack<int>* > stack_array; // Empty vector of stack objects
	//stack<int> s;
	void push(int number);
	int pop();
	int pop_at(int index);
};

void set_of_stacks::push(int number)
{
	// If vector is empty create a new stack. hold its address in vector
	// and an element to stack
	if (0 == stack_array.size())
	{
		stack<int> *new_stack = new stack<int>;
		stack_array.push_back(new_stack); // saving stack object to a vector
		new_stack->push(number); // pushing element to stack
		cout << "Pushed element "<< number <<" to new stack "<< new_stack << endl;
	}

	//else get the last object from the vector.
	// If it is not full add number to stack.
	// Else create a new stack, add its object address to vector and 
	// add an element
	else {
		int size = stack_array.size();
		stack<int> *temp = stack_array[size-1];
		if (temp->size() < STACK_SIZE)
		{
			temp->push(number);
			cout << "Pushed element "<< number <<" to existing stack "<< temp << endl;
		}
		else
		{
			stack<int> *new_stack = new stack<int>;
                	stack_array.push_back(new_stack); // saving stack objectto a vector
            		new_stack->push(number); // pushing element to stack
			cout << "Pushed element "<< number <<" to new stack "<< new_stack << endl;

		}
	}
}

int set_of_stacks::pop()
{
	if (0 == stack_array.size())
	{
		cout << "Stack is empty Ravi !!" << endl;
		return STACK_EMPTY;
	}
	else
	{
		int size = stack_array.size();
                stack<int> *temp = stack_array[size-1];
		int number = temp->top();
		temp->pop();
		cout << "Popped " << number << " from stack " << temp << endl;
		
		if (0 == temp->size())
		{
			stack_array.pop_back();
			cout << "stack " << temp << " empty.Deleting it." << endl;
			delete temp;
		}
		return number;
	}
}
int set_of_stacks::pop_at(int index)
{
	if (index < 0 || index >= stack_array.size())
	{
		cout << "Bad index!!" << endl;
		return BAD_INDEX;
	}
	else
	{
		stack<int> *temp = stack_array[index];
		int number = temp->top();
		temp->pop();
		cout << "Popped " << number << " from stack " << temp <<" at index "<< index << endl;
		if (0 == temp->size())
                {
                        stack_array.erase(stack_array.begin()+index);
                        cout << "stack " << temp << " empty.Deleting it." << endl;
                        delete temp;
                }
                return number;

	}
}
int main()
{
	set_of_stacks s;
	s.push(10);
	s.push(11);
	s.push(12);
	s.push(13);
	s.push(14);
	s.push(15);
	s.pop_at(1);
	s.pop();
	s.pop();
	s.pop();
	s.pop();
	s.pop();
	s.pop();	
	return 0;
}
