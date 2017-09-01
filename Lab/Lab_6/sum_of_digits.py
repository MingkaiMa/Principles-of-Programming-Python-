import sys
import itertools

try:
    arg_for_available = input('Input a number that we will use as available digits: ')
except ValueError:
    print('Incorrect, giving up.')
    sys.exit()

try:
    arg_for_sum = int(input('Input a number that represents the desired sum: '))
except ValueError:
    print('Incorrect, giving up.')
    sys.exit()


L = [int(i) for i in arg_for_available]

s = arg_for_sum

nb_of_solu = 0

R = []
T = []
for i in range(2,len(L) + 1):
    R.append(list(itertools.combinations(L,i)))


for i in range(0,len(R)):
    for j in R[i]:
        T.append(list(j))
        
for i in range(0,len(T)):
    if s == sum(T[i]):
        nb_of_solu += 1


for i in L:
    if i == s:
        nb_of_solu += 1

if nb_of_solu == 1:
    print(f'There is a unique solution.')
else:
    if nb_of_solu != 0:
        print(f'There is {nb_of_solu} solutions.')
    else:
        print(f'There is no solution.')

