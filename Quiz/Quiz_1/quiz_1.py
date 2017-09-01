# Generates a list L of random nonnegative integers at most equal to some value
# input by the user, and of length also input by the user, and outputs a list
# consisting of the longest streak of consecutive occurrences of the same value in L,
# possibly looping around (as if the list was a ring). In the case multiple value
# have the longest streak of consecutive occurrences in L, then the smallest value is chosen.
#
# Written by Mingkai Ma and Eric Martin for COMP9021
import sys
from random import seed, randint

try:
    arg_for_seed, length, max_value = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
print('\nThe generated list is:')
print('  ', L)

R = L
# Insert your code here
longest_length = 1
current_length = 1
current_value = 0
longest_value = 0

for i in range(-len(R)+1,len(R)):
    if R[i] == R [i-1]:
        current_length += 1
        current_value = R[i]
    else:
        if current_length == longest_length:
            if current_value < longest_value:
                longest_value = current_value
                current_value = 0
                current_length = 1
            else:
                current_length = 1
                current_value = 0    
        if current_length > longest_length:
            longest_length = current_length
            current_length = 1
            longest_value = current_value
            current_value = 0
        current_length = 1
        current_value = 0

L.sort()
if len(L) == 0 or len(L) == 1:
    R = L
else:
    if L[0] == L[len(L)-1]:
        R = L
    else:
        R = longest_length * [longest_value]

print('\nThe longest streak of the same value is:')
print('  ', R)

