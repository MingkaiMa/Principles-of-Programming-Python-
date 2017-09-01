

def populate_pascal_triangle(n):
    L = [[0]*(n+1) for _ in range(n+1)]
    L[0][0] = 1
    L[1][0] = 1
    L[1][1] = 1

    for i in range(2,n+1):
        for j in range(0,i+1):
            R = []
            if j == 0 or j == i:
                
                L[i][j] = 1
            else:
                L[i][j] = L[i-1][j-1] + L[i-1][j]
    
    width = len(str(max(L[n])))
    for i in range(0,n+1):
        print(' '*width * (n - i),end='')
        for j in range(0,n+1):
            
            if L[i][j] != 0:
                print(f'{L[i][j]:{width}d}',end=' '*width)
            else:
                print('',end='')
        print()

try:
    a = input('Enter a nonnegative integer: ')
except ValueError:
    print('Wrong input,giving up...')
    sys.exit()

try:
    a = int(a)
    if a <= 0:
        raise ValueError
except:
    print('Wrong input,giving up...')
    sys.exit
    
populate_pascal_triangle(a)
