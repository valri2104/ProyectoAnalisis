import numpy as np
import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def regla_falsa(f, xi, xs, Tol, niter, error_type):
    # Paso 1
    if Tol <= 0: raise ValueError("La tolerancia debe ser positiva.")
    if niter <= 0 or not float(niter).is_integer(): raise ValueError("niter debe ser entero positivo.")
    if error_type.lower() not in ('relativo','absoluto'): raise ValueError("error_type debe ser 'relativo' o 'absoluto'.")
    xi0, xs0 = xi, xs
    fl, fr = f(xi), f(xs)
    if fl*fr > 0: raise ValueError("No hay cambio de signo en el intervalo inicial.")
    historial = []
    for k in range(1, int(niter)+1):
        s = (xi*fr - xs*fl)/(fr - fl)
        fs = f(s)
        E = abs(fs) if error_type=='absoluto' else abs((xs-xi)/2)
        historial.append((k,s,fs,E))
        if fs==0 or E<Tol: break
        if fl*fs<0:
            xs, fr = s, fs
        else:
            xi, fl = s, fs

    # Gráfica
    x_vals = np.linspace(xi0, xs0, 100)
    y_vals = np.array([f(x) for x in x_vals])
    plt.figure()
    plt.plot(x_vals,y_vals,linewidth=2); plt.axhline(0,linestyle='--')
    plt.plot(s,f(s),'ro',markersize=6)
    plt.title('Regla Falsa'); plt.xlabel('x'); plt.ylabel('f(x)'); plt.grid(True)
    buf=io.BytesIO(); plt.savefig(buf,format='png'); plt.close(); buf.seek(0)
    img_base64=base64.b64encode(buf.read()).decode('ascii')

    return {'s':s,'E':E,'fm':f(s),'historial':historial,'grafica_base64':img_base64}