import sys
from random import seed, choice
from array_queue import *
from collections import defaultdict
def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' ', grid[i][j], end = '')
        print()
    print()

try:
    seed_arg = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
    
seed(seed_arg)
size = 3
dim = 2 * size + 1
grid = [[0] * dim for _ in range(dim)]
directions = 'NE', 'SE', 'SW', 'NW'

for i in range(dim):
    for j in range(dim):
        grid[i][j] = choice(directions)
print('Here is the grid that has been generated:')
display_grid()
dim = 7
corners = (0, 0), (dim - 1, 0), (dim - 1, dim - 1), (0, dim - 1)


from collections import deque
dic = {}
def BFS():
    
    queue = deque([[(3,3)]])
    while queue:
        path = queue.pop()
        
        if path[-1] in corners:
            if path[-1] not in dic:
                dic[path[-1]] = path
                continue
            continue
        
        x = path[-1][0]
        y = path[-1][1]

        if grid[x][y] == 'NE':
            if x - 1 >= 0 and y + 1 < 7 and (x - 1, y + 1) not in path:
                queue.appendleft(path + [(x - 1, y + 1)])
            if y + 1 < 7 and (x, y + 1) not in path:
                queue.appendleft(path + [(x, y + 1)])
            if x - 1 >= 0 and (x - 1, y) not in path:
                queue.appendleft(path + [(x - 1, y)])
        elif grid[x][y] == 'NW':
            if x - 1 >=0 and y - 1 >= 0 and (x - 1, y - 1) not in path:
                queue.appendleft(path + [(x - 1, y - 1)])
            if y - 1 >= 0 and (x, y - 1) not in path:
                queue.appendleft(path + [(x, y - 1)])
            if x - 1 >= 0 and (x - 1, y) not in path:
                queue.appendleft(path + [(x - 1, y)])
        elif grid[x][y] == 'SE':
            if x + 1 < 7 and y + 1 < 7 and (x + 1, y + 1) not in path:
                #print('*')
                queue.appendleft(path + [(x + 1, y + 1)])
            if y + 1 < 7 and (x, y + 1) not in path:
                #print('&')
                queue.appendleft(path + [(x, y + 1)])
            if x + 1 < 7 and (x + 1, y) not in path:
                queue.appendleft(path + [(x + 1, y)])
        elif grid[x][y] == 'SW':
            if x + 1 < 7 and y - 1 >= 0 and (x + 1, y - 1) not in path:
                queue.appendleft(path + [(x + 1, y - 1)])
            if y - 1 >= 0 and (x, y - 1) not in path:
                queue.appendleft(path + [(x, y - 1)])
            if x + 1 < 7 and (x + 1, y) not in path:
                queue.appendleft(path + [(x + 1, y)])

BFS()               
paths = defaultdict(list)              
for i in corners:
    if (i[1], i[0]) in dic:
        for j in dic[(i[1], i[0])]:
            paths[i].append((j[1],j[0]))
        
        
if not paths:
    print('There is no path to any corner')
    sys.exit()
for corner in corners:
    if corner not in paths:
        print(f'There is no path to {corner}')
    else:
        print(f'The preferred path to {corner} is:')
        print('  ', paths[corner])           

    
    

