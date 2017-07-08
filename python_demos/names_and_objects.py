
"""
A test program to understand the object,variable mapping in python.

Unike c/c++ its only a name-object binding and not an operation that writes in
to memory.

Also assigment of name to another name doesn't create a new object.
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["https://jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/"]
__status__  = "Prototype"


some_guy = 'Ravi'

first_names = []
first_names.append(some_guy)

another_list_of_names = first_names
another_list_of_names.append('sindhu')
some_guy = 'kiran'

print (some_guy, first_names, another_list_of_names)
