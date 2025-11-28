# Estadisticas-estudiantes

Proyecto para calcular y analizar estadísticas de los estudiantes
del primer semestre en la Universidad de Antioquia.

<p align="center">
  <a title="Twitter: Jose_leonardo" href="https://www.linkedin.com/in/jose-leonardo-poveda/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
  </a> 
  <br />
  <a title="Github: Sponsors" href="https://github.com/shiwirockztar">
    <img src="https://img.shields.io/twitter/url?color=032f62&label=Github%20%40Shiwirockztar&logo=github&logoColor=FFFFFF&style=flat-square&url=https%3A%2F%2Fgithub.com%2Fsponsors%2FShiwirockztar">
  </a>
</p>

## 📂 Estructura de carpetas

```
Estadisticas-estudiantes/
│
├── Guía Lab 7 - Estadísticas estudiantes.pdf  # Practica.
├── Readme  📝                                 # Project information and instructions.
│
├── main.py
│
├── modules/
│   ├── estudiantes.py
│   ├── archivo.py
│   ├── plots.py
│   └── __init__.py
│
└── database
    ├── hist_matriculados.csv 📜           # Csv.
    └── notas_estudiantes.csv 📜           # Csv.
```



**Descripción**
- **Propósito:** Generar estadísticas (promedios, matrículas, cursos cancelados, etc.)
	sobre los estudiantes del primer semestre a partir de las listas y la matriz
	de notas proporcionadas.
- **Contexto:** Este repositorio contiene una práctica de laboratorio (Práctica VII
	- Informática I) en la que la información está representada por dos listas y
	una matriz (lista bidimensional) que se administran de forma conjunta. Las
	listas contienen, por ejemplo, los números de documento de los estudiantes y
	los códigos de los cursos; la matriz contiene las notas de cada estudiante en
	cada curso.

**  📐 Estructura de datos (modelo de la práctica)**
- **Lista de estudiantes:** lista unidimensional con la identificación (documento)
	de cada estudiante. El orden posicional relaciona al estudiante i con la fila i
	de la matriz de notas.
- **Lista de cursos:** lista unidimensional con los códigos de los cursos. El
	orden posicional relaciona el curso j con la columna j de la matriz de notas.
- **Matriz de notas:** lista bidimensional donde el elemento en la fila i y
	columna j representa la nota del estudiante i en el curso j.
	- **-1**: el estudiante i canceló el curso j.
	- **-2**: el estudiante i no se matriculó en el curso j.

Se debe mantener la estructura propuesta (dos listas + matriz) y diseñar
funciones propias para administrar las listas/operaciones requeridas.

**Árbol de archivos (actual)**
- `main.py` : Punto de entrada del programa; coordina la lectura de datos y la
	generación de estadísticas.
- `modules/plots.py` : Funciones para generar visualizaciones (opcional).
- `database/hist_matriculados.csv` : Historial o registro de matrículas (CSV).
- `database/notas_estudiantes.csv` : Matriz/registro de notas por estudiante y curso (CSV).

**Flujo esperado y responsabilidades de los módulos**
- `main.py`: cargar datos desde `database/`, construir las dos listas y la matriz,
	ejecutar los cálculos estadísticos (promedios por estudiante/curso, conteos de
	cancelaciones/matrículas) y mostrar/guardar resultados.
- `modules/plots.py`: funciones para graficar distribuciones de notas, promedios,
	histogramas, etc. (siempre opcional; el análisis puede realizarse sin gráficos).

**  ✅ Requisitos y ejecución**
- Requisitos: Python 3.8+ (no se requiere librería externa para la versión básica).
- Ejecutar el programa:

```bash
python3 main.py
```

**Notas de implementación (sugerencias)**
- Mantenga las listas y la matriz desacopladas, usando la relación posicional
	para cruzar información (índice del estudiante ↔ fila; índice del curso ↔ columna).
