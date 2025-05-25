import numpy as np

def gauss_seidel(x0, A, b, Tol, niter, error_type):
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

    for k in range(1, int(niter)+1):
        x_new = x.copy()
        for i in range(n):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if error_type.lower() == 'absoluto':
            E = np.linalg.norm(x_new - x, ord=np.inf)
        else:
            E = np.linalg.norm((x_new - x) / x_new, ord=np.inf)
        historial.append((k, x_new.copy(), E))
        x = x_new
        if E < Tol:
            break

    return {
        'x': x.tolist(),
        'historial': historial
    }