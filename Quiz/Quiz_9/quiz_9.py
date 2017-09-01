# Prompts the user for a string, checks that it is a corect postfix expression
# built from positive numbers, + and spaces, and if it is,
# outputs a tree representation of the corresponding infix expression.

# Written by Mingkai Ma and Eric Martin for COMP9021


import sys
import re
from operator import add, sub, mul, truediv

from array_stack import *
from binary_tree import *


def store_in_two_stacks(expression):
    stack_1 = ArrayStack()
    stack_2 = ArrayStack()
    if any(not (c.isdigit() or c.isspace() or c in '+') for c in expression):
        return None, None
    tokens = re.compile('(\d+|\+)').findall(expression)
    for token in tokens:
        try:
            if token[0] == '0' and len(token) != 1:
                return None, None
            token = int(token)
            stack_1.push(token)
            stack_2.push(token)
            if token < 0:
                return None, None
        except ValueError:
            try:
                arg_2 = stack_1.pop()
                arg_1 = stack_1.pop()
                stack_1.push({'+':add}[token](arg_1, arg_2))
                stack_2.push(token)
            except EmptyStackError:
                stack_1.push(token)
                return stack_1, stack_2
    return stack_1, stack_2
                
            
def stores_correct_postfix_expression(stack):
    if stack.is_empty():
        return False
    a = stack.pop()
    a = str(a)
    if not a.isdigit():
        return False
    if not stack.is_empty():
        return False
    return True

def transfer_from_stack_to_tree(stack):
    L_1 = []
    L = []
    for i in range(len(stack)):
        L_1.append(stack.pop())
    for i in reversed(L_1):
        L.append(str(i))

    L_tree = []
    for i in L:
        L_tree.append(BinaryTree(i))

    stack = ArrayStack()
    for token in L_tree:
        if token.value.isdigit():
            stack.push(token)
        if token.value == '+':
            tree = token
            tree_right = stack.pop()
            tree_left = stack.pop()
            tree.right_node = tree_left
            tree.left_node = tree_right

            stack.push(tree)

    return stack.pop()
        

    
    

expression = input('Input an expression: ')
if not expression or expression.isspace():
    sys.exit()
stack_1, stack_2 = store_in_two_stacks(expression)
if not stack_1:
    print('Expression not built from nonnegative numbers and +')
else:
    if not stores_correct_postfix_expression(stack_1):
        print('Not a correct postfix expression')
    else:
        tree = transfer_from_stack_to_tree(stack_2)
        tree.print_binary_tree()
        

