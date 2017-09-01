


value_of_account = int(input('Input the desired amount: '))
n = value_of_account
L = [100, 50, 20, 10, 5, 2, 1]
dic = {}

for i in L:
    if n // i != 0:
        dic[i] = n // i
        n = n % i

nb_of_banknotes = 0
for i in dic:
    nb_of_banknotes += dic[i]

if nb_of_banknotes == 1:
    print(f'{nb_of_banknotes} banknote is needed.')
else:
    print(f'{nb_of_banknotes} banknotes are needed.')
print('The detail is: ')
for i in dic:
    s = str(i)
    s = '$'+ s
    print('{:>4}: {}'.format(s, dic[i]))
