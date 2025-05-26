from django.urls import path
from .views import (
    home, vista_biseccion, vista_gauss_seidel, vista_jacobi, vista_metodo_grafico,
    vista_newton, vista_punto_fijo, vista_raices_multiples, vista_regla_falsa,
    vista_secante, vista_sor, informe_comparativo, informe_comparativo_lineales, vista_lagrange, vista_vandermonde,
    vista_spline_cubico, vista_spline_lineal, vista_newtonint
)

urlpatterns = [
    path('', home, name='home'),
    path('biseccion/', vista_biseccion, name='biseccion'),
    path('gauss-seidel/', vista_gauss_seidel, name='gauss_seidel'),
    path('jacobi/', vista_jacobi, name='jacobi'),
    path('metodo-grafico/', vista_metodo_grafico, name='metodo_grafico'),
    path('newton/', vista_newton, name='newton'),
    path('punto-fijo/', vista_punto_fijo, name='punto_fijo'),
    path('raices-multiples/', vista_raices_multiples, name='raices_multiples'),
    path('regla-falsa/', vista_regla_falsa, name='regla_falsa'),
    path('secante/', vista_secante, name='secante'),
    path('sor/', vista_sor, name='sor'),
    path('lagrange/', vista_lagrange, name='lagrange'),
    path('vandermonde/', vista_vandermonde, name='vandermonde'),
    path('spline-cubico/', vista_spline_cubico, name='spline_cubico'),
    path('spline-lineal/', vista_spline_lineal, name='spline_lineal'),
    path('newtonint/', vista_newtonint, name='newtonint'),
    path('informe-comparativo/', informe_comparativo, name='informe_comparativo'),
    path('informe-comparativo-lineales/', informe_comparativo_lineales, name='informe_comparativo_lineales'),
]
