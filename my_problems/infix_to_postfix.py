"""
infix to postfix conversion and vice-versa.
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = [""]
__status__  = "Prototype"

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def infix_to_postfix(expression):

    """ Converts infix to postfix expression
    """
    precedence = {}
    precedence['+'] = 2
    precedence['-'] = 2
    precedence['/'] = 3
    precedence['*'] = 3
    precedence['('] = 1

    operators = ['+','-','*','/','(',')']

    postfix = []
    stack = Stack()
	
    for token in expression:
        if token not in operators:
            postfix.append(token)
        else:
            if token == '(':
                stack.push(token)
            elif token == ')':
                top_element = stack.pop()
                while top_element != '(':
                    postfix.append(top_element)
                    top_element = stack.pop()
            else:
                while (not stack.isEmpty() and precedence[stack.peek()] >= precedence[token]):
                    postfix.append(stack.pop())
                stack.push(token)

    while not stack.isEmpty():
        postfix.append(stack.pop())

    return "".join(postfix)


if __name__=='__main__':

    expression = 'A*B+C*D'
    postfix = infix_to_postfix(expression)

    print(expression)
    print(postfix)
