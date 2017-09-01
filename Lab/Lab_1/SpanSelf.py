from random import *
arg_for_seed = input('Input a seed for the random number generator: ')
try:
    arg_for_seed = int(arg_for_seed)
except ValueError:
    print('Input is not an integer,giving up.')
    sys.exit()

nb_of_elements = input('How many elements do you want to generate?')
try:
    nb_of_elements = int(nb_of_elements)
except ValueError:
    print('Input is not an integer,giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive,giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0,99) for _ in range(nb_of_elements)]


print('\nThe List is:',L)

max_value = 0
min_value = 99

for i in L:
    if i < min_value:
        min_value = i

for i in L:
    if i > max_value:
        max_value = i

print('The maximum difference between largest and smallest values in this list is: %d'%(max_value-min_value))
print('Confirming with builtin operations: %d'%(max(L)-min(L)))
