import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def spline_lineal(x, y):
    """
    spline_lineal: Interpolación spline lineal con impresión y gráfica.
    Entrada:
        x: nodos (vector de abscisas, ordenado y sin repetidos)
        y: valores en los nodos (vector de ordenadas)
    Salida:
        coef: matriz (n-1)x2 con los coeficientes de cada tramo: [pendiente, constante]
    """

    # Validaciones
    x = np.asarray(x)
    y = np.asarray(y)

    if x.ndim != 1 or y.ndim != 1:
        raise ValueError('Las entradas deben ser vectores.')
    if len(x) != len(y):
        raise ValueError('Los vectores x e y deben tener la misma longitud.')
    if len(np.unique(x)) != len(x):
        raise ValueError('Los valores de x deben ser distintos.')
    if not np.all(np.diff(x) > 0):
        raise ValueError('x debe estar ordenado estrictamente de forma creciente.')

    n = len(x)
    A = np.zeros((2*(n-1), 2*(n-1)))
    b = np.zeros(2*(n-1))

    # Ecuaciones para extremos de cada tramo
    c = 0
    h = 0
    for i in range(n-1):
        A[i, c] = x[i]
        A[i, c+1] = 1
        b[i] = y[i]
        c += 2
        h += 1

    c = 0
    for i in range(1, n):
        A[h, c] = x[i]
        A[h, c+1] = 1
        b[h] = y[i]
        c += 2
        h += 1

    # Resolver sistema
    sol = np.linalg.solve(A, b)
    coef = sol.reshape((n-1, 2))

    # Mostrar los polinomios por tramos
    print('Polinomio Spline Lineal por tramos:')
    for i in range(n-1):
        print(f'P{i+1}(x) = {coef[i,0]:.6f} * x + {coef[i,1]:.6f},  x ∈ [{x[i]:.2f}, {x[i+1]:.2f}]')

    # Graficar los tramos
    plt.figure()
    for i in range(n-1):
        xi = np.linspace(x[i], x[i+1], 100)
        yi = coef[i,0] * xi + coef[i,1]
        plt.plot(xi, yi, label=f'Tramo {i+1}')
    plt.plot(x, y, 'ro', label='Puntos de datos')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('Spline Lineal')
    plt.title('Interpolación Spline Lineal')
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    grafica_base64 = base64.b64encode(buf.read()).decode('ascii')
    return {'coef': coef.tolist(), 'grafica_base64': grafica_base64}