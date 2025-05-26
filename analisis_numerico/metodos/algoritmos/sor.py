import numpy as np
import matplotlib.pyplot as plt

def sor(x0, A, b, Tol, niter, w, tipo_error):
    try:
        # Validaciones básicas
        A = np.array(A, dtype=float)
        b = np.array(b, dtype=float).flatten()
        x0 = np.array(x0, dtype=float).flatten()

        n, m = A.shape
        if n != m:
            raise ValueError("La matriz A debe ser cuadrada.")
        if b.size != n:
            raise ValueError("El vector b debe tener la misma longitud que A.")
        if x0.size != n:
            raise ValueError("El vector inicial x0 debe tener la misma longitud que b.")
        if Tol <= 0:
            raise ValueError("La tolerancia debe ser positiva.")
        if not (0 < w < 2):
            raise ValueError("El parámetro de relajación w debe estar en el intervalo (0, 2).")
        if tipo_error not in ['absoluto', 'relativo']:
            raise ValueError("tipo_error debe ser 'absoluto' o 'relativo'.")

        x = x0.copy()
        E = []
        historial = []
        error = Tol + 1
        k = 0

        print(f"\nMétodo SOR (w = {w:.2f}) - Error {tipo_error}")
        print("-" * (13 + n * 13))
        header = "Iter".ljust(6) + "".join([f"x{i+1}".rjust(12) for i in range(n)]) + "    Error"
        print(header)
        print("-" * (13 + n * 13))

        while error > Tol and k < niter:
            x_old = x.copy()
            for i in range(n):
                sum1 = np.dot(A[i, :i], x[:i])
                sum2 = np.dot(A[i, i+1:], x_old[i+1:])
                x[i] = (1 - w) * x_old[i] + (w / A[i, i]) * (b[i] - sum1 - sum2)

            # Calcular error
            if tipo_error == 'absoluto':
                error = np.linalg.norm(x - x_old, ord=np.inf)
            else:
                denom = np.linalg.norm(x, ord=np.inf)
                error = np.linalg.norm(x - x_old, ord=np.inf) / (denom if denom > 0 else np.finfo(float).eps)

            E.append(error)
            historial.append(x.copy())

            row = f"{k+1:<6}" + "".join([f"{xi:12.6f}" for xi in x]) + f" {error:12.2e}"
            print(row)
            k += 1

        print("-" * (13 + n * 13))

        if error <= Tol:
            print(f"Convergencia lograda en {k} iteraciones con tolerancia {Tol:.2e}.")
        else:
            print(f"No se alcanzó la tolerancia después de {niter} iteraciones.")

        print("\nVector solución aproximada:")
        for i, xi in enumerate(x):
            print(f"x{i+1} = {xi:.10f}")

        # Graficar evolución
        historial = np.array(historial)
        plt.figure(figsize=(8, 5))
        for i in range(n):
            plt.plot(range(1, k+1), historial[:, i], '-o', label=f'x{i+1}', linewidth=1.5)
        plt.grid(True)
        plt.xlabel('Iteración')
        plt.ylabel('Valor de las variables')
        plt.title('Evolución de las variables por iteración (Método SOR)')
        plt.legend()
        plt.tight_layout()
        plt.show()

        return E, x

    except Exception as e:
        print(f"\nError: {e}")
        return [], []