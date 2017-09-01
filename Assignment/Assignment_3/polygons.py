import sys
import os
from collections import deque
from collections import defaultdict
from argparse import ArgumentParser
sys.setrecursionlimit(100000)
parser = ArgumentParser()
parser.add_argument('--file', dest = 'file_name', required = True)
parser.add_argument('-print','--print_tex', dest = 'flag',
                    action = 'store_true', required = False)

args = parser.parse_args()

file_name = args.file_name
flag_ = args.flag

R=[]
with open(file_name) as file:            
    lines = (line.rstrip() for line in file)
    lines = (line for line in lines if line)
    for line in lines:
        R.append(line)

L = []
for line in R:
    S = []
    for word in line:
        if word != ' ':
            S.append(word)
    L.append(S)
    
if len(L) == 0:
    print('Incorrect input.')
    sys.exit()
for i in range(len(L)):
    for j in range(len(L[i])):
        L[i][j] = int(L[i][j])

for i in range(len(L) - 1):
    if len(L[i]) != len(L[i + 1]):
        print('Incorrect input.')
        sys.exit()

if len(L[0]) < 2 or len(L[0]) > 50 or len(L) < 2 or len(L) > 50:
    print('Incorrect input.')
    sys.exit()

for i in range(len(L)):
    for j in range(len(L[i])):
        if L[i][j] != 0 and L[i][j] != 1:
            print('Incorrect input.')
            sys.exit()
            




