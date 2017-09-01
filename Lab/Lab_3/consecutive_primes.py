from math import sqrt

def primes(N):
 
    L = []

    N_index = (N - 1) // 2
    primes_sieve = [True] * (N_index + 1)
    for k in range(1, (round(sqrt(N)) + 1) // 2):
        if primes_sieve[k]:

            for i in range(2 * k * (k + 1), N_index + 1, 2 * k + 1):
                primes_sieve[i] = False
                
    for n in range(1, N_index + 1):
        if primes_sieve[n]:
            if 2*n+1 > 10000:
                L.append(2*n+1)           

    R = []
    for j in range(0,len(L)-6):
        if L[j+1] == L[j]+2 and L[j+2] == L[j] + 6 and L[j+3] == L[j] + 12 and L[j+4] == L[j] + 20 and L[j+5] == L[j] + 30:
            for i in L[j:j+6]:
                R.append(i)

    field_width = len(str(N)) + 1
    nb_of_fields = 6
    count = 0
    for n in range(0,len(R)):
        if count != 5:
            print(f'{R[n]:<{field_width}d}',end ='')
            count += 1
            continue
        if count == 5:
            print(f'{R[n]}',end = '\n')
            count = 0
            


if __name__ == '__main__':
    print('The solutions are:\n')
    primes(100000)