- Proporcione funciones claras para:
	- leer CSV y construir las estructuras (`archivo.py` o funciones en `main.py`),
	- acceder y modificar notas (por ejemplo, marcar cancelaciones con -1),
	- calcular métricas (promedios ignorando -1/-2, porcentajes de aprobados, etc.),
	- ordenar o buscar estudiantes según criterios (puede existir un módulo `ordenar`).
- Documente en el código las decisiones sobre cómo tratar `-1` y `-2` al calcular
	promedios y otros indicadores (por ejemplo: excluir `-2` y `-1` del cálculo de promedio).

**Ejemplo conceptual de estructuras**
- `estudiantes = [1001, 1002, 1003]`
- `cursos = ['MAT101', 'PROG101', 'FIS101']`
- `notas = [[3.5, -2, 4.0], [2.0, 3.0, -1], [4.5, 4.0, 4.0]]`
	- En este ejemplo, `notas[0][1] == -2` significa que el estudiante `1001`
		no se matriculó en `PROG101`.

**  ⛽️ Qué se espera entregar**
- Código que lea los CSV y construya las estructuras (listas + matriz).
- Implementaciones de funciones para calcular estadísticas básicas y
	para administrar las listas (búsqueda, ordenamiento, filtrado).
- Documentación mínima en `README.md` y comentarios claros en los módulos.

## Happy Code

Created by Jose Leonardo P Poveda, lot of ❤️ and a few ☕️

Claro, vamos a desglosar cómo funciona el **algoritmo de selección** (Selection Sort) para ordenar la lista de datos **paso a paso**, analizando los ciclos de la ejecución. En este caso, vamos a ordenar los datos según el **segundo valor** de cada sublista (es decir, los números decimales, como `2.9000000000000004`).

# Algoritmo ordenamiento por seleccion

### Datos Iniciales

La lista de datos es la siguiente:

```python
data = [
    ['1033492448', 2.9000000000000004, 4],
    ['1032090603', 3.1500000000000004, 4],
    ['1002152167', 2.46, 5],
    ['1028854736', 2.54, 5],
    ['1014191590', 3.7399999999999998, 5],
    ['1024351175', 2.5799999999999996, 5],
    ['1036351870', 3.66, 5]
]
```

### Ciclo 1: Seleccionar el valor más pequeño en todo el arreglo

1. En la primera iteración, **i = 0** (empezamos con el primer elemento, el que tiene índice 0).
2. Buscamos el valor más pequeño entre todos los elementos a partir de la posición 0 (es decir, en toda la lista).

#### Sub-ciclo 1.1: Buscar el mínimo

* Comparamos `2.9000000000000004` (índice 0) con `3.1500000000000004` (índice 1). El mínimo sigue siendo `2.9000000000000004`.
* Comparamos `2.9000000000000004` (índice 0) con `2.46` (índice 2). El mínimo ahora es `2.46`.
* Comparamos `2.46` (índice 2) con `2.54` (índice 3). El mínimo sigue siendo `2.46`.
* Comparamos `2.46` (índice 2) con `3.7399999999999998` (índice 4). El mínimo sigue siendo `2.46`.
* Comparamos `2.46` (índice 2) con `2.5799999999999996` (índice 5). El mínimo sigue siendo `2.46`.
* Comparamos `2.46` (índice 2) con `3.66` (índice 6). El mínimo sigue siendo `2.46`.

#### Intercambio

* El mínimo encontrado es `2.46` (índice 2).
* Intercambiamos `2.9000000000000004` (índice 0) con `2.46` (índice 2).

Resultado después del primer ciclo:

```python
data = [
    ['1002152167', 2.46, 5],  # Intercambiado
    ['1032090603', 3.1500000000000004, 4],
    ['1033492448', 2.9000000000000004, 4],  # Intercambiado
    ['1028854736', 2.54, 5],
    ['1014191590', 3.7399999999999998, 5],
    ['1024351175', 2.5799999999999996, 5],
    ['1036351870', 3.66, 5]
]
```

### Ciclo 2: Seleccionar el valor más pequeño en el subarreglo restante

Ahora, vamos a ordenar el subarreglo restante (después de la primera posición):