def matrix_of_neig(i, j, m, n):
    if m == i - 1 and n == j - 1 and L[i - 1][j] == 1:
        return (i - 1, j)
    elif m == i - 1 and n == j - 1 and j + 1 < len(L[i]) and L[i - 1][j + 1] == 1:
        return (i - 1, j + 1)
    elif m == i - 1 and n == j - 1 and j + 1 < len(L[i]) and L[i][j + 1] == 1:
        return (i, j + 1)
    elif m == i - 1 and n == j - 1 and i + 1 < len(L) and j + 1 < len(L[i]) and L[i + 1][j + 1] == 1:
        return (i + 1, j + 1)
    elif m == i - 1 and n == j - 1 and i + 1 < len(L) and L[i + 1][j] == 1:
        return (i + 1, j)
    elif m == i - 1 and n == j - 1 and i + 1 < len(L) and j - 1 >=0 and L[i + 1][j - 1] == 1:
        return (i + 1, j - 1)
    elif m == i - 1 and n == j - 1 and j - 1 >= 0 and L[i][j - 1] == 1:
        return (i, j - 1)

    ###
    elif m == i - 1 and n == j and j + 1 < len(L[i]) and i - 1 >= 0 and L[i - 1][j + 1] == 1:
        return (i - 1, j + 1)
    elif m == i - 1 and n == j and j + 1 < len(L[i]) and L[i][j + 1] == 1:
        return (i, j + 1)
    elif m == i - 1 and n == j and i + 1 < len(L) and j + 1 < len(L[i]) and L[i + 1][j + 1] == 1:
        return (i + 1, j + 1)
    elif m == i - 1 and n == j and i + 1 < len(L) and L[i + 1][j] == 1:
        return (i + 1, j)
    elif m == i - 1 and n == j and i + 1 < len(L) and j - 1 >=0 and L[i + 1][j - 1] == 1:
        return (i + 1, j - 1)
    elif m == i - 1 and n == j and j - 1 >= 0 and L[i][j - 1] == 1:
        return (i, j - 1)
    elif m == i - 1 and n == j and i - 1 >=0 and j - 1 >= 0 and L[i - 1][j - 1] == 1:
        return (i - 1, j - 1)

    ###
    elif m == i - 1 and n == j + 1 and j + 1 < len(L[i]) and L[i][j + 1] == 1:
        return (i, j + 1)
    elif m == i - 1 and n == j + 1 and i + 1 < len(L) and j + 1 < len(L[i]) and L[i + 1][j + 1] == 1:
        return (i + 1, j + 1)
    elif m == i - 1 and n == j + 1 and i + 1 < len(L) and L[i + 1][j] == 1:
        return (i + 1, j)
    elif m == i - 1 and n == j + 1 and i + 1 < len(L) and j - 1 >=0 and L[i + 1][j - 1] == 1:
        return (i + 1, j - 1)
    elif m == i - 1 and n == j + 1 and j - 1 >= 0 and L[i][j - 1] == 1:
        return (i, j - 1)
    elif m == i - 1 and n == j + 1 and i - 1 >=0 and j - 1 >= 0 and L[i - 1][j - 1] == 1:
        return (i - 1, j - 1)
    elif m == i - 1 and n == j + 1 and i - 1 >= 0 and L[i - 1][j] == 1:
        return (i - 1, j)
    
    #####
    elif m == i and n == j + 1 and i + 1 < len(L) and j + 1 < len(L[i]) and L[i + 1][j + 1] == 1:
        return (i + 1, j + 1)
    elif m == i and n == j + 1 and i + 1 < len(L) and L[i + 1][j] == 1:
        return (i + 1, j)
    elif m == i and n == j + 1 and i + 1 < len(L) and j - 1 >=0 and L[i + 1][j - 1] == 1:
        return (i + 1, j - 1)
    elif m == i and n == j + 1 and j - 1 >= 0 and L[i][j - 1] == 1:
        return (i, j - 1)
    elif m == i and n == j + 1 and i - 1 >=0 and j - 1 >= 0 and L[i - 1][j - 1] == 1:
        return (i - 1, j - 1)
    elif m == i and n == j + 1 and i - 1 >= 0 and L[i - 1][j] == 1:
        return (i - 1, j)
    elif m == i and n == j + 1 and j + 1 < len(L[i]) and i - 1 >= 0 and L[i - 1][j + 1] == 1:
        return (i - 1, j + 1)

    ###
    elif m == i + 1 and n == j + 1 and i + 1 < len(L) and L[i + 1][j] == 1:
        return (i + 1, j)
    elif m == i + 1 and n == j + 1 and i + 1 < len(L) and j - 1 >=0 and L[i + 1][j - 1] == 1:
        return (i + 1, j - 1)
    elif m == i + 1 and n == j + 1 and j - 1 >= 0 and L[i][j - 1] == 1:
        return (i, j - 1)
    elif m == i + 1 and n == j + 1 and i - 1 >=0 and j - 1 >= 0 and L[i - 1][j - 1] == 1:
        return (i - 1, j - 1)
    elif m == i + 1 and n == j + 1 and i - 1 >= 0 and L[i - 1][j] == 1:
        return (i - 1, j)
    elif m == i + 1 and n == j + 1 and j + 1 < len(L[i]) and i - 1 >= 0 and L[i - 1][j + 1] == 1:
        return (i - 1, j + 1)
    elif m == i + 1  and n == j + 1 and j + 1 < len(L[i]) and L[i][j + 1] == 1:
        return (i, j + 1)


    ####
    elif m == i + 1 and n == j and i + 1 < len(L) and j - 1 >=0 and L[i + 1][j - 1] == 1:
        return (i + 1, j - 1)
    elif m == i + 1 and n == j and j - 1 >= 0 and L[i][j - 1] == 1:
        return (i, j - 1)
    elif m == i + 1 and n == j and i - 1 >=0 and j - 1 >= 0 and L[i - 1][j - 1] == 1:
        return (i - 1, j - 1)
    elif m == i + 1 and n == j and i - 1 >= 0 and L[i - 1][j] == 1:
        return (i - 1, j)
    elif m == i + 1 and n == j and j + 1 < len(L[i]) and i - 1 >= 0 and L[i - 1][j + 1] == 1:
        return (i - 1, j + 1)
    elif m == i + 1 and n == j and j + 1 < len(L[i]) and L[i][j + 1] == 1:
        return (i, j + 1)
    elif m == i + 1 and n == j and i + 1 < len(L) and j + 1 < len(L[i]) and L[i + 1][j + 1] == 1:
        return (i + 1, j + 1)

    ####
    elif m == i + 1 and n == j - 1 and j - 1 >= 0 and L[i][j - 1] == 1:
        return (i, j - 1)
    elif m == i + 1 and n == j - 1 and i - 1 >=0 and j - 1 >= 0 and L[i - 1][j - 1] == 1:
        return (i - 1, j - 1)
    elif m == i + 1 and n == j - 1 and i - 1 >= 0 and L[i - 1][j] == 1:
        return (i - 1, j)
    elif m == i + 1 and n == j - 1 and j + 1 < len(L[i]) and i - 1 >= 0 and L[i - 1][j + 1] == 1:
        return (i - 1, j + 1)
    elif m == i + 1 and n == j - 1 and j + 1 < len(L[i]) and L[i][j + 1] == 1:
        return (i, j + 1)
    elif m == i + 1 and n == j - 1 and i + 1 < len(L) and j + 1 < len(L[i]) and L[i + 1][j + 1] == 1:
        return (i + 1, j + 1)
    elif m == i + 1 and n == j - 1 and i + 1 < len(L) and L[i + 1][j] == 1:
        return (i + 1, j)


    ###
    elif m == i and n == j - 1 and i - 1 >=0 and j - 1 >= 0 and L[i - 1][j - 1] == 1:
        return (i - 1, j - 1)
    elif m == i and n == j - 1 and i - 1 >= 0 and L[i - 1][j] == 1:
        return (i - 1, j)
    elif m == i and n == j - 1 and j + 1 < len(L[i]) and i - 1 >= 0 and L[i - 1][j + 1] == 1:
        return (i - 1, j + 1)
    elif m == i and n == j - 1 and j + 1 < len(L[i]) and L[i][j + 1] == 1:
        return (i, j + 1)
    elif m == i and n == j - 1 and i + 1 < len(L) and j + 1 < len(L[i]) and L[i + 1][j + 1] == 1:
        return (i + 1, j + 1)
    elif m == i and n == j - 1 and i + 1 < len(L) and L[i + 1][j] == 1:
        return (i + 1, j)
    elif m == i and n == j - 1 and i + 1 < len(L) and j - 1 >=0 and L[i + 1][j - 1] == 1:
        return (i + 1, j - 1)

    else:
        return 0



    ###

