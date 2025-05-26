from django.shortcuts import render
from django.contrib import messages
from .algoritmos import (
    biseccion, secante, regla_falsa, raices_multiples,
    sor, punto_fijo,  newton, metodo_grafico,
    jacobi, gauss_seidel
)

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
        resultado=metodo_grafico(f,float(request.POST['A']),float(request.POST['b']), float(request.POST['Tol']),
                                 int(request.POST['niter']), request.POST['error_type'])
    return render(request,'metodo_grafico.html',{'resultado':resultado})