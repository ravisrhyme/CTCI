"""
Prefix to Postfix conversion and vice-versa.
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = [""]
__status__  = "Prototype"


def prefix_to_postfix(expression):

    """ Converts prefix to postfix expression
    """
    stack = []
    operators = ['+','-','*','/']

    for index in range(len(expression)-1,-1,-1):
        if expression[index] in operators:
            first_operand = stack.pop()
            second_operand = stack.pop()
            new_string = first_operand + second_operand + expression[index] 
            stack.append(new_string)
        else:
            stack.append(expression[index])

    return stack.pop()

def postfix_to_prefix(expression):
    """ Converts postfix to prefix notation
    """
    stack = []
    operators = ['+','-','*','/']

    for index in range(0,len(expression)):
        if expression[index] in operators:
            first_operand = stack.pop()
            second_operand = stack.pop()
            new_string = expression[index] + second_operand + first_operand
            stack.append(new_string)
        else:
            stack.append(expression[index])

    return stack.pop()


if __name__=='__main__':

    expression = '++A*BCD'
    postfix = prefix_to_postfix(expression)
    prefix  = postfix_to_prefix(postfix)

    print(expression)
    print(prefix)
    print(postfix)