i_s = 0
j_s = 0
n = 2
dic = {}
dic_poly = defaultdict(list)
stack = deque()
U = []
def colour_1(i, j, colour, nb):
    global i_s, j_s
    L[i][j] = colour
    dic_poly[nb].append((i, j))
    
    i_s = i
    j_s = j

    if j + 1 < len(L[i]) and L[i][j + 1] == 1:
        dic[(i, j + 1)] = (i, j)
        L[i][j]  = 1
        colour_3(i, j + 1, colour, nb)
        for i in U:
            a,s = i
            L[a][s] = 1
        for i in U:
            if i in dic_poly[nb]:
                dic_poly[nb].remove(i)
        for i in U:
            if i in dic:
                dic.pop(i)
        U.clear()
        stack.clear()
    elif i + 1 < len(L) and j + 1 < len(L[i]) and L[i + 1][j + 1] == 1:
        dic[(i + 1, j + 1)] = (i, j)
        L[i][j]  = 1
        colour_3(i + 1, j + 1, colour, nb)
        for i in U:
            a,s = i
            L[a][s] = 1
        for i in U:
            if i in dic_poly[nb]:
                dic_poly[nb].remove(i)
        for i in U:
            if i in dic:
                dic.pop(i)
        U.clear()
        stack.clear()
    elif i + 1 < len(L) and L[i + 1][j] == 1:
        dic[(i + 1, j )] = (i, j)
        L[i][j] = 1
        colour_3(i + 1, j, colour, nb)
        for i in U:
            a,s = i
            L[a][s] = 1
        for i in U:
            if i in dic_poly[nb]:
                dic_poly[nb].remove(i)
        for i in U:
            if i in dic:
                dic.pop(i)
        U.clear()
        stack.clear()
    elif i + 1 < len(L) and j - 1 >= 0 and L[i + 1][j - 1] == 1:
        dic[(i + 1, j - 1)] = (i, j)
        L[i][j] = 1
        colour_3(i + 1, j - 1, colour, nb)
        for i in U:
            a,s = i
            L[a][s] = 1
        for i in U:
            if i in dic_poly[nb]:
                dic_poly[nb].remove(i)
        for i in U:
            if i in dic:
                dic.pop(i)
        U.clear()
        stack.clear()

