
import os.path
import sys
import os

file_name = input('Enter the name of a file: ')
if not os.path.isfile(file_name):
    print('Sorry, there is no such file.')
    sys.exit()
    
L = []
with open(file_name) as file:
    for line in file:
        for word in line.split():
            for i in word:
                if i.isdigit():
                    L.append(int(i))

if len(L) == 0:
    print('There is no digit in this file.')
    sys.exit()
    
width = len(str(max(L)))

L.sort()

R = dict((i,L.count(i)) for i in L)
##D = R.keys()
##for i in range(0,len(R)):
##    print('Digits:',end='')
##    print()

print('Digits:',end='')
for i in R:
    print(f'{i:5d}',end='')

print()    
print('Count:',end=' ')
for i in R:
    print(f'{R[i]:5d}',end='')


    
    
                    
    
