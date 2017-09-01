
dic = {}
def is_sum_of_two_squares(n):
    for i in range(0,32):
        for j in range(i,32):
            if i ** 2 + j ** 2 == n:
                dic[n] = [i,j]
                return True
    return False

L = list(range(100,1000))
                
R = [0] * len(L)

for k in range(0,len(L)):
    if is_sum_of_two_squares(L[k]):
        R[k] = 1
#print(R)



for i in range(0,len(L)-2):
    if sum(R[i:i+3]) == 3:
        print(f'({100+i},{101+i},{102+i}) (equal to ({dic[100+i][0]}^2+{dic[100+i][1]}^2, {dic[101+i][0]}^2+{dic[101+i][1]}^2, {dic[102+i][0]}^2+{dic[102+i][1]}^2)) is a solution.')
