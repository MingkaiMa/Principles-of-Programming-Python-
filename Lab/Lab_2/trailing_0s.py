# Prompts the user to input an integer N at least equal to 10 and computes N!
# in three different ways.


import sys
from math import factorial


def first_computation(x):
    t = 0
    while True:
        if x % 10 == 0:
            t += 1
            x = x//10
        else:
            break
    return t
        
    

def second_computation(x):
    t = 0
    for i in range(-1,-len(str(x))-1,-1):
        if str(x)[i] == '0':
            t += 1
        else:
            break
    return t


def third_computation(x):
    t = 0
    e = 1
    while True:
        if x//(5**e) != 0:
            t += x//(5**e)
            e += 1
        else:
            break
    return t
        

try:
    the_input = int(input('Input a nonnegative integer: '))
    if the_input < 5 :
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

the_input_factorial = factorial(the_input)
print(f'Computing the number of trailing 0s in {the_input}! by dividing by 10 for long enough:',
      first_computation(the_input_factorial))
print(f'Computing the number of trailing 0s in {the_input}! by converting it into a string:',
      second_computation(str(the_input_factorial)))
print(f'Computing the number of trailing 0s in {the_input}! the smart way:',
      third_computation(the_input))

    
    
    
