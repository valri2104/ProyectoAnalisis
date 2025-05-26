import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import io
import base64

def lagrange(x, y):
    """
    lagrange_interp: Interpolación de Lagrange con salida simbólica decimal.
    Entrada:
        x: nodos (valores de x)
        y: valores correspondientes
    Salida:
        pol: polinomio simbólico interpolante (decimal)
    """
    x = np.asarray(x)
    y = np.asarray(y)

    if x.ndim != 1 or y.ndim != 1:
        raise ValueError("Las entradas deben ser vectores.")
    if len(x) != len(y):
        raise ValueError("Los vectores x e y deben tener la misma longitud.")
    if len(np.unique(x)) < len(x):
        raise ValueError("Los valores de x deben ser distintos.")

    n = len(x)
    t = sp.Symbol('t')
    poly_sym = 0

    for i in range(n):
        Li = 1
        den = 1
        for j in range(n):
            if j != i:
                Li *= (t - sp.Float(x[j], 6))
                den *= (x[i] - x[j])
        Li_term = y[i] * Li / den
        poly_sym += Li_term

    poly_sym = sp.expand(poly_sym)
    poly_decimal = sp.N(poly_sym, 6)

    print("Polinomio de interpolación (forma simbólica, decimal):")
    print(poly_decimal)

    # Graficar
    f = sp.lambdify(t, poly_decimal, modules='numpy')
    t_vals = np.linspace(min(x)-1, max(x)+1, 500)
    y_vals = f(t_vals)
    plt.figure()
    plt.plot(t_vals, y_vals, label='Polinomio de Lagrange', linewidth=2)
    plt.plot(x, y, 'ro', label='Datos originales', markersize=8)
    plt.title('Interpolación de Lagrange')
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.grid(True)
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    grafica_base64 = base64.b64encode(buf.read()).decode('ascii')
    return {'grafica_base64': grafica_base64}