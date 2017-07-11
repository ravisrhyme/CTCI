#include<iostream>
using namespace std;

#include<stack>

void sort_stack(stack<int> *s1, stack<int> *s2)
{
	while(!s1->empty())
	{
		int number = s1->top();
		s1->pop();
		while ((!s2->empty()) && (s2->top() > number))
		{
			s1->push(s2->top());
			s2->pop();
		}
		s2->push(number);
	}

	cout << "Sorted stack is : " << endl << endl;
	while(!s2->empty())
        {
                cout << s2->top() << endl;
                cout << "|" << endl;
                s2->pop();
        }


	return;
}

int main()
{
	stack<int> s1;
	stack<int> s2;
	s1.push(10);
	s1.push(1);
	s1.push(2);

	
	/*while(!s1.empty())
	{
		cout << s1.top() << endl;
		cout << "|" << endl;
		s1.pop();	
	}*/
	
	sort_stack(&s1,&s2);
	while(!s2.empty())
        {
                cout << s2.top() << endl;
                cout << "|" << endl;
                s2.pop();
        }
	return 0;
}
