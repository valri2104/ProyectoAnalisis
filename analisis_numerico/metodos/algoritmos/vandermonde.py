import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import io
import base64

def vandermonde(x, y):
    """
    vandermonde: Interpolación mediante el método de Vandermonde.
    Entrada:
        x: lista o array de nodos (abscisas), deben ser distintos
        y: lista o array de valores en los nodos
    Salida:
        pol: polinomio interpolante en forma simbólica (expresado)
    """
    x = np.asarray(x)
    y = np.asarray(y)

    # Validaciones
    if x.ndim != 1 or y.ndim != 1:
        raise ValueError("Las entradas deben ser vectores.")
    if len(x) != len(y):
        raise ValueError("Los vectores x e y deben tener la misma longitud.")
    if len(np.unique(x)) < len(x):
        raise ValueError("Los valores de x deben ser distintos.")

    n = len(x)

    # Construir matriz de Vandermonde
    V = np.vander(x, N=n, increasing=False)

    # Resolver sistema
    coef = np.linalg.solve(V, y)

    # Polinomio simbólico con coeficientes insertos
    t = sp.symbols('t')
    pol = sum(coef[i] * t**(n - i - 1) for i in range(n))
    pol = sp.expand(pol)
    pol_decimal = sp.N(pol, 6)

    # Mostrar polinomio simbólico expandido
    print("Polinomio de interpolación (expandido con coeficientes):")
    sp.pprint(pol_decimal, use_unicode=True)

    # Graficar
    f = sp.lambdify(t, pol_decimal, modules='numpy')
    t_vals = np.linspace(min(x)-1, max(x)+1, 500)
    plt.figure()
    plt.plot(t_vals, f(t_vals), label='Polinomio', linewidth=2)
    plt.plot(x, y, 'ro', label='Datos originales', markersize=8)
    plt.title('Polinomio de Interpolación - Método de Vandermonde')
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.grid(True)
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    grafica_base64 = base64.b64encode(buf.read()).decode('ascii')
    return {'polinomio': str(pol_decimal), 'grafica_base64': grafica_base64}