#include<iostream>
using namespace std;


class node 
{
public:
	node *previous;
	int data;
	node *next;
};


class linked_list
{

private:
	node *head;
public:	
	linked_list();
	bool insert_node(node* new_node);
	bool insert_node_at(node* new_node,node* position);
	bool delete_node (node* ptr);
	void display_list(node* head);
};

// Constructor for linkedlist ! Writing after a longtime huh ! C'mon Ravi ! :D
linked_list::linked_list()
{
	head = NULL;
}
node* linked_list::get_next(node *node)
{
	return node->next;
}

bool linked_list::insert_node(node *new_node, linked_list list)
{
	if (list.head == NULL)
	{
		list.head = new_node;
	}
	else {
		node* i;
		for (i = head; i != NULL; i = get_next(i))
		{
			
		}
	}
}

int main()
{
	cout << "Linked list " << endl;
	linked_list* list = new linked_list;
	node node1 = new node;
	insert_node (node1;)
}
