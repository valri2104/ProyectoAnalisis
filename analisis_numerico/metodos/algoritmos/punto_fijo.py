import numpy as np
import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def punto_fijo(g, x0, Tol, niter, error_type):
    # Paso 1
    if Tol<=0: raise ValueError("Tol positiva.")
    if niter<=0 or not float(niter).is_integer(): raise ValueError("niter entero positivo.")
    if error_type.lower() not in ('relativo','absoluto'): raise ValueError("error_type inválido.")
    x = x0
    historial=[]
    for k in range(1,int(niter)+1):
        x_new = g(x)
        E = abs(x_new-x) if error_type=='absoluto' else abs((x_new-x)/x_new)
        historial.append((k,x_new,E))
        x = x_new
        if E<Tol: break

    # Gráfica
    xs = np.linspace(x0-1,x0+1,100)
    ys = np.array([g(xi) for xi in xs])
    plt.figure(); plt.plot(xs,ys,linewidth=2)
    plt.plot(xs,xs,'--'); plt.plot(x,x,'ro',markersize=6)
    plt.title('Método de Punto Fijo'); plt.xlabel('x'); plt.ylabel('g(x)'); plt.grid(True)
    buf=io.BytesIO(); plt.savefig(buf,format='png'); plt.close(); buf.seek(0)
    img_base64=base64.b64encode(buf.read()).decode('ascii')

    return {'x':x,'E':E,'historial':historial,'grafica_base64':img_base64}