def colour_3(i, j, colour, nb):
    L[i][j] = colour
    a, b = dic[(i, j)]
    dic_poly[nb].append((i, j))

    stack.append((i, j))


    if i == i_s and j == j_s:
        
        return

    elif matrix_of_neig(i, j, a, b) == 0:
        if i == i_s and j == j_s:
            return
        else:
            U.append(stack.pop())
            if len(stack) == 0:
                print('Cannot get polygons as expected.')
                sys.exit()
            w, e = stack[-1]
            colour_4(w, e, colour, nb)

    else:
        w, e = matrix_of_neig(i, j, a, b)

        dic[(w, e)] = (i, j)
  
        colour_3(w, e, colour, nb)


def colour_4(i, j, colour, nb):

    a, b = dic[(i, j)]

    if len(stack) == 1:
        print('Cannot get polygons as expected.')
        sys.exit()
    if matrix_of_neig(i, j, a, b) == 0:

        if i == i_s and j == j_s:
            return
        else:
            U.append(stack.pop())
            w, e = stack[-1]
            colour_4(w, e, colour, nb)
    elif i == i_s and j == j_s:
        return

    else:
        a,b = dic[(i, j)]
        w, e = matrix_of_neig(i, j, a, b)
        dic[(w, e)] = (i, j)
        colour_3(w, e, colour, nb)
        



def is_node(i, j):
    
    x1,y1 = dic[(i, j)]
    for (a,b), (c,d) in dic.items():
        if (c,d) == (i, j):
            
            x2 = a
            y2 = b
    
    if (x1 + x2) == 2 * i and (y1 + y2) == 2 * j:
        return False
    else:
        return True
        
    

        
def get_depth_return(i, j):
    list_left = []
    list_right = []
    list_top = []
    list_down = []

    for k in range(j, -1, -1):
        if L[i][k] == 0 or L[i][k] == 1 or k == j:
            continue
        if len(list_left) == 0:
            list_left.append(L[i][k])
        else:
            if L[i][k] not in list_left:
                list_left.append(L[i][k])
            else:
                continue

    for k in range(j,len(L[i])):
        if L[i][k] == 0 or L[i][k] == 1 or k == j:
            continue
        if len(list_right) == 0:
            list_right.append(L[i][k])
        else:
            if L[i][k] not in list_right:
                list_right.append(L[i][k])
            else:
                continue

    for k in range(i, -1, -1):
        if L[k][j] == 0 or L[k][j] == 1 or k == i:
            continue
        if len(list_top) == 0:
            list_top.append(L[k][j])
        else:
            if L[k][j] not in list_top:
                list_top.append(L[k][j])
            else:
                continue

    for k in range(i, len(L)):
        if L[k][j] == 0 or L[k][j] == 1 or k == i:
            continue
        if len(list_down) == 0:
            list_down.append(L[k][j])
        else:
            if L[k][j] not in list_down:
                list_down.append(L[k][j])
            else:
                continue


    if len(list_left) == 0 or len(list_right) == 0 or len(list_top) == 0 or len(list_down) == 0:
        return 0
    if len(list_left) == len(list_right) and len(list_right) == len(list_top) and len(list_top) == len(list_down):
        return len(list_left)
    
    s1 = set(list_left)
    s2 = set(list_right)
    s3 = set(list_top)
    s4 = set(list_down)

    nb = s1 & s2 & s3 & s4
    nb_list = list(nb)
    if len(nb_list) == 0:
        return 0
    else:
        return len(nb_list)
    
    



    


n = 0
colour = 1
for i in range(len(L)):
    for j in range(len(L[i])):
        if L[i][j] != 1:
            continue
        n = n + 1
        colour += 1
        colour_1(i, j, colour, n)

