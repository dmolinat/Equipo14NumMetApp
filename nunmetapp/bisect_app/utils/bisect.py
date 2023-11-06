import numpy as np
def bisect(f_s, a, b, delta):
    try:
        f=lambda x: eval(f_s)
        ya = f(a);
        yb = f(b);
        c = 0;
        err = 0;
        yc = 0;
        if  (ya*yb > 0):
            return (np.finfo(np.float64).eps, np.finfo(np.float64).eps, np.finfo(np.float64).eps, "BISECT: No satisface que TVI: f(a)*f(b)>0")
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
        return (c, err, yc, "BISECT")
    except:
        return (np.finfo(np.float64).eps,np.finfo(np.float64).eps,np.finfo(np.float64).eps,"BISECT-ERROR: Function or params is not valid")