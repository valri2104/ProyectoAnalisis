import numpy as np
import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def newton(f, df, x0, Tol, niter, error_type):
    # Paso 1
    if Tol<=0: raise ValueError("Tol debe ser positiva.")
    if niter<=0 or not float(niter).is_integer(): raise ValueError("niter entero positivo.")
    if error_type.lower() not in ('relativo','absoluto'): raise ValueError("error_type inválido.")
    x = x0
    historial=[]
    for k in range(1,int(niter)+1):
        fx, dfx = f(x), df(x)
        if dfx==0: raise ZeroDivisionError("df(x)=0.")
        x_new = x - fx/dfx
        E = abs(fx) if error_type=='absoluto' else abs(x_new-x)
        historial.append((k,x_new,f(x_new),E))
        x = x_new
        if f(x)==0 or E<Tol: break

    # Gráfica
    xs = np.linspace(x0-1,x0+1,100)
    ys = np.array([f(xi) for xi in xs])
    plt.figure(); plt.plot(xs,ys,linewidth=2); plt.axhline(0,linestyle='--')
    plt.plot(x,f(x),'ro',markersize=6); plt.title('Método de Newton')
    plt.xlabel('x'); plt.ylabel('f(x)'); plt.grid(True)
    buf=io.BytesIO(); plt.savefig(buf,format='png'); plt.close(); buf.seek(0)
    img_base64=base64.b64encode(buf.read()).decode('ascii')

    return {'x':x,'E':E,'fm':f(x),'historial':historial,'grafica_base64':img_base64}