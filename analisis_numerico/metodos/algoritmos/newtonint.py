import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

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
    tabla = np.zeros((n, n), dtype=object)
    tabla[:, 0] = list(map(sp.Rational, y))  # y como racionales exactos

    for j in range(1, n):
        for i in range(j, n):
            tabla[i, j] = (tabla[i, j-1] - tabla[i-1, j-1]) / (x[i] - x[i-j])

    coef = [tabla[i, i] for i in range(n)]

    t = sp.Symbol('t')
    pol = sp.Rational(0)
    prod = 1

    for i in range(n):
        pol += coef[i] * prod
        prod *= (t - sp.Float(x[i], 6))  # mantener decimal explícito en factores

    pol_decimal = sp.N(pol, 6)

    # Mostrar sin expandir
    print("Polinomio de interpolación (forma simbólica, decimal):")
    print(pol_decimal)

    # Graficar
    f = sp.lambdify(t, pol_decimal, modules='numpy')
    t_vals = np.linspace(min(x)-1, max(x)+1, 500)
    plt.plot(t_vals, f(t_vals), label='Polinomio', linewidth=2)
    plt.plot(x, y, 'ro', label='Datos originales', markersize=8)
    plt.title('Polinomio de Interpolación de Newton (forma factorizada)')
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.grid(True)
    plt.legend()
    plt.show()

    return pol_decimal