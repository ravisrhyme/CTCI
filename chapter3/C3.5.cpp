#include<iostream>
#include<stack>
using namespace std;

class my_queue
{
	private:
	stack<int> s1; // Stack to store items as passed in LIFO
	stack<int> s2; // stack to store items for dequeueing
	public:
	void enqueue(int number);
	void dequeue();
};

void my_queue::enqueue(int number)
{
	s1.push(number);
	cout << "Pushed element " << number << " to S1" << endl;
}

void my_queue::dequeue()
{
	if (s1.empty() && s2.empty())
	{
		cout << "No elements in queue." << endl;
		return;
	}
	if (s2.empty())
	{
		//copy all elements in stack s1 to s2
		while (!s1.empty())
		{
			int number = s1.top();
			s1.pop();
			s2.push(number);
			cout << "Popped top element " << number << " from S1 and pushed to S2" << endl;
		}
	}
	cout << "Element is " << s2.top() << endl;
        s2.pop();
        return;
}

int main()
{
	my_queue q;
	q.dequeue();
	q.enqueue(1);
	q.enqueue(2);
	q.enqueue(3);
	q.dequeue();
	q.dequeue();
	q.dequeue();
	return 0;
}
