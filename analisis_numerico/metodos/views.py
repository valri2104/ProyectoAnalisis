from django.shortcuts import render
from django.contrib import messages
from .algoritmos import (
    biseccion, secante, regla_falsa, raices_multiples,
    sor, punto_fijo,  newton, metodo_grafico,
    jacobi, gauss_seidel, lagrange, spline_cubico, spline_lineal, vandermonde, newtonint
)
import time
import numpy as np

def home(request):
    return render(request, 'home.html')

def validate_function(func_str, var='x'):
    try:
        # Test the function with a sample value
        test_func = lambda x: eval(func_str)
        test_func(1.0)
        return True
    except Exception as e:
        return False

def validate_matrix(matrix_str):
    try:
        matrix = eval(matrix_str)
        if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            return False
        if not all(len(row) == len(matrix[0]) for row in matrix):
            return False
        return True
    except:
        return False

def validate_vector(vector_str):
    try:
        vector = eval(vector_str)
        return isinstance(vector, list) and all(isinstance(x, (int, float)) for x in vector)
    except:
        return False

def vista_biseccion(request):
    if request.method == 'POST':
        try:
            f_str = request.POST['f']
            if not validate_function(f_str):
                messages.error(request, 'La función ingresada no es válida. Use la sintaxis de Python (ej: x**2 - 4)')
                return render(request, 'biseccion.html', {
                    'f': f_str,
                    'xi': request.POST['xi'],
                    'xs': request.POST['xs'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            f = lambda x: eval(f_str)
            xi = float(request.POST['xi'])
            xs = float(request.POST['xs'])
            tol = float(request.POST['Tol'])
            niter = int(request.POST['niter'])
            error_type = request.POST['error_type']

            if xi >= xs:
                messages.error(request, 'El valor de xi debe ser menor que xs')
                return render(request, 'biseccion.html', {
                    'f': f_str,
                    'xi': request.POST['xi'],
                    'xs': request.POST['xs'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            if tol <= 0:
                messages.error(request, 'La tolerancia debe ser un número positivo')
                return render(request, 'biseccion.html', {
                    'f': f_str,
                    'xi': request.POST['xi'],
                    'xs': request.POST['xs'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            if niter <= 0:
                messages.error(request, 'El número de iteraciones debe ser positivo')
                return render(request, 'biseccion.html', {
                    'f': f_str,
                    'xi': request.POST['xi'],
                    'xs': request.POST['xs'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            resultado = biseccion(f, xi, xs, tol, niter, error_type)
            messages.success(request, 'Cálculo completado exitosamente')
            return render(request, 'biseccion.html', {
                'resultado': resultado,
                'f': f_str,
                'xi': request.POST['xi'],
                'xs': request.POST['xs'],
                'Tol': request.POST['Tol'],
                'niter': request.POST['niter'],
                'error_type': request.POST['error_type']
            })

        except ValueError as e:
            messages.error(request, str(e))
            return render(request, 'biseccion.html', {
                'f': request.POST.get('f', ''),
                'xi': request.POST.get('xi', ''),
                'xs': request.POST.get('xs', ''),
                'Tol': request.POST.get('Tol', ''),
                'niter': request.POST.get('niter', ''),
                'error_type': request.POST.get('error_type', '')
            })
        except Exception as e:
            messages.error(request, 'Ocurrió un error al procesar los datos. Verifique que todos los campos sean correctos.')
            return render(request, 'biseccion.html', {
                'f': request.POST.get('f', ''),
                'xi': request.POST.get('xi', ''),
                'xs': request.POST.get('xs', ''),
                'Tol': request.POST.get('Tol', ''),
                'niter': request.POST.get('niter', ''),
                'error_type': request.POST.get('error_type', '')
            })
    
    return render(request, 'biseccion.html')

def vista_regla_falsa(request):
    if request.method == 'POST':
        try:
            f_str = request.POST['f']
            
            if not validate_function(f_str):
                messages.error(request, 'La función f(x) no es válida. Use la sintaxis de Python (ej: x**2 - 4)')
                return render(request, 'regla_falsa.html', {
                    'f': f_str,
                    'xi': request.POST['xi'],
                    'xs': request.POST['xs'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            f = lambda x: eval(f_str)
            xi = float(request.POST['xi'])
            xs = float(request.POST['xs'])
            tol = float(request.POST['Tol'])
            niter = int(request.POST['niter'])
            error_type = request.POST['error_type']

            if tol <= 0:
                messages.error(request, 'La tolerancia debe ser un número positivo')
                return render(request, 'regla_falsa.html', {
                    'f': f_str,
                    'xi': request.POST['xi'],
                    'xs': request.POST['xs'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            if niter <= 0:
                messages.error(request, 'El número de iteraciones debe ser positivo')
                return render(request, 'regla_falsa.html', {
                    'f': f_str,
                    'xi': request.POST['xi'],
                    'xs': request.POST['xs'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            resultado = regla_falsa(f, xi, xs, tol, niter, error_type)
            messages.success(request, 'Cálculo completado exitosamente')
            return render(request, 'regla_falsa.html', {
                'resultado': resultado,
                'f': f_str,
                'xi': request.POST['xi'],
                'xs': request.POST['xs'],
                'Tol': request.POST['Tol'],
                'niter': request.POST['niter'],
                'error_type': request.POST['error_type']
            })

        except ValueError as e:
            messages.error(request, str(e))
            return render(request, 'regla_falsa.html', {
                'f': request.POST.get('f', ''),
                'xi': request.POST.get('xi', ''),
                'xs': request.POST.get('xs', ''),
                'Tol': request.POST.get('Tol', ''),
                'niter': request.POST.get('niter', ''),
                'error_type': request.POST.get('error_type', '')
            })
        except Exception as e:
            messages.error(request, 'Ocurrió un error al procesar los datos. Verifique que todos los campos sean correctos.')
            return render(request, 'regla_falsa.html', {
                'f': request.POST.get('f', ''),
                'xi': request.POST.get('xi', ''),
                'xs': request.POST.get('xs', ''),
                'Tol': request.POST.get('Tol', ''),
                'niter': request.POST.get('niter', ''),
                'error_type': request.POST.get('error_type', '')
            })
    
    return render(request, 'regla_falsa.html')

def vista_secante(request):
    if request.method == 'POST':
        try:
            f_str = request.POST['f']
            
            if not validate_function(f_str):
                messages.error(request, 'La función f(x) no es válida. Use la sintaxis de Python (ej: x**2 - 4)')
                return render(request, 'secante.html', {
                    'f': f_str,
                    'x0': request.POST['x0'],
                    'x1': request.POST['x1'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            f = lambda x: eval(f_str)
            x0 = float(request.POST['x0'])
            x1 = float(request.POST['x1'])
            tol = float(request.POST['Tol'])
            niter = int(request.POST['niter'])
            error_type = request.POST['error_type']

            if tol <= 0:
                messages.error(request, 'La tolerancia debe ser un número positivo')
                return render(request, 'secante.html', {
                    'f': f_str,
                    'x0': request.POST['x0'],
                    'x1': request.POST['x1'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            if niter <= 0:
                messages.error(request, 'El número de iteraciones debe ser positivo')
                return render(request, 'secante.html', {
                    'f': f_str,
                    'x0': request.POST['x0'],
                    'x1': request.POST['x1'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            resultado = secante(f, x0, x1, tol, niter, error_type)
            messages.success(request, 'Cálculo completado exitosamente')
            return render(request, 'secante.html', {
                'resultado': resultado,
                'f': f_str,
                'x0': request.POST['x0'],
                'x1': request.POST['x1'],
                'Tol': request.POST['Tol'],
                'niter': request.POST['niter'],
                'error_type': request.POST['error_type']
            })

        except ValueError as e:
            messages.error(request, str(e))
            return render(request, 'secante.html', {
                'f': request.POST.get('f', ''),
                'x0': request.POST.get('x0', ''),
                'x1': request.POST.get('x1', ''),
                'Tol': request.POST.get('Tol', ''),
                'niter': request.POST.get('niter', ''),
                'error_type': request.POST.get('error_type', '')
            })
        except Exception as e:
            messages.error(request, 'Ocurrió un error al procesar los datos. Verifique que todos los campos sean correctos.')
            return render(request, 'secante.html', {
                'f': request.POST.get('f', ''),
                'x0': request.POST.get('x0', ''),
                'x1': request.POST.get('x1', ''),
                'Tol': request.POST.get('Tol', ''),
                'niter': request.POST.get('niter', ''),
                'error_type': request.POST.get('error_type', '')
            })
    
    return render(request, 'secante.html')

def vista_newton(request):
    if request.method == 'POST':
        try:
            f_str = request.POST['f']
            df_str = request.POST['df']
            
            if not validate_function(f_str):
                messages.error(request, 'La función f(x) no es válida. Use la sintaxis de Python (ej: x**2 - 4)')
                return render(request, 'newton.html', {
                    'f': f_str,
                    'df': df_str,
                    'x0': request.POST['x0'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })
            
            if not validate_function(df_str):
                messages.error(request, 'La derivada f\'(x) no es válida. Use la sintaxis de Python (ej: 2*x)')
                return render(request, 'newton.html', {
                    'f': f_str,
                    'df': df_str,
                    'x0': request.POST['x0'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            f = lambda x: eval(f_str)
            df = lambda x: eval(df_str)
            x0 = float(request.POST['x0'])
            tol = float(request.POST['Tol'])
            niter = int(request.POST['niter'])
            error_type = request.POST['error_type']

            if tol <= 0:
                messages.error(request, 'La tolerancia debe ser un número positivo')
                return render(request, 'newton.html', {
                    'f': f_str,
                    'df': df_str,
                    'x0': request.POST['x0'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            if niter <= 0:
                messages.error(request, 'El número de iteraciones debe ser positivo')
                return render(request, 'newton.html', {
                    'f': f_str,
                    'df': df_str,
                    'x0': request.POST['x0'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            resultado = newton(f, df, x0, tol, niter, error_type)
            messages.success(request, 'Cálculo completado exitosamente')
            return render(request, 'newton.html', {
                'resultado': resultado,
                'f': f_str,
                'df': df_str,
                'x0': request.POST['x0'],
                'Tol': request.POST['Tol'],
                'niter': request.POST['niter'],
                'error_type': request.POST['error_type']
            })

        except ValueError as e:
            messages.error(request, str(e))
            return render(request, 'newton.html', {
                'f': request.POST.get('f', ''),
                'df': request.POST.get('df', ''),
                'x0': request.POST.get('x0', ''),
                'Tol': request.POST.get('Tol', ''),
                'niter': request.POST.get('niter', ''),
                'error_type': request.POST.get('error_type', '')
            })
        except Exception as e:
            messages.error(request, 'Ocurrió un error al procesar los datos. Verifique que todos los campos sean correctos.')
            return render(request, 'newton.html', {
                'f': request.POST.get('f', ''),
                'df': request.POST.get('df', ''),
                'x0': request.POST.get('x0', ''),
                'Tol': request.POST.get('Tol', ''),
                'niter': request.POST.get('niter', ''),
                'error_type': request.POST.get('error_type', '')
            })
    
    return render(request, 'newton.html')

def vista_raices_multiples(request):
    if request.method == 'POST':
        try:
            f_str = request.POST['f']
            df_str = request.POST['df']
            d2f_str = request.POST['d2f']
            
            if not validate_function(f_str):
                messages.error(request, 'La función f(x) no es válida. Use la sintaxis de Python (ej: (x-1)**3)')
                return render(request, 'raices_multiples.html', {
                    'f': f_str,
                    'df': df_str,
                    'd2f': d2f_str,
                    'x0': request.POST['x0'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })
            
            if not validate_function(df_str):
                messages.error(request, 'La primera derivada f\'(x) no es válida. Use la sintaxis de Python (ej: 3*(x-1)**2)')
                return render(request, 'raices_multiples.html', {
                    'f': f_str,
                    'df': df_str,
                    'd2f': d2f_str,
                    'x0': request.POST['x0'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })
            
            if not validate_function(d2f_str):
                messages.error(request, 'La segunda derivada f\'\'(x) no es válida. Use la sintaxis de Python (ej: 6*(x-1))')
                return render(request, 'raices_multiples.html', {
                    'f': f_str,
                    'df': df_str,
                    'd2f': d2f_str,
                    'x0': request.POST['x0'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            f = lambda x: eval(f_str)
            df = lambda x: eval(df_str)
            d2f = lambda x: eval(d2f_str)
            x0 = float(request.POST['x0'])
            tol = float(request.POST['Tol'])
            niter = int(request.POST['niter'])
            error_type = request.POST['error_type']

            if tol <= 0:
                messages.error(request, 'La tolerancia debe ser un número positivo')
                return render(request, 'raices_multiples.html', {
                    'f': f_str,
                    'df': df_str,
                    'd2f': d2f_str,
                    'x0': request.POST['x0'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            if niter <= 0:
                messages.error(request, 'El número de iteraciones debe ser positivo')
                return render(request, 'raices_multiples.html', {
                    'f': f_str,
                    'df': df_str,
                    'd2f': d2f_str,
                    'x0': request.POST['x0'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            resultado = raices_multiples(f, df, d2f, x0, tol, niter, error_type)
            messages.success(request, 'Cálculo completado exitosamente')
            return render(request, 'raices_multiples.html', {
                'resultado': resultado,
                'f': f_str,
                'df': df_str,
                'd2f': d2f_str,
                'x0': request.POST['x0'],
                'Tol': request.POST['Tol'],
                'niter': request.POST['niter'],
                'error_type': request.POST['error_type']
            })

        except ValueError as e:
            messages.error(request, str(e))
            return render(request, 'raices_multiples.html', {
                'f': request.POST.get('f', ''),
                'df': request.POST.get('df', ''),
                'd2f': request.POST.get('d2f', ''),
                'x0': request.POST.get('x0', ''),
                'Tol': request.POST.get('Tol', ''),
                'niter': request.POST.get('niter', ''),
                'error_type': request.POST.get('error_type', '')
            })
        except Exception as e:
            messages.error(request, 'Ocurrió un error al procesar los datos. Verifique que todos los campos sean correctos.')
            return render(request, 'raices_multiples.html', {
                'f': request.POST.get('f', ''),
                'df': request.POST.get('df', ''),
                'd2f': request.POST.get('d2f', ''),
                'x0': request.POST.get('x0', ''),
                'Tol': request.POST.get('Tol', ''),
                'niter': request.POST.get('niter', ''),
                'error_type': request.POST.get('error_type', '')
            })
    
    return render(request, 'raices_multiples.html')

def vista_punto_fijo(request):
    if request.method == 'POST':
        try:
            g_str = request.POST['g']
            if not validate_function(g_str):
                messages.error(request, 'La función g(x) no es válida. Use la sintaxis de Python (ej: (x + 2/x)/2)')
                return render(request, 'punto_fijo.html', {
                    'g': g_str,
                    'x0': request.POST['x0'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            g = lambda x: eval(g_str)
            x0 = float(request.POST['x0'])
            tol = float(request.POST['Tol'])
            niter = int(request.POST['niter'])
            error_type = request.POST['error_type']

            if tol <= 0:
                messages.error(request, 'La tolerancia debe ser un número positivo')
                return render(request, 'punto_fijo.html', {
                    'g': g_str,
                    'x0': request.POST['x0'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            if niter <= 0:
                messages.error(request, 'El número de iteraciones debe ser positivo')
                return render(request, 'punto_fijo.html', {
                    'g': g_str,
                    'x0': request.POST['x0'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            resultado = punto_fijo(g, x0, tol, niter, error_type)
            messages.success(request, 'Cálculo completado exitosamente')
            return render(request, 'punto_fijo.html', {
                'resultado': resultado,
                'g': g_str,
                'x0': request.POST['x0'],
                'Tol': request.POST['Tol'],
                'niter': request.POST['niter'],
                'error_type': request.POST['error_type']
            })

        except ValueError as e:
            messages.error(request, str(e))
            return render(request, 'punto_fijo.html', {
                'g': request.POST.get('g', ''),
                'x0': request.POST.get('x0', ''),
                'Tol': request.POST.get('Tol', ''),
                'niter': request.POST.get('niter', ''),
                'error_type': request.POST.get('error_type', '')
            })
        except Exception as e:
            messages.error(request, 'Ocurrió un error al procesar los datos. Verifique que todos los campos sean correctos.')
            return render(request, 'punto_fijo.html', {
                'g': request.POST.get('g', ''),
                'x0': request.POST.get('x0', ''),
                'Tol': request.POST.get('Tol', ''),
                'niter': request.POST.get('niter', ''),
                'error_type': request.POST.get('error_type', '')
            })
    
    return render(request, 'punto_fijo.html')

def vista_jacobi(request):
    if request.method == 'POST':
        try:
            A_str = request.POST['A']
            b_str = request.POST['b']
            x0_str = request.POST['x0']

            if not validate_matrix(A_str):
                messages.error(request, 'La matriz A no es válida. Ingrese una matriz cuadrada en formato Python (ej: [[4,1],[1,3]])')
                return render(request, 'jacobi.html', {
                    'A': A_str,
                    'b': b_str,
                    'x0': x0_str,
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            if not validate_vector(b_str):
                messages.error(request, 'El vector b no es válido. Ingrese un vector en formato Python (ej: [1,2])')
                return render(request, 'jacobi.html', {
                    'A': A_str,
                    'b': b_str,
                    'x0': x0_str,
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            if not validate_vector(x0_str):
                messages.error(request, 'El vector x0 no es válido. Ingrese un vector en formato Python (ej: [0,0])')
                return render(request, 'jacobi.html', {
                    'A': A_str,
                    'b': b_str,
                    'x0': x0_str,
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            A = eval(A_str)
            b = eval(b_str)
            x0 = eval(x0_str)
            tol = float(request.POST['Tol'])
            niter = int(request.POST['niter'])
            error_type = request.POST['error_type']

            if len(A) != len(b) or len(A) != len(x0):
                messages.error(request, 'Las dimensiones de la matriz A y los vectores b y x0 deben coincidir')
                return render(request, 'jacobi.html', {
                    'A': A_str,
                    'b': b_str,
                    'x0': x0_str,
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            if tol <= 0:
                messages.error(request, 'La tolerancia debe ser un número positivo')
                return render(request, 'jacobi.html', {
                    'A': A_str,
                    'b': b_str,
                    'x0': x0_str,
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            if niter <= 0:
                messages.error(request, 'El número de iteraciones debe ser positivo')
                return render(request, 'jacobi.html', {
                    'A': A_str,
                    'b': b_str,
                    'x0': x0_str,
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            resultado = jacobi(x0, A, b, tol, niter, error_type)
            messages.success(request, 'Cálculo completado exitosamente')
            return render(request, 'jacobi.html', {
                'resultado': resultado,
                'A': A_str,
                'b': b_str,
                'x0': x0_str,
                'Tol': request.POST['Tol'],
                'niter': request.POST['niter'],
                'error_type': request.POST['error_type']
            })

        except ValueError as e:
            messages.error(request, str(e))
            return render(request, 'jacobi.html', {
                'A': request.POST.get('A', ''),
                'b': request.POST.get('b', ''),
                'x0': request.POST.get('x0', ''),
                'Tol': request.POST.get('Tol', ''),
                'niter': request.POST.get('niter', ''),
                'error_type': request.POST.get('error_type', '')
            })
        except Exception as e:
            messages.error(request, 'Ocurrió un error al procesar los datos. Verifique que todos los campos sean correctos.')
            return render(request, 'jacobi.html', {
                'A': request.POST.get('A', ''),
                'b': request.POST.get('b', ''),
                'x0': request.POST.get('x0', ''),
                'Tol': request.POST.get('Tol', ''),
                'niter': request.POST.get('niter', ''),
                'error_type': request.POST.get('error_type', '')
            })
    
    return render(request, 'jacobi.html')

def vista_gauss_seidel(request):
    if request.method == 'POST':
        try:
            A_str = request.POST['A']
            b_str = request.POST['b']
            x0_str = request.POST['x0']

            if not validate_matrix(A_str):
                messages.error(request, 'La matriz A no es válida. Ingrese una matriz cuadrada en formato Python (ej: [[4,1],[1,3]])')
                return render(request, 'gauss_seidel.html', {
                    'A': A_str,
                    'b': b_str,
                    'x0': x0_str,
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            if not validate_vector(b_str):
                messages.error(request, 'El vector b no es válido. Ingrese un vector en formato Python (ej: [1,2])')
                return render(request, 'gauss_seidel.html', {
                    'A': A_str,
                    'b': b_str,
                    'x0': x0_str,
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            if not validate_vector(x0_str):
                messages.error(request, 'El vector x0 no es válido. Ingrese un vector en formato Python (ej: [0,0])')
                return render(request, 'gauss_seidel.html', {
                    'A': A_str,
                    'b': b_str,
                    'x0': x0_str,
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            A = eval(A_str)
            b = eval(b_str)
            x0 = eval(x0_str)
            tol = float(request.POST['Tol'])
            niter = int(request.POST['niter'])
            error_type = request.POST['error_type']

            if len(A) != len(b) or len(A) != len(x0):
                messages.error(request, 'Las dimensiones de la matriz A y los vectores b y x0 deben coincidir')
                return render(request, 'gauss_seidel.html', {
                    'A': A_str,
                    'b': b_str,
                    'x0': x0_str,
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            if tol <= 0:
                messages.error(request, 'La tolerancia debe ser un número positivo')
                return render(request, 'gauss_seidel.html', {
                    'A': A_str,
                    'b': b_str,
                    'x0': x0_str,
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            if niter <= 0:
                messages.error(request, 'El número de iteraciones debe ser positivo')
                return render(request, 'gauss_seidel.html', {
                    'A': A_str,
                    'b': b_str,
                    'x0': x0_str,
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            resultado = gauss_seidel(x0, A, b, tol, niter, error_type)
            messages.success(request, 'Cálculo completado exitosamente')
            return render(request, 'gauss_seidel.html', {
                'resultado': resultado,
                'A': A_str,
                'b': b_str,
                'x0': x0_str,
                'Tol': request.POST['Tol'],
                'niter': request.POST['niter'],
                'error_type': request.POST['error_type']
            })

        except ValueError as e:
            messages.error(request, str(e))
            return render(request, 'gauss_seidel.html', {
                'A': request.POST.get('A', ''),
                'b': request.POST.get('b', ''),
                'x0': request.POST.get('x0', ''),
                'Tol': request.POST.get('Tol', ''),
                'niter': request.POST.get('niter', ''),
                'error_type': request.POST.get('error_type', '')
            })
        except Exception as e:
            messages.error(request, 'Ocurrió un error al procesar los datos. Verifique que todos los campos sean correctos.')
            return render(request, 'gauss_seidel.html', {
                'A': request.POST.get('A', ''),
                'b': request.POST.get('b', ''),
                'x0': request.POST.get('x0', ''),
                'Tol': request.POST.get('Tol', ''),
                'niter': request.POST.get('niter', ''),
                'error_type': request.POST.get('error_type', '')
            })
    
    return render(request, 'gauss_seidel.html')

def vista_sor(request):
    if request.method == 'POST':
        try:
            A_str = request.POST['A']
            b_str = request.POST['b']
            x0_str = request.POST['x0']
            try:
                A = eval(A_str)
                b = eval(b_str)
                x0 = eval(x0_str)
            except:
                messages.error(request, 'Error en el formato de las matrices. Use la sintaxis de Python (ej: [[1,2],[3,4]])')
                return render(request, 'sor.html', {
                    'A': A_str,
                    'b': b_str,
                    'x0': x0_str,
                    'omega': request.POST['omega'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            if not isinstance(A, list) or not isinstance(b, list) or not isinstance(x0, list):
                messages.error(request, 'Las entradas deben ser matrices y vectores en formato de lista')
                return render(request, 'sor.html', {
                    'A': A_str,
                    'b': b_str,
                    'x0': x0_str,
                    'omega': request.POST['omega'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            omega = float(request.POST['omega'])
            tol = float(request.POST['Tol'])
            niter = int(request.POST['niter'])
            error_type = request.POST['error_type']

            if omega <= 0 or omega >= 2:
                messages.error(request, 'El factor de relajación omega debe estar entre 0 y 2')
                return render(request, 'sor.html', {
                    'A': A_str,
                    'b': b_str,
                    'x0': x0_str,
                    'omega': request.POST['omega'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            if tol <= 0:
                messages.error(request, 'La tolerancia debe ser un número positivo')
                return render(request, 'sor.html', {
                    'A': A_str,
                    'b': b_str,
                    'x0': x0_str,
                    'omega': request.POST['omega'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            if niter <= 0:
                messages.error(request, 'El número de iteraciones debe ser positivo')
                return render(request, 'sor.html', {
                    'A': A_str,
                    'b': b_str,
                    'x0': x0_str,
                    'omega': request.POST['omega'],
                    'Tol': request.POST['Tol'],
                    'niter': request.POST['niter'],
                    'error_type': request.POST['error_type']
                })

            resultado = sor(A, b, x0, omega, tol, niter, error_type)
            # Compatibilidad: si resultado es tupla, convertir a dict
            if isinstance(resultado, tuple):
                resultado = {
                    'x': resultado[1] if len(resultado) > 1 else [],
                    'historial': [],
                    'grafica_base64': None
                }
            if 'grafica_base64' not in resultado:
                resultado['grafica_base64'] = None
            messages.success(request, 'Cálculo completado exitosamente')
            return render(request, 'sor.html', {
                'resultado': resultado,
                'A': A_str,
                'b': b_str,
                'x0': x0_str,
                'omega': request.POST['omega'],
                'Tol': request.POST['Tol'],
                'niter': request.POST['niter'],
                'error_type': request.POST['error_type']
            })

        except ValueError as e:
            messages.error(request, str(e))
            return render(request, 'sor.html', {
                'A': request.POST.get('A', ''),
                'b': request.POST.get('b', ''),
                'x0': request.POST.get('x0', ''),
                'omega': request.POST.get('omega', ''),
                'Tol': request.POST.get('Tol', ''),
                'niter': request.POST.get('niter', ''),
                'error_type': request.POST.get('error_type', '')
            })
        except Exception as e:
            messages.error(request, 'Ocurrió un error al procesar los datos. Verifique que todos los campos sean correctos.')
            return render(request, 'sor.html', {
                'A': request.POST.get('A', ''),
                'b': request.POST.get('b', ''),
                'x0': request.POST.get('x0', ''),
                'omega': request.POST.get('omega', ''),
                'Tol': request.POST.get('Tol', ''),
                'niter': request.POST.get('niter', ''),
                'error_type': request.POST.get('error_type', '')
            })
    return render(request, 'sor.html')

def vista_metodo_grafico(request):
    resultado=None
    if request.method=='POST':
        f=lambda x: eval(request.POST['f'])
        resultado=metodo_grafico(f,float(request.POST['a']),float(request.POST['b']), float(request.POST['Tol']),
                                 int(request.POST['niter']), request.POST['error_type'])
    return render(request,'metodo_grafico.html',{'resultado':resultado})

def informe_comparativo(request):
    if request.method != 'POST':
        return redirect('home')
    
    metodo_original = request.POST.get('metodo_original')
    funcion_str = request.POST.get('funcion')
    tolerancia = float(request.POST.get('tolerancia'))
    niter = int(request.POST.get('niter'))
    error_type = request.POST.get('error_type')
    
    f = lambda x: eval(funcion_str)
    
    metodos = {
        'biseccion': lambda: biseccion(f, float(request.POST.get('xi')), float(request.POST.get('xs')), tolerancia, niter, error_type),
        'regla_falsa': lambda: regla_falsa(f, float(request.POST.get('xi')), float(request.POST.get('xs')), tolerancia, niter, error_type),
        'punto_fijo': lambda: punto_fijo(lambda x: (x + f(x))/2, float(request.POST.get('xi')), tolerancia, niter, error_type),
        'newton': lambda: newton(f, lambda x: eval('2*x'), float(request.POST.get('xi')), tolerancia, niter, error_type),
        'secante': lambda: secante(f, float(request.POST.get('xi')), float(request.POST.get('xs')), tolerancia, niter, error_type),
        'raices_multiples': lambda: raices_multiples(f, lambda x: eval('2*x'), lambda x: 2, float(request.POST.get('xi')), tolerancia, niter, error_type)
    }

    resultados = []
    mejor_metodo = None
    mejor_tiempo = float('inf')
    mensaje_usuario_error = "Este método no logró encontrar una solución en el número máximo de iteraciones o produjo un error de cálculo."

    # Ejecutar el método original primero y marcarlo
    if metodo_original in metodos:
        try:
            inicio = time.time()
            resultado = metodos[metodo_original]()
            tiempo = time.time() - inicio
            if metodo_original in ['biseccion', 'regla_falsa']:
                raiz = resultado['s']
            else:
                raiz = resultado['x']
            iteraciones = len(resultado['historial'])
            resultados.append({
                'metodo': metodo_original.replace('_', ' ').title(),
                'iteraciones': iteraciones,
                'tiempo': tiempo,
                'raiz': raiz,
                'exito': True,
                'mensaje': 'Convergió',
                'original': True,
                'detalle_error': ''
            })
            if tiempo < mejor_tiempo:
                mejor_tiempo = tiempo
                mejor_metodo = {
                    'nombre': metodo_original.replace('_', ' ').title(),
                    'iteraciones': iteraciones,
                    'tiempo': tiempo
                }
        except Exception as e:
            resultados.append({
                'metodo': metodo_original.replace('_', ' ').title(),
                'iteraciones': '-',
                'tiempo': '-',
                'raiz': '-',
                'exito': False,
                'mensaje': mensaje_usuario_error,
                'original': True,
                'detalle_error': str(e)
            })
        del metodos[metodo_original]

    # Ejecutar el resto de métodos
    for nombre_metodo, metodo_func in metodos.items():
        try:
            inicio = time.time()
            resultado = metodo_func()
            tiempo = time.time() - inicio
            if nombre_metodo in ['biseccion', 'regla_falsa']:
                raiz = resultado['s']
            else:
                raiz = resultado['x']
            iteraciones = len(resultado['historial'])
            resultados.append({
                'metodo': nombre_metodo.replace('_', ' ').title(),
                'iteraciones': iteraciones,
                'tiempo': tiempo,
                'raiz': raiz,
                'exito': True,
                'mensaje': 'Convergió',
                'original': False,
                'detalle_error': ''
            })
            if tiempo < mejor_tiempo:
                mejor_tiempo = tiempo
                mejor_metodo = {
                    'nombre': nombre_metodo.replace('_', ' ').title(),
                    'iteraciones': iteraciones,
                    'tiempo': tiempo
                }
        except Exception as e:
            resultados.append({
                'metodo': nombre_metodo.replace('_', ' ').title(),
                'iteraciones': '-',
                'tiempo': '-',
                'raiz': '-',
                'exito': False,
                'mensaje': mensaje_usuario_error,
                'original': False,
                'detalle_error': str(e)
            })

    # Ordenar resultados por número de iteraciones (menor a mayor), errores al final
    def iteraciones_key(x):
        try:
            return (int(x['iteraciones']) if str(x['iteraciones']).isdigit() else float('inf'), x['tiempo'] if x['exito'] else float('inf'))
        except:
            return (float('inf'), float('inf'))
    resultados.sort(key=iteraciones_key)

    # Elegir el mejor método: el primero que haya convergido en la tabla ordenada
    mejor_metodo = None
    for r in resultados:
        if r['exito']:
            mejor_metodo = {
                'nombre': r['metodo'],
                'iteraciones': r['iteraciones'],
                'tiempo': r['tiempo']
            }
            break

    return render(request, 'informe_comparativo.html', {
        'metodo_original': metodo_original.replace('_', ' ').title(),
        'funcion': funcion_str,
        'tolerancia': tolerancia,
        'resultados': resultados,
        'mejor_metodo': mejor_metodo,
        'metodo_original_url': metodo_original
    })

def informe_comparativo_lineales(request):
    if request.method != 'POST':
        return redirect('home')

    A_str = request.POST.get('A')
    b_str = request.POST.get('b')
    x0_str = request.POST.get('x0')
    tol = float(request.POST.get('Tol'))
    niter = int(request.POST.get('niter'))
    error_type = request.POST.get('error_type')
    metodo_original = request.POST.get('metodo_original')
    omega = request.POST.get('omega', None)

    # Convertir a listas
    try:
        A = eval(A_str)
        b = eval(b_str)
        x0 = eval(x0_str)
    except Exception as e:
        return render(request, 'error.html', {'mensaje': 'Error en el formato de las matrices/vectores.'})

    metodos = {
        'jacobi': lambda: jacobi(x0, A, b, tol, niter, error_type),
        'gauss_seidel': lambda: gauss_seidel(x0, A, b, tol, niter, error_type),
        'sor': lambda: sor(A, b, x0, float(omega), tol, niter, error_type) if omega else None
    }

    resultados = []
    mensaje_usuario_error = "Este método no logró encontrar una solución en el número máximo de iteraciones o produjo un error de cálculo."

    # Ejecutar el método original primero y marcarlo
    if metodo_original in metodos:
        try:
            inicio = time.time()
            resultado = metodos[metodo_original]()
            tiempo = time.time() - inicio
            iteraciones = len(resultado['historial'])
            solucion = np.array2string(np.array(resultado['x'])) if 'x' in resultado else '-'
            resultados.append({
                'metodo': metodo_original.replace('_', ' ').title(),
                'iteraciones': iteraciones,
                'tiempo': tiempo,
                'solucion': solucion,
                'exito': True,
                'mensaje': 'Convergió',
                'original': True,
                'detalle_error': ''
            })
        except Exception as e:
            resultados.append({
                'metodo': metodo_original.replace('_', ' ').title(),
                'iteraciones': '-',
                'tiempo': '-',
                'solucion': '-',
                'exito': False,
                'mensaje': mensaje_usuario_error,
                'original': True,
                'detalle_error': str(e)
            })
        del metodos[metodo_original]

    # Ejecutar el resto de métodos
    for nombre_metodo, metodo_func in metodos.items():
        if metodo_func is None:
            continue
        try:
            inicio = time.time()
            resultado = metodo_func()
            tiempo = time.time() - inicio
            iteraciones = len(resultado['historial'])
            solucion = np.array2string(np.array(resultado['x'])) if 'x' in resultado else '-'
            resultados.append({
                'metodo': nombre_metodo.replace('_', ' ').title(),
                'iteraciones': iteraciones,
                'tiempo': tiempo,
                'solucion': solucion,
                'exito': True,
                'mensaje': 'Convergió',
                'original': False,
                'detalle_error': ''
            })
        except Exception as e:
            resultados.append({
                'metodo': nombre_metodo.replace('_', ' ').title(),
                'iteraciones': '-',
                'tiempo': '-',
                'solucion': '-',
                'exito': False,
                'mensaje': mensaje_usuario_error,
                'original': False,
                'detalle_error': str(e)
            })

    # Ordenar por menor número de iteraciones (errores al final, luego por tiempo)
    def iteraciones_key(x):
        try:
            return (int(x['iteraciones']) if str(x['iteraciones']).isdigit() else float('inf'), x['tiempo'] if x['exito'] else float('inf'))
        except:
            return (float('inf'), float('inf'))
    resultados.sort(key=iteraciones_key)

    # Elegir el mejor método: el primero que haya convergido en la tabla ordenada
    mejor_metodo = None
    for r in resultados:
        if r['exito']:
            mejor_metodo = {
                'nombre': r['metodo'],
                'iteraciones': r['iteraciones'],
                'tiempo': r['tiempo']
            }
            break

    return render(request, 'informe_comparativo_lineales.html', {
        'metodo_original': metodo_original.replace('_', ' ').title(),
        'A': A_str,
        'b': b_str,
        'x0': x0_str,
        'tol': tol,
        'niter': niter,
        'resultados': resultados,
        'mejor_metodo': mejor_metodo,
        'metodo_original_url': metodo_original
    })

#CAPITULO TRES (Falta lo del informe y revision errores)

def vista_lagrange(request):
    if request.method == 'POST':
        try:
            x_str = request.POST['x']
            y_str = request.POST['y']
            x = eval(x_str)
            y = eval(y_str)

            if not isinstance(x, list) or not isinstance(y, list):
                messages.error(request, 'Las entradas deben ser listas.')
                return render(request, 'lagrange.html', {'x': x_str, 'y': y_str})

            if len(x) != len(y):
                messages.error(request, 'Los vectores x e y deben tener la misma longitud.')
                return render(request, 'lagrange.html', {'x': x_str, 'y': y_str})

            resultado = lagrange(x, y)
            messages.success(request, 'Cálculo completado exitosamente')
            return render(request, 'lagrange.html', {'x': x_str, 'y': y_str, 'resultado': resultado})

        except Exception as e:
            messages.error(request, 'Error al procesar los datos.')
            return render(request, 'lagrange.html', {'x': request.POST.get('x', ''), 'y': request.POST.get('y', '')})
    return render(request, 'lagrange.html')

def vista_vandermonde(request):
    if request.method == 'POST':
        try:
            x_str = request.POST['x']
            y_str = request.POST['y']
            x = eval(x_str)
            y = eval(y_str)

            if not isinstance(x, list) or not isinstance(y, list):
                messages.error(request, 'Las entradas deben ser listas.')
                return render(request, 'vandermonde.html', {'x': x_str, 'y': y_str})

            if len(x) != len(y):
                messages.error(request, 'Los vectores x e y deben tener la misma longitud.')
                return render(request, 'vandermonde.html', {'x': x_str, 'y': y_str})

            resultado = vandermonde(x, y)
            messages.success(request, 'Cálculo completado exitosamente')
            return render(request, 'vandermonde.html', {'x': x_str, 'y': y_str, 'resultado': resultado})

        except Exception as e:
            messages.error(request, 'Error al procesar los datos.')
            return render(request, 'vandermonde.html', {'x': request.POST.get('x', ''), 'y': request.POST.get('y', '')})
    return render(request, 'vandermonde.html')

def vista_spline_lineal(request):
    if request.method == 'POST':
        try:
            x_str = request.POST['x']
            y_str = request.POST['y']
            x = eval(x_str)
            y = eval(y_str)

            if not isinstance(x, list) or not isinstance(y, list):
                messages.error(request, 'Las entradas deben ser listas.')
                return render(request, 'spline_lineal.html', {'x': x_str, 'y': y_str})

            if len(x) != len(y):
                messages.error(request, 'Los vectores x e y deben tener la misma longitud.')
                return render(request, 'spline_lineal.html', {'x': x_str, 'y': y_str})

            resultado = spline_lineal(x, y)
            messages.success(request, 'Cálculo completado exitosamente')
            return render(request, 'spline_lineal.html', {'x': x_str, 'y': y_str, 'resultado': resultado})

        except Exception as e:
            messages.error(request, 'Error al procesar los datos.')
            return render(request, 'spline_lineal.html', {'x': request.POST.get('x', ''), 'y': request.POST.get('y', '')})
    return render(request, 'spline_lineal.html')

def vista_spline_cubico(request):
    if request.method == 'POST':
        try:
            x_str = request.POST['x']
            y_str = request.POST['y']
            x = eval(x_str)
            y = eval(y_str)

            if not isinstance(x, list) or not isinstance(y, list):
                messages.error(request, 'Las entradas deben ser listas.')
                return render(request, 'spline_cubico.html', {'x': x_str, 'y': y_str})

            if len(x) != len(y):
                messages.error(request, 'Los vectores x e y deben tener la misma longitud.')
                return render(request, 'spline_cubico.html', {'x': x_str, 'y': y_str})

            resultado = spline_cubico(x, y)
            messages.success(request, 'Cálculo completado exitosamente')
            return render(request, 'spline_cubico.html', {'x': x_str, 'y': y_str, 'resultado': resultado})

        except Exception as e:
            messages.error(request, 'Error al procesar los datos.')
            return render(request, 'spline_cubico.html', {'x': request.POST.get('x', ''), 'y': request.POST.get('y', '')})
    return render(request, 'spline_cubico.html')

def vista_newtonint(request):
    if request.method == 'POST':
        try:
            x_str = request.POST['x']
            y_str = request.POST['y']
            x = eval(x_str)
            y = eval(y_str)

            if not isinstance(x, list) or not isinstance(y, list):
                messages.error(request, 'Las entradas deben ser listas.')
                return render(request, 'newtonint.html', {'x': x_str, 'y': y_str})

            if len(x) != len(y):
                messages.error(request, 'Los vectores x e y deben tener la misma longitud.')
                return render(request, 'newtonint.html', {'x': x_str, 'y': y_str})

            resultado = newtonint(x, y)
            messages.success(request, 'Cálculo completado exitosamente')
            return render(request, 'newtonint.html', {'x': x_str, 'y': y_str, 'resultado': resultado})

        except Exception as e:
            messages.error(request, 'Error al procesar los datos.')
            return render(request, 'newtonint.html', {'x': request.POST.get('x', ''), 'y': request.POST.get('y', '')})
    return render(request, 'newtonint.html')

def informe_comparativo_interpolacion(request):
    if request.method != 'POST':
        return redirect('home')

    x_str = request.POST.get('x')
    y_str = request.POST.get('y')
    metodo_original = request.POST.get('metodo_original')

    try:
        x = eval(x_str)
        y = eval(y_str)
    except Exception as e:
        return render(request, 'error.html', {'mensaje': 'Error en el formato de los vectores x e y.'})

    metodos = {
        'vandermonde': lambda: vandermonde(x, y),
        'newtonint': lambda: newtonint(x, y),
        'lagrange': lambda: lagrange(x, y),
        'spline_lineal': lambda: spline_lineal(x, y),
        'spline_cubico': lambda: spline_cubico(x, y),
    }

    resultados = []
    mensaje_usuario_error = "Este método no logró encontrar una solución o produjo un error de cálculo."

    # Ejecutar el método original primero y marcarlo
    if metodo_original in metodos:
        try:
            inicio = time.time()
            resultado = metodos[metodo_original]()
            tiempo = time.time() - inicio
            resultados.append({
                'metodo': metodo_original.replace('_', ' ').title(),
                'tiempo': tiempo,
                'resultado': resultado,
                'exito': True,
                'mensaje': 'Éxito',
                'original': True,
                'detalle_error': ''
            })
        except Exception as e:
            resultados.append({
                'metodo': metodo_original.replace('_', ' ').title(),
                'tiempo': '-',
                'resultado': '-',
                'exito': False,
                'mensaje': mensaje_usuario_error,
                'original': True,
                'detalle_error': str(e)
            })
        del metodos[metodo_original]

    # Ejecutar el resto de métodos
    for nombre_metodo, metodo_func in metodos.items():
        try:
            inicio = time.time()
            resultado = metodo_func()
            tiempo = time.time() - inicio
            resultados.append({
                'metodo': nombre_metodo.replace('_', ' ').title(),
                'tiempo': tiempo,
                'resultado': resultado,
                'exito': True,
                'mensaje': 'Éxito',
                'original': False,
                'detalle_error': ''
            })
        except Exception as e:
            resultados.append({
                'metodo': nombre_metodo.replace('_', ' ').title(),
                'tiempo': '-',
                'resultado': '-',
                'exito': False,
                'mensaje': mensaje_usuario_error,
                'original': False,
                'detalle_error': str(e)
            })

    # Elegir el mejor método: el primero que haya tenido éxito y menor tiempo
    mejor_metodo = None
    resultados_exito = [r for r in resultados if r['exito']]
    if resultados_exito:
        mejor_metodo = min(resultados_exito, key=lambda r: r['tiempo'])

    return render(request, 'informe_comparativo_interpolacion.html', {
        'metodo_original': metodo_original.replace('_', ' ').title(),
        'x': x_str,
        'y': y_str,
        'resultados': resultados,
        'mejor_metodo': mejor_metodo,
        'metodo_original_url': metodo_original
    })