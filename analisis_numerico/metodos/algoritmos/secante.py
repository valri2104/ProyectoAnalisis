import numpy as np
import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def secante(f, x0, x1, Tol, niter, error_type):
    # Paso 1
    if Tol<=0: raise ValueError("Tol debe ser positiva.")
    if niter<=0 or not float(niter).is_integer(): raise ValueError("niter entero positivo.")
    if error_type.lower() not in ('relativo','absoluto'): raise ValueError("error_type inválido.")
    x0, x1 = x0, x1
    historial=[]
    for k in range(1,int(niter)+1):
        f0, f1 = f(x0), f(x1)
        x2 = x1 - f1*(x1-x0)/(f1-f0)
        f2 = f(x2)
        E = abs(f2) if error_type=='absoluto' else abs((x2-x1))
        historial.append((k,x2,f2,E))
        if f2==0 or E<Tol: break
        x0, x1 = x1, x2

    # Gráfica
    xs = np.linspace(min(x0,x1),max(x0,x1),100)
    ys = np.array([f(x) for x in xs])
    plt.figure(); plt.plot(xs,ys,linewidth=2); plt.axhline(0,linestyle='--')
    plt.plot(x2,f2,'ro',markersize=6); plt.title('Método de la Secante')
    plt.xlabel('x'); plt.ylabel('f(x)'); plt.grid(True)
    buf=io.BytesIO(); plt.savefig(buf,format='png'); plt.close(); buf.seek(0)
    img_base64=base64.b64encode(buf.read()).decode('ascii')

    return {'x':x2,'E':E,'fm':f2,'historial':historial,'grafica_base64':img_base64}