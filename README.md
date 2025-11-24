# Estadisticas-estudiantes

Proyecto para calcular y analizar estadísticas de los estudiantes
del primer semestre en la Universidad de Antioquia.

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

**Estructura de datos (modelo de la práctica)**
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

**Requisitos y ejecución**
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

**Qué se espera entregar**
- Código que lea los CSV y construya las estructuras (listas + matriz).
- Implementaciones de funciones para calcular estadísticas básicas y
	para administrar las listas (búsqueda, ordenamiento, filtrado).
- Documentación mínima en `README.md` y comentarios claros en los módulos.

Si quieres, puedo:
- generar ejemplos de funciones para leer `database/notas_estudiantes.csv` y
	construir las estructuras, o
- implementar cálculos estadísticos (promedios, número de cancelaciones, etc.),
	o
- crear gráficos básicos en `modules/plots.py`.