if len(dic) == 0:
    print('Cannot get polygons as expected.')
    sys.exit()

for i in range(len(L)):
    for j in range(len(L[i])):
        if L[i][j] == 0:
            continue
        if (i, j) not in dic:
            print('Cannot get polygons as expected.')
            sys.exit()



##
##Get Depth
R = []
dic_depth = defaultdict(list)
def get_depth(n):
    depth = 100
    T = dic_poly[n][:]
    for i in T:
        if not is_node(i[0], i[1]):
            continue
        if get_depth_return(i[0], i[1]) < depth:
            depth = get_depth_return(i[0], i[1])

    return depth

for i in dic_poly:
    dic_depth[i].append(get_depth(i)) 
    


##Get Depth_2
def get_number(m, n):
    for i in dic_poly:
        if dic_poly[i][0] == (m, n):
            return i
        
dic_depth_2 = defaultdict(list)
for i in dic_depth:
    dic_depth_2[dic_depth[i][0]].append(i)
    



##Get Parameter
dic_parameter = defaultdict(list)
from math import sqrt
def get_parameter(n):
    parameter = ''
    part_1 = 0
    part_2 = 0

    
    T = dic_poly[n][:]
    for i in range(len(T) - 1):

        if T[i][0] == T[i + 1][0] or T[i][1] == T[i + 1][1]:
            part_1 = part_1 + abs((T[i][0] - T[i + 1][0])) + abs((T[i][1] - T[i + 1][1]))
        else:
            part_2 += 1
    part_1 = round(part_1 * 0.4, 1)


    if part_1 != 0 and part_2 != 0:
        parameter = str(part_1) + ' + ' + str(part_2) + '*' + 'sqrt' + '(.32)'
    elif part_1 != 0 and part_2 == 0:
        parameter = str(part_1)
    elif part_1 == 0 and part_2 != 0:
        parameter = str(part_2) + '*' + 'sqrt' + '(.32)'
        

    dic_parameter[n].append(parameter)
    
for i in dic_poly:
    get_parameter(i)



##Get area
dic_area = defaultdict(list)
def get_area(n):
    area = 0
    T = dic_poly[n][:]
    for i in range(len(T) - 1):
        area += T[i][0] * T[i + 1][1] - T[i + 1][0] * T[i][1]

    area = abs(area) / 2

    area = round(area * 0.4 * 0.4, 2)

    area = '%.2f' % area
    dic_area[n].append(area)

for i in dic_poly:
    get_area(i)
    



##Get convex
dic_convex = defaultdict(list)
def get_convex_of_node(i, j):
    x1, y1 = dic[(i, j)]
    x2, y2 = i, j
    for (a, b), (c, d) in dic.items():
        if (c, d) == (i, j):
            x3 = a
            y3 = b
    s = (x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)
    
    if s <= 0:
        return True
    else:
        return False


def get_convex_of_polygon(n):
    T = dic_poly[n][:]
    for i in T:
        if not get_convex_of_node(i[0],i[1]):
            dic_convex[n].append('no')
            return
    dic_convex[n].append('yes')



for i in dic_poly:
    get_convex_of_polygon(i)



##Get rotation
dic_rotation = defaultdict(list)
def rotate_90(n,a,b):
    T = dic_poly[n][:]
    x_o = a
    y_o = b
    
    for i in range(len(T) - 1):
        x = T[i][0]
        y = T[i][1]
        x_90 = x_o + y - y_o
        y_90 = y_o + x_o - x

        if (x_90, y_90) not in T:
            return 0
        
    return 1
    
        
def rotate_180(n,a,b):
    T = dic_poly[n][:]
    x_o = a
    y_o = b
    
    for i in range(len(T) - 1):
        x = T[i][0]
        y = T[i][1]
        x_180 = 2 * x_o - x
        y_180 = 2 * y_o - y

        if (x_180, y_180) not in T:
            return 0
    return 1
    
