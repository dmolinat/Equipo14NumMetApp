import numpy as np

def RK4(ED, a, b, Z, M):
    try:
            
        F = lambda t,y: eval(ED)
        h = (b - a) / M
        T = np.linspace(a, b, M+1)
        Za=[Z]
        n = len(Za)
        Z = np.zeros((M+1, n))
        Z[0, :] = Za

        for j in range(M):
            k1 = h * F(T[j], Z[j, :])
            k2 = h * F(T[j] + h/2, Z[j, :] + k1/2)
            k3 = h * F(T[j] + h/2, Z[j, :] + k2/2)
            k4 = h * F(T[j] + h, Z[j, :] + k3)
            Z[j+1, :] = Z[j, :] + (k1 + 2*k2 + 2*k3 + k4) / 6

        AproxSol = np.column_stack((T, Z))
        return (str(list(AproxSol)), "RK4")
    except:
        return (str([[-1,-1]]), "RK4: Error with params.")