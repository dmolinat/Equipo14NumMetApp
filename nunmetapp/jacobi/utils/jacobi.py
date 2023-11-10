import numpy as np

def jacobi(A, B, x0, tol, max_iter):
    try:
        A=np.array(eval(A))
        B=np.array(eval(B))
        x0=np.array(eval(x0))
        n = len(B)
        x = x0.copy()
        
        for k in range(max_iter):
            x_new = np.zeros(n)
            for i in range(n):
                x_new[i] = (B[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
            
            err=np.linalg.norm(x_new - x)
            if  err < tol:
                return (str(x_new),k,err,"JACOBI")
            x = x_new
        
        return (str(x),k,err,"JACOBI")
    except:
        return (str(np.zeros(1)),-1,np.finfo(np.float64).eps,"JACOBI-ERROR: Matrix A or Vectors B, x0 or params is not valid.")
