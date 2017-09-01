# Decodes all multiplications of the form
#
#                        *  *  *
#                   x       *  *
#                     ----------
#                     *  *  *  *
#                     *  *  *
#                     ----------
#                     *  *  *  *
#
# such that the sum of all digits in all 4 columns is constant.

L = []
for a in range(100,1000):
    for b in range(10,100):
        c = a * b
        d = a * int(str(b)[1])
        e = a * int(str(b)[0])
        if len(str(c)) == 4:
            if len(str(d)) == 4:
                if len(str(e)) == 3:
                    f = int(str(a)[2])+int(str(b)[1])+int(str(c)[3])+int(str(d)[3])
                    g = int(str(a)[1])+int(str(b)[0])+int(str(c)[2])+int(str(d)[2])+int(str(e)[2])
                    h = int(str(a)[0])+int(str(c)[1])+int(str(d)[1])+int(str(e)[1])
                    i = int(str(c)[0])+ int(str(d)[0])+int(str(e)[0])
                    if f == g == h == i:
                        L.append((a,b))
                        print(f'{a} * {b} = {e}, all columns adding up to {f}.')

