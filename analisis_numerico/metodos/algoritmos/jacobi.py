import numpy as np
import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def jacobi(x0, A, b, Tol, niter, error_type):
    # Paso 1
    A = np.array(A, float)
    b = np.array(b, float)
    x = np.array(x0, float)

    if not (A.ndim == 2 and A.shape[0] == A.shape[1]):
        raise ValueError("La matriz A debe ser cuadrada.")
    if b.size != A.shape[0] or x.size != A.shape[0]:
        raise ValueError("Las dimensiones de x0, A y b no son compatibles.")
    if error_type.lower() not in ('absoluto', 'relativo'):
        raise ValueError("error_type debe ser 'absoluto' o 'relativo'.")

    historial = []
    n = A.shape[0]
    D = np.diag(A)
    R = A - np.diagflat(D)
    X = np.zeros((n, int(niter)+1))
    X[:, 0] = x

    for k in range(1, int(niter)+1):
        x_new = (b - R.dot(x)) / D
        if error_type.lower() == 'absoluto':
            E = np.linalg.norm(x_new - x, ord=np.inf)
        else:
            E = np.linalg.norm((x_new - x) / x_new, ord=np.inf)
        historial.append((k, x_new.copy(), E))
        X[:, k] = x_new
        x = x_new
        if E < Tol:
            break

    # Gráfica
    plt.figure()
    for i in range(n):
        plt.plot(range(0, k+1), X[i, :k+1], '-o', linewidth=1.5, label=f'x({i+1})')
    plt.xlabel('Iteración')
    plt.ylabel('Valor de las variables')
    plt.legend(loc='best')
    plt.title('Evolución de las variables (Jacobi)')
    plt.grid(True)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('ascii')

    return {
        'x': x.tolist(),
        'historial': historial,
        'grafica_base64': img_base64
    }