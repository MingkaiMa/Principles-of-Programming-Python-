# Prompts the user for an integer N and finds all perfect numbers up to N.
# Quadratic complexity, can deal with small values only.


import sys


try:
    N = int(input('Input an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


def is_perfect(n):
    L = []
    for i in range(1,n):
        if n % i == 0:
            L.append(i)
    if sum(L) == n:
        return True
    else:
        return False
    
for i in range(2, N+1):
    if is_perfect(i):
        print(f'{i} is a perfect number.')


   
