# Uses the Stack interface to evaluate an arithmetic expression
# written in postfix and built from natural numbers using
# the binary +, -, * and / operators.             
#
# Written by Mingkai Ma and Eric Martin for COMP9021


import re
from operator import add, sub, mul, truediv

from array_stack import ArrayStack, EmptyStackError
from binary_tree import *

def parse_tree(expression):
    if any(not (c.isdigit() or c.isspace() or c in '+-*/(){}[]') for c in expression):
        return
    # Tokens can be natural numbers, +, -, *, and /
    tokens = re.compile('(\d+|\+|-|\*|/|\(|\)|\{|\}|\[|\])').findall(expression)
    try:
        value = evaluate_expression(tokens)
        return value
    except ZeroDivisionError:
        return


def evaluate_expression(tokens):
    stack_number = ArrayStack()
    stack_operator = ArrayStack()
    stack_pa = ArrayStack()
    for token in tokens:
        if token.isdigit():
            stack_number.push(BinaryTree(token))
        else:
            if token in '({[':
                stack_pa.push(token)
            elif token in '+-*/':
                stack_operator.push(BinaryTree(token))
                
            else:
                if stack_operator.is_empty():
                    return
                stack_pa.pop()
                arg_2 = stack_number.pop()
                arg_1 = stack_number.pop()
                tree = stack_operator.pop()
                tree.left_node = arg_1
                tree.right_node = arg_2
                stack_number.push(tree)
    
                
    if stack_number.is_empty():
        return
    value = stack_number.pop()
    if not stack_number.is_empty():
        return
    if not stack_pa.is_empty():
        return
    if not stack_operator.is_empty():
        return
    return value
        
        

        


