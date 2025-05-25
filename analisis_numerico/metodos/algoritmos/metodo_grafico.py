import numpy as np
import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def metodo_grafico(f, a, b, Tol, niter, error_type):
    # Paso 1
    if a >= b:
        raise ValueError('El valor de "a" debe ser menor que "b".')
    if Tol <= 0:
        raise ValueError('La tolerancia debe ser positiva.')
    if niter <= 1 or int(niter) != niter:
        raise ValueError('niter debe ser un entero mayor que 1.')
    if error_type.lower() not in ('absoluto', 'relativo'):
        raise ValueError('El tipo de error debe ser "relativo" o "absoluto".')

    X = np.linspace(a, b, int(niter))
    FX = np.array([f(xi) for xi in X])
    E = np.zeros(len(X))
    raiz_aprox = np.nan

    for i in range(len(X)):
        if i == 0:
            E[i] = np.nan
        else:
            if error_type.lower() == 'relativo':
                E[i] = abs((X[i] - X[i-1]) / max(abs(X[i]), np.finfo(float).eps))
            else:
                E[i] = abs(X[i] - X[i-1])
            if FX[i-1] * FX[i] < 0 and np.isnan(raiz_aprox):
                raiz_aprox = X[i] if abs(FX[i]) < abs(FX[i-1]) else X[i-1]
            if not np.isnan(raiz_aprox) and E[i] < Tol:
                break

    n = i + 1

    # Gráfica
    plt.figure()
    plt.plot(X[:n], FX[:n], 'b-', linewidth=2)
    plt.axhline(0, color='r', linestyle='--')
    if not np.isnan(raiz_aprox):
        plt.plot(raiz_aprox, f(raiz_aprox), 'ro', markersize=8)
    plt.title('Método Gráfico para Raíces')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    grafica_base64 = base64.b64encode(buf.read()).decode('ascii')

    return {
        'n': n,
        'X': X[:n].tolist(),
        'FX': FX[:n].tolist(),
        'E': E[:n].tolist(),
        'raiz_aprox': raiz_aprox,
        'grafica_base64': grafica_base64
    }