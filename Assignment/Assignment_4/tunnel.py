import os.path
import sys
import os
from collections import deque

file_name = input('Please enter the name of the file you want to get data from: ')
if not os.path.isfile(file_name):
    print('Sorry, there is no such file.')
    sys.exit()
    
L = []
with open(file_name) as file:
    for line in file:
        if line != '\n':
            L.append(line.strip('\n'))

if len(L) != 2:
    print('Sorry, input file does not store valid data.')
    sys.exit()

R = []
T = []

R = list(str(L[0]).split())
T = list(str(L[1]).split())

if len(R) != len(T):
    print('Sorry, input file does not store valid data.')
    sys.exit()
if len(R) < 2 or len(T) < 2:
    print('Sorry, input file does not store valid data.')
    sys.exit()

for i in range(0,len(R)):
    try:
        R[i] = int(R[i])
    except:
        print('Sorry, input file does not store valid data.')
        sys.exit()
        break
    
for i in range(0,len(T)):
    try:
        T[i] = int(T[i])
    except:
        print('Sorry, input file does not store valid data.')
        sys.exit()
        break

        
for i in range(0,len(R)):
    if R[i] <= T[i]:
        print('Sorry, input file does not store valid data.')
        sys.exit()

c = deque()
f = deque()

current_distance = 0
max_distance = 0
pop_number = 0
min_element = float('inf')
max_element = float('-inf')
for i in range(0,len(R)):
    c.append(R[i])
    f.append(T[i])
    

    if R[i] < min_element:
        min_element = R[i]
    if T[i] > max_element:
        max_element = T[i]
    
    if min_element > max_element:
        current_distance = len(c)
        if pop_number == 0:
            max_west_distance = len(c)
    else:
        c.popleft()
        f.popleft()
        min_element = min(c)
        max_element = max(f)
        pop_number += 1
 
        if max_distance < current_distance:
            max_distance = current_distance
    if max_distance < current_distance:
        max_distance = current_distance

print(f'From the west, one can into the tunnel over a distance of {max_west_distance}')
print(f'Inside the tunnel, one can into the tunnel over a maximum distance of {max_distance}')



