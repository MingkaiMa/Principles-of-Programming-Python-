L = []

for i in range(10,100):
    for j in range(10,100):
        for k in range(10,100):
                
                a = set(str(i)+str(j)+str(k))
                c = set(str(i*j*k))
                R = [i,j,k]
                R.sort()
                if len(a) == 6 :
                    if a == c:
                        if not R in L:
                            L.append(R)


for lst in L:
    print(f'{lst[0]} x {lst[1]} x {lst[2]} = {lst[0]*lst[1]*lst[2]} is a solution.',end = '\n')
                        

                
