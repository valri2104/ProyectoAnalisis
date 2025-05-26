# Proyecto de Análisis Numérico

Este proyecto es una aplicación web desarrollada en Django que implementa varios métodos numéricos para la resolución de ecuaciones y sistemas de ecuaciones.

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

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (opcional, para clonar el repositorio)

## Instalación

1. Clonar el repositorio (o descargar los archivos):
```bash
git clone <url-del-repositorio>
cd ProyectoAnalisis
```

2. Crear y activar un entorno virtual:
```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución del Proyecto

1. Asegúrate de estar en el directorio correcto:
```bash
cd analisis_numerico
```

2. Realiza las migraciones de la base de datos:
```bash
python manage.py migrate
```

3. Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```

4. Abre tu navegador web y visita:
```
http://127.0.0.1:8000/
```

## Uso de la Aplicación

1. Selecciona el método numérico que deseas utilizar desde el menú de navegación.
2. Ingresa los parámetros requeridos para cada método:
   - Para métodos de ecuaciones: función, puntos iniciales, tolerancia, etc.
   - Para métodos de sistemas lineales: matriz A, vector b, vector inicial, etc.
3. Haz clic en "Calcular" para obtener los resultados.
4. Los resultados incluirán:
   - La solución aproximada
   - El historial de iteraciones
   - Una gráfica del proceso

## Notas Importantes

- Para funciones matemáticas, usa la sintaxis de Python:
  - Potencias: `x**2`
  - Funciones trigonométricas: `math.sin(x)`, `math.cos(x)`
  - Constantes: `math.pi`, `math.e`

- Para matrices y vectores, usa la sintaxis de Python:
  - Matriz: `[[1,2],[3,4]]`
  - Vector: `[1,2,3]`

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