def iterative_fibonacci(n):
    if n < 2:
        return n
    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current


def encode(n):
    i = 2
    L = []
    R = []
    while (iterative_fibonacci(i) <= n ):
        L.append(i)
        i += 1        
    sigma = ''
    for i in sorted(L, reverse = True):
        if n - iterative_fibonacci(i) >= 0:
            R.append(1)
            n = n - iterative_fibonacci(i)
        else:
            R.append(0)
    for i in reversed(R):
        sigma += str(i)
    fibonacci_code = sigma + '1'
    print(fibonacci_code)
    
def decode(fibonacci_code):
    n = 0
    s = fibonacci_code[:len(fibonacci_code) - 1]
    if len(s) == 0:
        return 0
    if len(s) == 1:
        if s == '0':
            return 0
        else:
            return 1
    for i in range(len(s) - 1):
        if int(s[i]) == int(s[i + 1]) and int(s[i]) != 0:
            return 0

    for i in range(len(s)):
        if int(s[i]):
            n += iterative_fibonacci(i + 2)
    return n
            
    
    
    
