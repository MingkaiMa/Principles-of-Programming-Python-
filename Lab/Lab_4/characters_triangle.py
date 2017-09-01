from collections import deque
from copy import copy
import sys
a = deque()

def populate_deque():
    for i in range(65,91):
        a.append(i)
populate_deque()
b = copy(a)
c = copy(b)
s = ''
def triangle(n):
    global s
    L = [[0] * n for _ in range(10)]
    m = 1
    while(m <= n):
        print(' ' * (n-m),end = '')

        for i in range(0,m):
    
            if len(b) == 0:
                for i in range(65,91):
                    b.append(i)
            if len(c) == 0:
                for i in range(65,91):
                    c.append(i)
            s = s + chr(c.popleft())

            print(chr(b.popleft()),end='')
        print(s[::-1][1:],end='')
        print()
        m += 1
        s = ''

try:
    a = input('Enter strictly positive number: ')
except ValueError:
    print('Wrong input,giving up...')
    sys.exit()

try:
    a = int(a)
    if a <= 0:
        raise ValueError
except:
    print('Wrong input,giving up...')
    sys.exit

triangle(a)
    










    
