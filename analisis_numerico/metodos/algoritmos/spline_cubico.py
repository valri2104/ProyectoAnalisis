import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def spline_cubico(x, y):
    """
    spline_cubico: Interpolación spline cúbico natural.
    Entrada:
        x: nodos (vector de abscisas, ordenado y sin repetidos)
        y: valores en los nodos (vector de ordenadas)
    Salida:
        coef: matriz (n-1)x4 con los coeficientes de cada tramo: [a, b, c, d]
    """
    x = np.asarray(x)
    y = np.asarray(y)

    # Validaciones
    if x.ndim != 1 or y.ndim != 1:
        raise ValueError('Las entradas deben ser vectores.')
    if len(x) != len(y):
        raise ValueError('Los vectores x e y deben tener la misma longitud.')
    if len(np.unique(x)) != len(x):
        raise ValueError('Los valores de x deben ser distintos.')
    if not np.all(np.diff(x) > 0):
        raise ValueError('x debe estar ordenado estrictamente de forma creciente.')

    n = len(x)
    N = 4 * (n - 1)
    A = np.zeros((N, N))
    b_vec = np.zeros(N)

    # Ecuaciones de coincidencia
    row = 0
    col = 0
    for i in range(n - 1):
        xi = x[i]
        A[row, col:col+4] = [xi**3, xi**2, xi, 1]
        b_vec[row] = y[i]
        row += 1
        col += 4

    col = 0
    for i in range(1, n):
        xi = x[i]
        A[row, col:col+4] = [xi**3, xi**2, xi, 1]
        b_vec[row] = y[i]
        row += 1
        col += 4

    # Primera derivada continua en puntos interiores
    col = 0
    for i in range(1, n - 1):
        xi = x[i]
        A[row, col:col+3] = [3*xi**2, 2*xi, 1]
        A[row, col+4:col+7] = [-3*xi**2, -2*xi, -1]
        row += 1
        col += 4

    # Segunda derivada continua en puntos interiores
    col = 0
    for i in range(1, n - 1):
        xi = x[i]
        A[row, col:col+2] = [6*xi, 2]
        A[row, col+4:col+6] = [-6*xi, -2]
        row += 1
        col += 4

    # Condiciones de spline natural
    A[row, 0:2] = [6*x[0], 2]
    row += 1
    A[row, -4:-2] = [6*x[-1], 2]
    row += 1

    # Resolver el sistema
    sol = np.linalg.solve(A, b_vec)
    coef = sol.reshape((n - 1, 4))

    # Mostrar polinomios por tramos
    print("Polinomio Spline Cúbico por tramos:")
    for i in range(n - 1):
        a, b_, c, d = coef[i]
        print(f"P{i+1}(x) = {a:.6f}*x^3 + {b_:.6f}*x^2 + {c:.6f}*x + {d:.6f},  x ∈ [{x[i]:.2f}, {x[i+1]:.2f}]")

    # Graficar
    plt.figure()
    for i in range(n - 1):
        a, b_, c, d = coef[i]
        t = np.linspace(x[i], x[i+1], 100)
        f = a*t**3 + b_*t**2 + c*t + d
        plt.plot(t, f, label=f'Tramo {i+1}')
    plt.plot(x, y, 'ro', label='Puntos de datos')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('Spline Cúbico')
    plt.title('Interpolación Spline Cúbico Natural')
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    grafica_base64 = base64.b64encode(buf.read()).decode('ascii')
    return {'coef': coef.tolist(), 'grafica_base64': grafica_base64}