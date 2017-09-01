
from collections import defaultdict
def permute(L):
    yield L
    stack = [(0, i) for i in range(len(L) - 1, 0, -1)]
    while stack:
        low, high = stack.pop()
        if high % 2:
            L[low], L[high] = L[high], L[low]
        else:
            L[0], L[high] = L[high], L[0]
        yield L
        if low + 1 != high:
            stack.append((low + 1, high))
        for i in range(high - 1, 0, -1):
            stack.append((0, i))


def can_merge(string_1,string_2,string_3):
    if not string_1 and string_2 == string_3:
        return True
    if not string_2 and string_1 == string_3:
        return True
    if not string_1 or not string_2:
        return False

    if string_1[0] == string_3[0] and can_merge(string_1[1:], string_2, string_3[1:]):
        return True
    if string_2[0] == string_3[0] and can_merge(string_1, string_2[1:], string_3[1:]):
        return True

while 1:
    try:
        string_1 = input('Please input the first string: ')
        string_2 = input('Please input the second string: ')
        string_3 = input('Please input the third string: ')
        break
    except:
        print('Incorrect, giving up.')
    



result = ['',string_1,string_2,string_3]

dic = defaultdict(list)

if len(string_1) == len(string_2) + len(string_3):
    for i in range(3):
        dic[1].append(string_2)
        dic[1].append(string_3)
        dic[1].append(string_1)
if len(string_2) == len(string_1) + len(string_3):
    for i in range(3):
        dic[2].append(string_1)
        dic[2].append(string_3)
        dic[2].append(string_2)
if len(string_3) == len(string_2) + len(string_1):
    for i in range(3):
        dic[3].append(string_1)
        dic[3].append(string_2)
        dic[3].append(string_3)




for i in dic:
    if can_merge(dic[i][0],dic[i][1],dic[i][2]):
        if i == 1:
            print('The first string can be obtained by merging the other two.')
        if i == 2:
            print('The second string can be obtained by merging the other two.')
        if i == 3:
            print('The third string can be obtained by merging the other two.')
    else:
        print('No solution')
    
