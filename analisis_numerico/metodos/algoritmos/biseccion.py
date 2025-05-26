import numpy as np
import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def biseccion(f, xi, xs, Tol, niter, error_type):
    # Paso 1: Validaciones
    if Tol <= 0:
        raise ValueError("La tolerancia debe ser positiva.")
    if niter <= 0 or not float(niter).is_integer():
        raise ValueError("niter debe ser un entero positivo.")
    if error_type.lower() not in ('relativo', 'absoluto'):
        raise ValueError("El tipo de error debe ser 'relativo' o 'absoluto'.")
    if xi >= xs:
        raise ValueError("El límite inferior debe ser menor que el límite superior.")

    # Verificar condiciones iniciales
    try:
        fl = f(xi)
        fr = f(xs)
    except Exception as e:
        raise ValueError(f"Error al evaluar la función en los límites: {str(e)}")

    if fl * fr > 0:
        raise ValueError("No hay cambio de signo en el intervalo inicial.")
    if abs(fl) < Tol:
        return {
            's': xi,
            'E': 0,
            'fm': fl,
            'historial': [(0, xi, fl, 0)],
            'grafica_base64': None,
            'iteraciones': 0,
            'convergencia': True
        }
    if abs(fr) < Tol:
        return {
            's': xs,
            'E': 0,
            'fm': fr,
            'historial': [(0, xs, fr, 0)],
            'grafica_base64': None,
            'iteraciones': 0,
            'convergencia': True
        }

    xi0, xs0 = xi, xs
    s = xi
    historial = []
    convergencia = False

    for k in range(1, int(niter)+1):
        s = (xi + xs) / 2
        try:
            fs = f(s)
        except Exception as e:
            raise ValueError(f"Error al evaluar la función en la iteración {k}: {str(e)}")

        if error_type.lower() == 'absoluto':
            E = abs(fs)
        else:
            E = abs((xs - xi) / 2)

        historial.append((k, s, fs, E))

        if abs(fs) < Tol or E < Tol:
            convergencia = True
            break

        if fl * fs < 0:
            xs = s
            fr = fs
        else:
            xi = s
            fl = fs

    if not convergencia:
        raise ValueError("El método no convergió en el número máximo de iteraciones.")

    # Gráfica
    try:
        x_vals = np.linspace(xi0, xs0, 100)
        y_vals = np.array([f(x) for x in x_vals])
        
        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_vals, 'b-', linewidth=2, label='f(x)')
        plt.axhline(0, color='r', linestyle='--', label='y=0')
        plt.plot(s, f(s), 'go', markersize=8, label='Raíz')
        
        # Marcar los puntos iniciales
        plt.plot(xi0, f(xi0), 'ro', markersize=6, label='xi')
        plt.plot(xs0, f(xs0), 'ro', markersize=6, label='xs')
        
        plt.title('Método de Bisección')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.legend()
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=300, bbox_inches='tight')
        plt.close()
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode('ascii')
    except Exception as e:
        img_base64 = None
        print(f"Error al generar la gráfica: {str(e)}")

    return {
        's': s,
        'E': E,
        'fm': f(s),
        'historial': historial,
        'grafica_base64': img_base64,
        'iteraciones': k,
        'convergencia': convergencia
    }