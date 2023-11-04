import numpy as np

def boolerl(f_s, a, b, M):
    # Entradas: f una función creada por @
    #           - Intervalo [a, b]
    #           - M subintervalos con M múltiplo de 4

    # Salida: Aproximación de la integral de f en [a, b] por el método de boole compuesto.
    
    f=lambda x: eval(f_s)
    if M % 4 != 0:
        return (np.nan, "BOOLER: M must be multiple of 4.")
    else:
        AproxNum = 0
        h = (b - a) / M
        subI = np.linspace(a, b, M + 1)
        for i in range(M + 1):
            if i == 0 or i == M:
                AproxNum += 7 * f(subI[i])
            elif i % 2 != 0:
                AproxNum += 32 * f(subI[i])
            elif i % 2 == 0 and i % 4 != 0:
                AproxNum += 12 * f(subI[i])
            elif i % 4 == 0:
                AproxNum += 14 * f(subI[i])

        AproxNum = (2 * h / 45) * AproxNum
        #print("La aproximación de la integral es de orden h^6 =", h ** 6)
        return (AproxNum, "BOOLERL")