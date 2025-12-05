# Módulo que contiene las funciones relacionadas con el procesamiento de datos estadísticos de estudiantes
import csv
import copy


def limpiar_pantalla(espacios = 40):
    # Esta función limpia la pantalla de la consola.
    print("\n"*espacios)
    print("\033[H")   # Secuencia de escape ANSI para mover el cursor a la posición (0,0)
    
def menu():
    '''
    Muestra el menú de opciones al usuario y retorna la opción seleccionada.
    Retorna:
        str: Opción seleccionada por el usuario.    
    '''
    print("Menú de opciones:")
    print("1. Cargar datos desde archivo")
    print("2. Eliminar estudiante")
    print("3. Mayor nota de estudiante")
    print("4. Ordenar promedios de estudiantes")
    print("5. Ordenar estudiantes por cantidad de cursos")
    print("6. Salir del programa")
    seleccion = input("Seleccione una opción: ")
    return seleccion

def cargar_notas(path = './database/notas_estudiantes.csv'):
    '''
    Carga las notas de los estudiantes desde un archivo CSV.
    Parámetros:
        path (str): Ruta al archivo CSV con las notas de los estudiantes.
    Retorna:
        tuple: Tupla con tres elementos:
            - lista de IDs de estudiantes (list)
            - lista de códigos de cursos (list)
            - lista de listas con las notas de cada estudiante (list)       
    '''
    estudiantes = []
    cursos = []
    notas = []
    with open(path,"r") as file:
        cursos = file.readline().strip().split(",")  # Saltar la cabecera
        estudiantes = file.readline().strip().split(",") # Leer la segunda línea con los id de usuarios
        for line in file:
            nota = line.strip().split(",") # Asignar las notas a cada usuario como lista
            notas.append(nota)

    return estudiantes, cursos, notas

def eliminar_estudiante(estudiantes, notas, id_estudiante):
    '''
    Elimina un estudiante y sus notas asociadas.
    Parámetros:
        estudiantes (list): Lista de IDs de estudiantes.
        notas (list): Lista de listas con las notas de cada estudiante.
        id_estudiante (str): ID del estudiante a eliminar.
    Retorna:
        None    
    '''
    if id_estudiante in estudiantes:
        index = estudiantes.index(id_estudiante)
        estudiantes.pop(index)
        notas.pop(index)
        print(f"Estudiante con ID {id_estudiante} eliminado.")
    else:
        print(f"No se encontró al estudiante con ID {id_estudiante}.")


def mayor_nota_estudiante(estudiantes, notas, id_estudiante):    
    '''
    Encuentra la mayor nota de un estudiante y el código del curso donde la obtuvo.
    Parámetros:
        estudiantes (list): Lista de IDs de estudiantes.
        notas (list): Lista de listas con las notas de cada estudiante.
        id_estudiante (str): ID del estudiante a consultar.
    Retorna:
        tuple: Mayor nota y código del curso donde la obtuvo.
    '''
    if id_estudiante in estudiantes:
        index = estudiantes.index(id_estudiante)
        notas_estudiante = notas[index]
        max_nota = max(float(nota) for nota in notas_estudiante if nota)
        curso_index = notas_estudiante.index(str(max_nota))
        return max_nota, curso_index
    else:
        return None, None
    
def obtener_promedios_materias(notas):
    '''
    Calcula el promedio de notas para cada estudiante.
    Parámetros:
        notas (list): Lista de listas con las notas de cada estudiante.
    Retorna:
        list: Lista con los promedios de cada estudiante.
    '''
    promedios =[]
    materias_cursadas = []
    for nota_alumno in notas:
        promedio_alumno = 0
        suma_notas = 0
        contador_notas = 0
        for nota in nota_alumno:
            if nota != "-1":
                contador_notas += 1
                suma_notas += float(nota)
        if contador_notas > 0:
            promedio_alumno = suma_notas / contador_notas
        materias_cursadas.append(contador_notas)    
        promedios.append(promedio_alumno)
    return promedios, materias_cursadas

def sort_bubble(promedios):
    '''
    Ordena los promedios de los estudiantes usando el algoritmo de burbuja.
    Parámetros:
        promedios (list): Lista con los promedios de cada estudiante.
    Retorna:
        list: Lista con los promedios ordenados de mayor a menor.   
    '''

    data = copy.deepcopy(promedios)
    # Algoritmo de burbuja
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] < data[j+1]: # comparando promedios del 1 y el segundo elemento de la tupla en los elementos de promedio
                data[j], data[j+1] = data[j+1], data[j] # intercambiar si el elemento encontrado es menor   
    return data

def ordenar_estudiantes_burbuja(estudiantes, notas):
    '''
    Ordena los estudiantes según su promedio usando el algoritmo de burbuja.
    Parámetros:
        estudiantes (list): Lista de IDs de estudiantes.
        notas (list): Lista de listas con las notas de cada estudiante.
    Retorna:
        list: Lista de tuplas con ID del estudiante y su promedio, ordenada de mayor a menor promedio.                      
    '''
    promedios, _ = obtener_promedios_materias(notas)
    promedios_ordenados = sort_bubble(promedios)
    indices_ordenados = []
    for promedio in promedios_ordenados:
        index = promedios.index(promedio)
        while index in indices_ordenados:
            index = promedios.index(promedio, index + 1)
        indices_ordenados.append(index) 

    return [(estudiantes[i], promedios[i]) for i in indices_ordenados]  

def ordenar_materias_seleccion(estudiantes, notas):
    '''
    Ordena los estudiantes según la cantidad de materias cursadas usando el algoritmo de selección.
    Parámetros:
        estudiantes (list): Lista de IDs de estudiantes.
        notas (list): Lista de listas con las notas de cada estudiante.
    Retorna:
        None: Imprime la lista de estudiantes ordenada por cantidad de materias cursadas.
    '''
    x , materias_cursadas = obtener_promedios_materias(notas)
    n = len(materias_cursadas)
    for i in range(n):
        ind = i # índice del elemento 
        for j in range(i+1, n):
            #print("ciclo ",i,"Comparando:",materias_cursadas[ind], "y", materias_cursadas[j])
            if materias_cursadas[j] > materias_cursadas[ind]:
                ind = j
            #print("INTERCAMBIO:",data[i],"y",data[ind])
        materias_cursadas[i], materias_cursadas[ind] = materias_cursadas[ind], materias_cursadas[i]
    for i in range(n):
        print(f"Estudiante ID: {estudiantes[i]}, Cantidad de cursos: {materias_cursadas[i]}")
     