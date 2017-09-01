# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out".
#
# Written by Mingkai Ma and Eric Martin for COMP9021


from random import seed, randrange
import sys
from collections import defaultdict

dim = 10

def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' 1', end = '') if grid[i][j] else print(' 0', end = '')
        print()
    print()

def colour_shapes():
    colour = 1
    for i in range(0, dim):
        for j in range(0, dim):
            if not grid[i][j]:
                continue
            if grid[i][j] != 1:
                continue
            colour = colour + 1
            find_adjacent(i,j,colour)
            
def find_adjacent(i,j,colour):
    grid[i][j] = colour
    if j + 1 < 10:
        if grid[i][j + 1] and grid[i][j + 1] != colour:
            grid[i][j + 1] = colour
            find_adjacent(i,j + 1,colour)
    if j - 1 >= 0:
        if grid[i][j - 1] and grid[i][j - 1] != colour:
            grid[i][j - 1] = colour
            find_adjacent(i,j - 1,colour)
    if i + 1 < 10:
        if grid[i + 1][j] and grid[i + 1][j] != colour:
            grid[i + 1][j] = colour
            find_adjacent(i + 1,j,colour)
    if i - 1 >= 0:
        if grid[i - 1][j] and grid[i - 1][j] != colour:
            grid[i - 1][j] = colour
            find_adjacent(i - 1,j,colour)
    return None

def nb_of_non_zero_neig(i,j):
    n = 4
    if i - 1 >= 0:
        if grid[i - 1][j] == 0:
            n = n - 1
    else:
        n = n - 1
    if i + 1 < 10:
        if grid[i + 1][j] == 0:
            n = n - 1
    else:
        n = n - 1
    if j + 1 < 10:
        if grid[i][j + 1] == 0:
            n = n - 1
    else:
        n = n - 1
    if j - 1 >= 0:
        if grid[i][j - 1] == 0:
            n = n - 1
    else:
        n = n - 1
    return n
        

try:
    for_seed, n = [int(i) for i in
                        input('Enter two integers, the second one being strictly positive: ').split()]
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randrange(n) != 0 for _ in range(dim)] for _ in range(dim)]
                

print('Here is the grid that has been generated:')
display_grid()
colour_shapes()
L = []
dic = defaultdict(list)
x = -1
for i in range(0, dim):
    for j in range(0, dim):
        if grid[i][j]:
            if x != grid[i][j]:
                x = grid[i][j]
                if x not in L:
                    L.append(x)
                    
for i in range(0, dim):
    for j in range(0, dim):
        if grid[i][j] in L:
            dic[grid[i][j]].append(nb_of_non_zero_neig(i,j))
 
nb_of_shapes = 0
for i in dic:
    if dic[i].count(1) > nb_of_shapes:
        nb_of_shapes = dic[i].count(1)

if nb_of_shapes == 0:
    for i in dic:
        if dic[i].count(0) > nb_of_shapes:
            nb_of_shapes = dic[i].count(0)

print(f'The maximum number of spikes of some shape is equal to {nb_of_shapes}')