def rotate_270(n,a,b):
    T = dic_poly[n][:]
    x_o = a
    y_o = b
    
    for i in range(len(T) - 1):
        x = T[i][0]
        y = T[i][1]
        x_270 = x_o + y_o - y
        y_270 = x - x_o + y_o

        if (x_270, y_270) not in T:
            return 0
    return 1


def get_rotation(n):
    nb_of_roration = 1
    T = dic_poly[n][:]
    a = 0
    b = 0
    x_o = 0
    y_o = 0

    for i in range(len(T) - 1):
        a += T[i][0]
        b += T[i][1]

    x_o = a / (len(T) - 1)
    y_o = b / (len(T) - 1)

    nb_of_roration += rotate_90(n, x_o, y_o) + rotate_180(n, x_o, y_o) + rotate_270(n, x_o, y_o)
    dic_rotation[n].append(nb_of_roration)

    
     
for i in dic_poly:
    get_rotation(i)


if not flag_:
    for i in dic_poly:
        print(f'Polygon {i}:')
        
        print(' ' * 4, end = '')
        print('Perimeter: ', end = '')
        print(dic_parameter[i][0])

        print(' ' * 4, end = '')
        print('Area: ', end = '')
        print(dic_area[i][0])

        print(' ' * 4, end = '')
        print('Convex: ', end = '')
        print(dic_convex[i][0])

        print(' ' * 4, end = '')
        print('Nb of invariant rotations: ', end = '')
        print(dic_rotation[i][0])

        print(' ' * 4, end = '')
        print('Depth: ', end = '')
        print(dic_depth[i][0])

else:
    tex_filename = file_name[0 : len(file_name) - 4] + '.tex'

    C = []
    for i in dic_area:
        C.append(float(dic_area[i][0]))

    max_area = max(C)
    min_area = min(C)

    dic_color_pro = defaultdict(list)
    for i in dic_area:
        if float(dic_area[i][0]) == max_area:
            dic_color_pro[i].append(0)
        elif float(dic_area[i][0]) == min_area:
            dic_color_pro[i].append(100)
        else:
            pro = (max_area - float(dic_area[i][0])) / (max_area - min_area)
            pro = pro * 100
            pro = round(pro)
            
            dic_color_pro[i].append(pro)


    dic_poly_node = defaultdict(list)

    for i in dic_poly:
        for j in dic_poly[i]:
            if is_node(j[0],j[1]):
                a = j[1]
                b = j[0]
                if (a, b) not in dic_poly_node[i]:
                    dic_poly_node[i].append((a,b))




    with open(tex_filename, 'w') as tex_file:
        print('\\documentclass[10pt]{article}\n'
              '\\usepackage{tikz}\n'
              '\\usepackage[margin=0cm]{geometry}\n'
              '\\pagestyle{empty}\n'
              '\n'
              '\\begin{document}\n'
              '\n'
              '\\vspace*{\\fill}\n'
              '\\begin{center}\n'
              '\\begin{tikzpicture}[x=0.4cm, y=-0.4cm, thick, brown]', file = tex_file)
    
        print(f'\draw[ultra thick] (0, 0) -- ({len(L[0]) - 1}, 0) -- ({len(L[0]) - 1}, {len(L) - 1}) -- (0, {len(L) - 1}) -- cycle;', file = tex_file)

        for i in dic_depth_2:
            print(f'%Depth {i}', file = tex_file)
            for j in dic_depth_2[i]:
                print(f'\\filldraw[fill=orange!{dic_color_pro[j][0]}!yellow]',end = ' ', file = tex_file)
                for i in dic_poly_node[j]:
                    print(f'({i[0]}, {i[1]}) -- ', end = '', file = tex_file)
                print('cycle;', file = tex_file)

        print('\\end{tikzpicture}\n'
              '\\end{center}\n'
              '\\vspace*{\\fill}\n'
              '\n'
              '\\end{document}', file = tex_file)


    os.system('pdflatex ' + tex_filename)
    for file in (file_name[0 : len(file_name) - 4]  + ext for ext in ('.aux', '.log')):
        os.remove(file)
    print(f'\nProduced {file_name[0 : len(file_name) - 4]  + ".pdf"}')

