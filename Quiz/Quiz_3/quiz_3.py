# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the number of
# parallelograms with horizontal sides. 
#
# Written by Mingkai Ma and Eric Martin for COMP9021

from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' 1', end = '') if grid[i][j] else print(' 0', end = '')
        print()
    print()


def size_of_largest_parallelogram():

    max_size = 0
    size = 0
    for i in range(0,dim-1):
        for j1 in range(0,dim-1):
            if(not grid[i][j1]):
                continue
            for j2 in range(j1+1,dim):
                if (not grid[i][j2]):
                    break
                size = size_of_largest_parallelogram_straight(i,j1,j2)
                if size > max_size:
                    max_size = size
                size = size_of_largest_parallelogram_left(i,j1,j2)
                if size > max_size:
                    max_size = size
                size = size_of_largest_parallelogram_right(i,j1,j2)
                if size > max_size:
                    max_size = size


    return max_size



def size_of_largest_parallelogram_straight(i1,j1,j2):
    length = j2 - j1 + 1
    i2 = i1 
    good_flag = True
    while ( good_flag and i2 < dim):
        i2 += 1
        if i2 < dim:
            for j in range(j1,j2+1):
                if not grid[i2][j]:
                    good_flag = False
                    break
        else:
            break
    if i2 == i1 + 1:
        return 0
    return (i2 - i1) * length

def size_of_largest_parallelogram_left(i1,j1,j2):
    length = j2 - j1 + 1
    i2 = i1
    good_flag = True
    while ( good_flag and i2 < dim and j1 >=0):
        i2 += 1
        j1 -= 1
        j2 -= 1
        if i2 <dim and j1 >= 0:
            for j in range(j1,j2+1):
                if not grid[i2][j]:
                    good_flag = False
                    break
        else:
            break
    if i2 == i1 + 1:
        return 0
    return (i2 - i1) * length

def size_of_largest_parallelogram_right(i1,j1,j2):
    length = j2 - j1 + 1
    i2 = i1
    good_flag = True
    while ( good_flag and i2 < dim and j2 < dim):
        j2 += 1
        j1 += 1
        j2 += 1
        if i2 < dim and j2 < dim:
            for j in range(j1,j2+1):
                if not grid[i2][j]:
                    good_flag = False
                    break
        else:
            break
    if i2 == i1 + 1:
        return 0
    return (i2 - i1) * length

try:
    for_seed, n = [int(i) for i in
                           input('Enter two integers, the second one being strictly positive: ').split()]
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randrange(n) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_parallelogram()
if size:
    print('The largest parallelogram with horizontal sides has a size of', size, end = '.\n')
else:
    print('There is no parallelogram with horizontal sides.')
            




