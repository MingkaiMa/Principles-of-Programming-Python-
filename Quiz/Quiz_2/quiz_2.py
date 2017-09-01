
import sys


def pr(n):
    if n==2:return True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def main(N):
    n = 2
    a = []
    while True:
        if pr(n):
            a.append(n)
        if sum(a)>=N:
            break
        n+=1
    le=len(a)
    j=le
    while j:
        for k in reversed(range(0,le+1-j)):
            y=sum(a[k:k+j])
            if y<=N:
                if pr(y):
                    return len(a[k:k+j]),y
        j-=1

try:
    N = int(input('Enter an integer at least equal to 5: '))
    if N < 5:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


max_length, candidate = main(N)
if max_length:
    print('The largest sequence of consecutive primes that add up\n  '
          'to a prime P equal to {} at most has a length of {}.\n'
          'The largest such P is {}.'.format(N, max_length, candidate))




