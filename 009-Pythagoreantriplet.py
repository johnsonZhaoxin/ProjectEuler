import numpy as np
def get_hypo(a,b):
    err = 1e-7
    hypo = np.sqrt(a**2+b**2)
    if hypo - int(hypo) < err:
        #print("斜边为整数,为%d"%(int(hypo)))
        return hypo
    else:
        #print("斜边不是整数,为%f" % (hypo))
        return hypo


for i in range(1,998):
    for j in range(1,998-i):
        hypo = get_hypo(i,j)
        if int(hypo)+i+j == 1000:
            print(i,j,hypo)

