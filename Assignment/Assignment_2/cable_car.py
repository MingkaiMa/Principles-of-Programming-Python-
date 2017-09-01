import os.path
import sys
import os

from random import randint

file_name = input('Please enter the name of the file you want to get data from: ')
if not os.path.isfile(file_name):
    print('Sorry, there is no such file.')
    sys.exit()
L = []
with open(file_name) as file:
    for line in file:
        for word in line.split():
            L.append(word)

for i in range(0,len(L)):
    try:
        L[i] = int(L[i])
    except:
        print('Sorry, input file does not store valid data.')
        sys.exit()
        break

if len(L) == 0 or len(L) == 1:
    print('Sorry, input file does not store valid data.')
    sys.exit()
else:
    if not all(x<y for x,y in zip(L,L[1:])):
        print('Sorry, input file does not store valid data.')
        sys.exit()
    else:
        if min(L) <= 0:
            print('Sorry, input file does not store valid data.')
            sys.exit()

if len(L) == 2:
    print('The ride is perfect!')
    print(f'The longest good ride has a length of: {len(L)-1}')
    print('The minimal number of pillars to remove to build a perfect ride from the rest is: 0')
    sys.exit()

R = []

for i in range(1,len(L)):
    R.append(L[i]-L[i-1])


R_1 = R[:]
R_1.sort()

if min(R_1) == max(R_1):
    print('The ride is perfect!')
    print(f'The longest good ride has a length of: {len(L)-1}')
    print('The minimal number of pillars to remove to build a perfect ride from the rest is: 0')
    sys.exit()
else:
    print('The ride could be better...')


longest_length = 1
current_length = 1
for i in range(1,len(R)):
    if R[i] == R[i-1]:
        current_length += 1
    else:
        if current_length > longest_length:
            longest_length = current_length
            current_length =1
        else:
            current_length = 1

print(f'The longest good ride has a length of: {longest_length}')

def length_of_longest_ap(L,n):
    if n <= 2:
        return n

    R= [[0] * n for _ in range(n)]

    result = 2

    for i in range(0,n):
        R[i][n-1] = 2

    for j in range(n - 2, 0, -1):
        i = j - 1
        k = j + 1
        while(i >= 0 and k <= n - 1):
            if(L[i] + L[k] < 2 * L[j]):
                k += 1
            elif L[i] + L[k] > 2 * L[j]:               
                R[i][j] = 2
                i -= 1
            else:
                R[i][j] = R[j][k] + 1

                result = max(result,R[i][j])
                i -= 1
                k += 1


        while(i >= 0):
            R[i][j] = 2
            i -= 1
  
    return result

print(f'The minimal number of pillars to remove to build a perfect ride from the rest is: {len(L)-length_of_longest_ap(L,len(L))}')

             

