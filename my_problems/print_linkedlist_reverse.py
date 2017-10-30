"""
Printing a singly linkedlist from end
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = [""]
__status__  = "Prototype"


import math

class node():
    def __init__(self,value):
        self.data = value
        self.next = None 


def print_reverse(head):
    """ Prints list in reverse order
    Time Complexity  : O(n)
    Space Complexity : O(n)
    """
    list_items = []
    current_pointer = head

    while current_pointer:
        list_items.append(current_pointer.data)
        current_pointer = current_pointer.next

    for i in range(len(list_items)-1,-1,-1):
        print(list_items[i])


def print_reverse_squareroot(head):
    """
    Time Complexity = O(n*sqrt(n))
    Space Complexity = O(sqrt(n))
    """
    length_of_list = 0
    current_pointer = head
    node_pointers = []

    # Find the length of list
    while current_pointer:
        length_of_list += 1
        current_pointer = current_pointer.next

    #print(length_of_list)

    square_root = int(math.sqrt(length_of_list))

    if square_root * square_root == length_of_list:
        number_of_pointers = square_root
    else:
        number_of_pointers = square_root + 1

    # Storing sqrt(n) pointers in list
    current_pointer = head
    for i in range(0,length_of_list):
        if i % square_root == 0:
            node_pointers.append(current_pointer)
            #print(current_pointer.data)
        current_pointer = current_pointer.next

    for i in range(len(node_pointers)-1,-1,-1):
        print_reverse_list(node_pointers[i],i,length_of_list,square_root)
        


def print_reverse_list(head,i,length_of_list,block_size):

    current_node = head
    current_node_index = i * block_size
    end_node_index = current_node_index + block_size

    if end_node_index > length_of_list:
        end_node_index = length_of_list

    print_index = end_node_index -1

    for i in range(current_node_index,end_node_index):
        for j in range(current_node_index,end_node_index):
            if j == print_index:
                print(current_node.data)
                break
            current_node = current_node.next
        current_node = head
        print_index -= 1


if __name__=='__main__':

    # Linkedlist to Test
    head = node(1)
    head.next = node(2)
    head.next.next = node(3)
    head.next.next.next = node(4)
    head.next.next.next.next = node(5)
    head.next.next.next.next.next = node(6)
    head.next.next.next.next.next.next = node(7)
    head.next.next.next.next.next.next.next = node(8)
    head.next.next.next.next.next.next.next.next = node(9)
    #print_reverse(head)
    print_reverse_squareroot(head)
