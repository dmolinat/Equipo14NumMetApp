import numpy as np
def bisect(f_s, a, b, delta):
    f=lambda x: eval(f_s)
    ya = f(a);
    yb = f(b);
    c = 0;
    err = 0;
    yc = 0;
    if  (ya*yb > 0):
        return
    max1 = 1 + round((np.log(b-a) - np.log(delta)) / np.log(2));
    for k in range(1,max1+1):
        c = (a + b) / 2;
        yc = f(c);
        if  (yc == 0):
            a = c;
            b = c;
        elif  (yb*yc > 0):
            b = c;
            yb = yc;
        else:
            a = c;
            ya = yc;
        if  (b-a < delta):
            break
    c = (a + b) / 2;
    err = abs(b - a);
    yc = f(c);
    return (c, err, yc)
    
#f=lambda x: (np.exp(-2*x))/(np.tan(x))
#bisect(f,4,5,1e-10)