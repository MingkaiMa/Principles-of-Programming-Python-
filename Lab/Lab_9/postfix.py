import re
from operator import add, sub, mul, truediv

from array_stack import ArrayStack, EmptyStackError


def evaluate(expression):
    if any(not(c.isdigit() or c.isspace() or c in '()[]{}+-*/') for c in expression):
        return
    tokens = re.compile('(\d+|\(|\)|\[|\]|{|}|\+|-|\*|/)').findall(expression)
    try:
        value = evalueate_expression(tokens)
        return value
    except ZeroDivisionError:
        return

def evalueate_expression(tokens):
    parentheses = {')':'(', '}':'{', ']':'['}
    stack = ArrayStack()
    for token in tokens:
        try:
            token = (int(token))
        except ValueError:
            pass

        if token not in parentheses:
            stack.push(token)
        else:
            try:
                arg_2 = stack.pop()
                operator = stack.pop()
                arg_1 = stack.pop()
                opening_group_symbol = stack.pop()
                if parentheses[token] != opening_group_symbol:
                    return
                stack.push({'+':add, '-':sub, '*':mul, '/':truediv}[operator](arg_1, arg_2))
            except EmptyStackError:
                return
    if stack.is_empty():
        return
    value = stack.pop()
    if not stack.is_empty():
        return
    return value



    
