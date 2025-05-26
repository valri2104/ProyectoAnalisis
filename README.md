# Proyecto de Análisis Numérico

Aplicación web en Django que implementa métodos numéricos para resolver ecuaciones y sistemas de ecuaciones.

## Métodos Implementados

- Bisección
- Secante
- Gauss-Seidel
- Jacobi
- Método Gráfico
- Newton
- Punto Fijo
- Raíces Múltiples
- Regla Falsa
- SOR (Successive Over-Relaxation)

## Requisitos

- Python 3.8 o superior
- pip

## Instalación

1. Crear y activar entorno virtual:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución

1. Navegar al directorio del proyecto:
```bash
cd analisis_numerico
```

2. Iniciar el servidor:
```bash
python manage.py runserver
```

3. Abrir en el navegador:
```
http://127.0.0.1:8000/
```

## Uso

1. Seleccionar el método numérico desde el menú
2. Ingresar los parámetros requeridos:
   - Para ecuaciones: función, puntos iniciales, tolerancia
   - Para sistemas lineales: matriz A, vector b, vector inicial
3. Hacer clic en "Calcular" para ver resultados

## Notas

- Funciones matemáticas: usar sintaxis Python (ej: `x**2`, `math.sin(x)`)
- Matrices y vectores: usar sintaxis Python (ej: `[[1,2],[3,4]]`, `[1,2,3]`)

## Estructura del Proyecto

```
ProyectoAnalisis/
├── analisis_numerico/
│   ├── metodos/
│   │   ├── algoritmos/     # Implementaciones de los métodos
│   │   ├── templates/      # Plantillas HTML
│   │   └── views.py        # Vistas de la aplicación
│   ├── static/             # Archivos estáticos (CSS, JS)
│   └── manage.py           # Script de administración de Django
└── requirements.txt        # Dependencias del proyecto
```

## Contribuir

Si deseas contribuir al proyecto:

1. Haz un fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles. 