

def get_longest_sequence(string):
    dic = {}
    L = []
    s = string
    L.append(s[0])
    s = s[1:]
    max_length = 0
    max_letter = ''
    while True:
        if ord(L[-1]) + 1 == ord(s[0]):
            L.append(s[0])
            s = s[1:]
            
        else:
            s = s[1:]

        if len(s) == 0:
            break

    if max_length < len(L):
        max_length = len(L)
        for i in range(0,len(L)):
            max_letter = max_letter + L[i]

    return max_letter
        

    
string = 'abcdiivjwkaalbmmbz'

while 1:
    try:
        string = input('Please input a string of lowercase letters: ')
        break
    except:
        print('Incorrect, giving up.')
    



max_length = 0
max_letter = ''
if len(string) == 1:
    print(f'The solution is: {string}')
else:
    for i in range(len(string)-1):
        if max_length < len(get_longest_sequence(string)):
            max_length = len(get_longest_sequence(string))
            max_letter = get_longest_sequence(string)
        string = string[1:] 
    print(f'The solution is: {max_letter}')
    
    
    
    
    
            
            
        