3. En la segunda iteración, **i = 1** (empezamos con el segundo elemento, el que tiene índice 1).
4. Buscamos el valor más pequeño en el subarreglo que empieza en el índice 1.

#### Sub-ciclo 2.1: Buscar el mínimo

* Comparamos `3.1500000000000004` (índice 1) con `2.9000000000000004` (índice 2). El mínimo sigue siendo `2.9000000000000004`.
* Comparamos `2.9000000000000004` (índice 2) con `2.54` (índice 3). El mínimo ahora es `2.54`.
* Comparamos `2.54` (índice 3) con `3.7399999999999998` (índice 4). El mínimo sigue siendo `2.54`.
* Comparamos `2.54` (índice 3) con `2.5799999999999996` (índice 5). El mínimo sigue siendo `2.54`.
* Comparamos `2.54` (índice 3) con `3.66` (índice 6). El mínimo sigue siendo `2.54`.

#### Intercambio

* El mínimo encontrado es `2.54` (índice 3).
* Intercambiamos `3.1500000000000004` (índice 1) con `2.54` (índice 3).

Resultado después del segundo ciclo:

```python
data = [
    ['1002152167', 2.46, 5], 
    ['1028854736', 2.54, 5],  # Intercambiado
    ['1033492448', 2.9000000000000004, 4],
    ['1032090603', 3.1500000000000004, 4],  # Intercambiado
    ['1014191590', 3.7399999999999998, 5],
    ['1024351175', 2.5799999999999996, 5],
    ['1036351870', 3.66, 5]
]
```

### Ciclo 3: Seleccionar el valor más pequeño en el subarreglo restante

5. En la tercera iteración, **i = 2** (empezamos con el tercer elemento, el que tiene índice 2).
6. Buscamos el valor más pequeño en el subarreglo que empieza en el índice 2.

#### Sub-ciclo 3.1: Buscar el mínimo

* Comparamos `2.9000000000000004` (índice 2) con `3.1500000000000004` (índice 3). El mínimo sigue siendo `2.9000000000000004`.
* Comparamos `2.9000000000000004` (índice 2) con `3.7399999999999998` (índice 4). El mínimo sigue siendo `2.9000000000000004`.
* Comparamos `2.9000000000000004` (índice 2) con `2.5799999999999996` (índice 5). El mínimo ahora es `2.5799999999999996`.
* Comparamos `2.5799999999999996` (índice 5) con `3.66` (índice 6). El mínimo sigue siendo `2.5799999999999996`.

#### Intercambio

* El mínimo encontrado es `2.5799999999999996` (índice 5).
* Intercambiamos `2.9000000000000004` (índice 2) con `2.5799999999999996` (índice 5).

Resultado después del tercer ciclo:

```python
data = [
    ['1002152167', 2.46, 5], 
    ['1028854736', 2.54, 5], 
    ['1024351175', 2.5799999999999996, 5],  # Intercambiado
    ['1032090603', 3.1500000000000004, 4], 
    ['1033492448', 2.9000000000000004, 4],  # Intercambiado
    ['1014191590', 3.7399999999999998, 5],
    ['1036351870', 3.66, 5]
]
```

### Ciclo 4: Seleccionar el valor más pequeño en el subarreglo restante

7. En la cuarta iteración, **i = 3** (empezamos con el cuarto elemento, el que tiene índice 3).
8. Buscamos el valor más pequeño en el subarreglo que empieza en el índice 3.

#### Sub-ciclo 4.1: Buscar el mínimo

* Comparamos `3.1500000000000004` (índice 3) con `2.9000000000000004` (índice 4). El mínimo ahora es `2.9000000000000004`.
* Comparamos `2.9000000000000004` (índice 4) con `3.7399999999999998` (índice 5). El mínimo sigue siendo `2.9000000000000004`.
* Comparamos `2.9000000000000004` (índice 4) con `3.66` (índice 6). El mínimo sigue siendo `2.9000000000000004`.

#### Intercambio

* El mínimo encontrado es `2.9000000000000004` (índice 4), que ya está en su lugar. No
