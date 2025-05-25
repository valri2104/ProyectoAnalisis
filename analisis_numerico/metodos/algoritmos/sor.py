import numpy as np
import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def sor(x0, A, b, Tol, niter, w, error_type):
    # Paso 1
    A = np.array(A, float)
    b = np.array(b, float)
    x = np.array(x0, float)

    if not (A.ndim == 2 and A.shape[0] == A.shape[1]):
        raise ValueError("La matriz A debe ser cuadrada.")
    if error_type.lower() not in ('absoluto', 'relativo'):
        raise ValueError("error_type debe ser 'absoluto' o 'relativo'.")

    historial = []
    datos = []

    for k in range(1, int(niter)+1):
        x_new = x.copy()
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (1 - w)*x[i] + (w / A[i, i])*(b[i] - s1 - s2)
        if error_type.lower() == 'absoluto':
            E = np.linalg.norm(x_new - x, ord=np.inf)
        else:
            E = np.linalg.norm((x_new - x) / x_new, ord=np.inf)
        historial.append((k, x_new.copy(), E))
        datos.append(x_new.copy())
        x = x_new
        if E < Tol:
            break

    # Gráfica
    datos = np.array(datos)
    plt.figure()
    for i in range(datos.shape[1]):
        plt.plot(range(1, datos.shape[0]+1), datos[:, i], '-o', linewidth=1.5, label=f'x{i+1}')
    plt.xlabel('Iteración')
    plt.ylabel('Valor de las variables')
    plt.title('Evolución de las variables por iteración (Método SOR)')
    plt.legend(loc='best')
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