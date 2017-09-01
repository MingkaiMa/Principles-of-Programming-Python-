import sys


str_list = input("Please input the heroes' powers: ")

try:
    super_power_list = [int(n) for n in str_list.split()]
except ValueError:
    print('Sorry, these are not valid power values.')
    sys.exit()

try:
    nb_of_swiches = int(input('Please input the number of power flips: '))
except ValueError:
    print('Sorry, this is not a valid number of power flips.')
    sys.exit()
if nb_of_swiches > len(super_power_list) or nb_of_swiches < 0:
    print('Sorry, this is not a valid number of power flips.')
    sys.exit()
 
nb_of_swiches_1 = nb_of_swiches
T = sorted(super_power_list)
R = T[:]
for i in range(0,len(R)):
    if nb_of_swiches_1 == 0:
        break
    if R[i] < 0:
        R[i] = R[i] * (-1)
        nb_of_swiches_1 -= 1
    if nb_of_swiches_1 == 0:
        break
if nb_of_swiches_1 != 0:
    if nb_of_swiches_1 % 2 != 0:
        R[R.index(min(R))] = R[R.index(min(R))] * (-1)
print(f'Possibly flipping the power of the same hero many times, the greatest achievable power is {sum(R)}.')

nb_of_swiches_2 = nb_of_swiches
R = T[:]
if len(super_power_list) == nb_of_swiches_2:
    print(f'Flipping the power of the same hero at most once, the greatest achievable power is {(-1)*sum(R)}.')
else:
    for i in range(0,len(R)):
        if nb_of_swiches_2 == 0:
            break
        R[i] = R[i] * (-1)
        nb_of_swiches_2 -= 1
        if nb_of_swiches_2 == 0:
            break
    print(f'Flipping the power of the same hero at most once, the greatest achievable power is {sum(R)}.')


P = [-1 * i for i in super_power_list]
R = P[:]
nb_of_swiches_3 = nb_of_swiches
def function_3(L,length):
    max_so_far = float('-Inf')
    s = sum(L[0:length])
    for i in range(1,len(L) - length + 1):
        max_so_far = max(max_so_far, s)
        s = s - L[i-1] + L[i+length-1]
        max_so_far = max(max_so_far, s)
        
    return max_so_far

if len(R) == nb_of_swiches_3:
    print(f'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {sum(R)}.')
elif nb_of_swiches_3 == 0:
    print(f'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {sum(super_power_list)}.')
else:
    print(f'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {sum(super_power_list)+2*function_3(R,nb_of_swiches_3)}.')

R = P[:]
def function_4(L):
    max_end_here = 0
    max_so_far = 0
    for i in range(0,len(L)):
        max_end_here = max(0,max_end_here + L[i])
        max_so_far = max(max_so_far, max_end_here)
    return max_so_far

print(f'Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is {sum(super_power_list)+2*function_4(R)}.')

