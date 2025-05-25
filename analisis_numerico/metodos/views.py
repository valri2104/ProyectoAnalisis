from django.shortcuts import render
from .algoritmos import (
    biseccion, secante, regla_falsa, raices_multiples,
    sor, punto_fijo,  newton, metodo_grafico,
    jacobi, gauss_seidel
)

def vista_biseccion(request):
    resultado=None
    if request.method=='POST':
        f=lambda x: eval(request.POST['f'])
        resultado=biseccion(f,float(request.POST['xi']),float(request.POST['xs']),
                            float(request.POST['Tol']),int(request.POST['niter']),
                            request.POST['error_type'])
    return render(request,'biseccion.html',{'resultado':resultado})

def vista_regla_falsa(request):
    resultado=None
    if request.method=='POST':
        f=lambda x: eval(request.POST['f'])
        resultado=regla_falsa(f,float(request.POST['xi']),float(request.POST['xs']),
                                 float(request.POST['Tol']),int(request.POST['niter']),
                                 request.POST['error_type'])
    return render(request,'regla_falsa.html',{'resultado':resultado})

def vista_secante(request):
    resultado=None
    if request.method=='POST':
        f=lambda x: eval(request.POST['f'])
        resultado=secante(f,float(request.POST['x0']),float(request.POST['x1']),
                          float(request.POST['Tol']),int(request.POST['niter']),
                          request.POST['error_type'])
    return render(request,'secante.html',{'resultado':resultado})

def vista_newton(request):
    resultado=None
    if request.method=='POST':
        f=lambda x: eval(request.POST['f'])
        df=lambda x: eval(request.POST['df'])
        resultado=newton(f,df,float(request.POST['x0']),
                        float(request.POST['Tol']),int(request.POST['niter']),
                        request.POST['error_type'])
    return render(request,'newton.html',{'resultado':resultado})

def vista_raices_multiples(request):
    resultado=None
    if request.method=='POST':
        f=lambda x: eval(request.POST['f'])
        df=lambda x: eval(request.POST['df'])
        d2f=lambda x: eval(request.POST['d2f'])
        resultado=raices_multiples(f,df,d2f,float(request.POST['x0']),
                                   float(request.POST['Tol']),int(request.POST['niter']),
                                   request.POST['error_type'])
    return render(request,'raices_multiples.html',{'resultado':resultado})

def vista_punto_fijo(request):
    resultado=None
    if request.method=='POST':
        g=lambda x: eval(request.POST['g'])
        resultado=punto_fijo(g,float(request.POST['x0']),
                             float(request.POST['Tol']),int(request.POST['niter']),
                             request.POST['error_type'])
    return render(request,'punto_fijo.html',{'resultado':resultado})

def vista_jacobi(request):
    resultado=None
    if request.method=='POST':
        A=eval(request.POST['A']); b=eval(request.POST['b']); x0=eval(request.POST['x0'])
        resultado=jacobi(A,b,x0,float(request.POST['Tol']),int(request.POST['niter']), request.POST['error_type'])
    return render(request,'jacobi.html',{'resultado':resultado})

def vista_gauss_seidel(request):
    resultado=None
    if request.method=='POST':
        A=eval(request.POST['A']); b=eval(request.POST['b']); x0=eval(request.POST['x0'])
        resultado=gauss_seidel(A,b,x0,float(request.POST['Tol']),int(request.POST['niter']), request.POST['error_type'])
    return render(request,'gauss_seidel.html',{'resultado':resultado})

def vista_sor(request):
    resultado=None
    if request.method=='POST':
        A=eval(request.POST['A']); b=eval(request.POST['b']); x0=eval(request.POST['x0'])
        resultado=sor(A,b,x0,float(request.POST['Tol']),int(request.POST['niter']),
                     float(request.POST['omega']), request.POST['error_type'])
    return render(request,'sor.html',{'resultado':resultado})

def vista_metodo_grafico(request):
    resultado=None
    if request.method=='POST':
        f=lambda x: eval(request.POST['f'])
        resultado=metodo_grafico(f,float(request.POST['A']),float(request.POST['b']), float(request.POST['Tol']),
                                 int(request.POST['niter']), request.POST['error_type'])
    return render(request,'metodo_grafico.html',{'resultado':resultado})