import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import io
import base64

def newtonint(x, y):
    """
    newtonint: Interpolación de Newton con diferencias divididas (forma factorizada).
    Entrada:
        x: vector de nodos
        y: vector de valores
    Salida:
        pol: polinomio interpolante en forma simbólica no expandida (decimal)
    """
    x = np.asarray(x)
    y = np.asarray(y)

    if x.ndim != 1 or y.ndim != 1:
        raise ValueError("Las entradas deben ser vectores.")
    if len(x) != len(y):
        raise ValueError("x e y deben tener la misma longitud.")
    if len(np.unique(x)) < len(x):
        raise ValueError("Los valores de x deben ser distintos.")

    n = len(x)
    coef = np.copy(y)
    for j in range(1, n):
        coef[j:n] = (coef[j:n] - coef[j-1]) / (x[j:n] - x[j-1])

    def p(t):
        result = coef[0]
        prod = 1.0
        for j in range(1, n):
            prod *= (t - x[j-1])
            result += coef[j] * prod
        return result

    t_vals = np.linspace(min(x)-1, max(x)+1, 500)
    y_vals = [p(t) for t in t_vals]
    plt.figure()
    plt.plot(t_vals, y_vals, label='Polinomio de Newton', linewidth=2)
    plt.plot(x, y, 'ro', label='Datos originales', markersize=8)
    plt.title('Interpolación de Newton')
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.grid(True)
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    grafica_base64 = base64.b64encode(buf.read()).decode('ascii')
    return {'coef': coef.tolist(), 'grafica_base64': grafica_base64}