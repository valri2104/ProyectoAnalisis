import numpy as np
import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def newton(f, df, x0, Tol, niter, error_type):
    # Paso 1: Validaciones
    if Tol <= 0:
        raise ValueError("La tolerancia debe ser positiva.")
    if niter <= 0 or not float(niter).is_integer():
        raise ValueError("niter debe ser un entero positivo.")
    if error_type.lower() not in ('relativo', 'absoluto'):
        raise ValueError("error_type debe ser 'relativo' o 'absoluto'.")

    # Verificar condiciones iniciales
    try:
        fx0 = f(x0)
        dfx0 = df(x0)
    except Exception as e:
        raise ValueError(f"Error al evaluar la función o su derivada en x0: {str(e)}")

    if abs(dfx0) < 1e-10:
        raise ValueError("La derivada en el punto inicial es muy cercana a cero.")

    x = x0
    historial = []
    convergencia = False

    for k in range(1, int(niter)+1):
        try:
            fx = f(x)
            dfx = df(x)
            
            if abs(dfx) < 1e-10:
                raise ValueError(f"La derivada se anula en la iteración {k}.")
            
            x_new = x - fx/dfx
            
            if error_type == 'absoluto':
                E = abs(fx)
            else:
                E = abs((x_new - x)/x_new) if x_new != 0 else abs(x_new - x)
            
            historial.append((k, x_new, fx, E))
            x = x_new
            
            if abs(fx) < Tol or E < Tol:
                convergencia = True
                break
                
        except Exception as e:
            raise ValueError(f"Error en la iteración {k}: {str(e)}")

    if not convergencia:
        raise ValueError("El método no convergió en el número máximo de iteraciones.")

    # Gráfica
    try:
        # Determinar el rango de la gráfica
        x_min = min(x0, x) - 1
        x_max = max(x0, x) + 1
        xs = np.linspace(x_min, x_max, 100)
        ys = np.array([f(xi) for xi in xs])
        
        plt.figure(figsize=(10, 6))
        plt.plot(xs, ys, 'b-', linewidth=2, label='f(x)')
        plt.axhline(0, color='r', linestyle='--', label='y=0')
        plt.plot(x, f(x), 'go', markersize=8, label='Raíz')
        
        # Marcar el punto inicial
        plt.plot(x0, f(x0), 'ro', markersize=6, label='x0')
        
        plt.title('Método de Newton')
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
        'x': x,
        'E': E,
        'fm': f(x),
        'historial': historial,
        'grafica_base64': img_base64,
        'iteraciones': k,
        'convergencia': convergencia
    }