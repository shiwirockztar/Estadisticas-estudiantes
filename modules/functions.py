# Módulo que contiene las funciones relacionadas con el procesamiento de datos estadísticos de estudiantes
import csv
import copy

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

def cargar_notas(path = 'notas_estudiantes.csv'):
    '''
    Calcula el promedio de notas para cada estudiante.
    Parámetros:
        notas_estudiantes (list): Lista de diccionarios con las notas de los estudiantes.
    Retorna:
        dict: Diccionario con el promedio de notas por estudiante.
    '''
    datos = {}
    with open(path,"r") as file:
        file.readline()  # Saltar la cabecera
        usuarios = file.readline().strip().split(",") # Leer la segunda línea con los id de usuarios
        dic_usuarios = {usuario: [] for usuario in usuarios} # Crear diccionario con listas vacías
        for index, line in enumerate(file):
            id = list(dic_usuarios.keys())[index]
            dic_usuarios[id] = line.strip().split(",") # Asignar las notas a cada usuario como lista
    #print(dic_usuarios)
    return dic_usuarios

def eliminar_estudiante(notas_estudiantes, id_estudiante):
    '''
    Elimina un estudiante del diccionario de notas.
    Parámetros:
        notas_estudiantes (dict): Diccionario con las notas de los estudiantes.
        id_estudiante (str): ID del estudiante a eliminar.
    Retorna:
        dict: Diccionario actualizado sin el estudiante eliminado.
    '''
    #nuevas_notas = copy.deepcopy(notas_estudiantes)
    if id_estudiante in notas_estudiantes:
        del notas_estudiantes[id_estudiante]
        print(f"Estudiante con ID {id_estudiante} eliminado.")
    else:
        print(f"No se encontró al estudiante con ID {id_estudiante}.")

def mayor_nota_estudiante(notas_estudiantes, id_estudiante):    
    '''
    Encuentra la mayor nota de un estudiante y el código del curso donde la obtuvo.
    Parámetros:
        notas_estudiantes (dict): Diccionario con las notas de los estudiantes.
        id_estudiante (str): ID del estudiante a consultar.
    Retorna:
        tuple: Mayor nota y código del curso donde la obtuvo.
    '''
    if id_estudiante in notas_estudiantes:
        notas = notas_estudiantes[id_estudiante]
        max_nota = max(float(nota) for nota in notas if nota)
        curso_index = notas.index(str(max_nota))
        return max_nota, curso_index
    else:
        return None, None
    
def estudiante_promedio(notas_estudiantes):
    '''
    Funcion que calcula el promedio de notas para cada estudiante.
    Parámetros:
        notas_estudiantes (dict): Diccionario con las notas de los estudiantes.
    Retorna:
        list: Lista de tuplas con ID del estudiante y su promedio.
    '''
    promedios = []
    for id_estudiante, notas in notas_estudiantes.items():
        suma_notas = sum([float(nota) for nota in notas if nota])
        promedio = suma_notas / len(notas)
        promedios.append([id_estudiante, promedio])
    return promedios

def ordenar_promedios_burbuja(promedios):
    '''
    Ordena los estudiantes según su promedio de notas usando el algoritmo de burbuja.
    Parámetros:
        promedios (list): Lista de tuplas con ID del estudiante y su promedio.
    Retorna:
        list: Lista de tuplas con ID del estudiante y su promedio, ordenada de mayor a menor promedio.
    '''
    n = len(promedios)
    for i in range(n):
        for j in range(0, n-i-1):
            if promedios[j][1] < promedios[j+1][1]:
                promedios[j], promedios[j+1] = promedios[j+1], promedios[j]
    return promedios

def ordenar_promedios_burbujaT(notas_estudiantes):
    '''
    Ordena los estudiantes según su promedio de notas usando el algoritmo de burbuja.
    Parámetros:
        notas_estudiantes (dict): Diccionario con las notas de los estudiantes.
    Retorna:
        list: Lista de tuplas con ID del estudiante y su promedio, ordenada de mayor a menor promedio.
    '''
    promedios = []
    for id_estudiante, notas in notas_estudiantes.items():
        notas_float = [float(nota) for nota in notas if nota]
        promedio = sum(notas_float) / len(notas_float) if notas_float else 0
        promedios.append([id_estudiante, promedio])
    
    # Algoritmo de burbuja
    n = len(promedios)
    for i in range(n):
        for j in range(0, n-i-1):
            if promedios[j][1] < promedios[j+1][1]:
                promedios[j], promedios[j+1] = promedios[j+1], promedios[j]
    
    return promedios

def promedio_cursos_seleccion(notas_estudiantes):
    '''
    Ordena los estudiantes según la cantidad de cursos usando el algoritmo de selección.
    Parámetros:
        notas_estudiantes (dict): Diccionario con las notas de los estudiantes.
    Retorna:
        list: Lista de tuplas con ID del estudiante y cantidad de cursos, ordenada de mayor a menor cantidad.
    '''
    cantidades = []
    for id_estudiante, notas in notas_estudiantes.items():
        cantidad = len([nota for nota in notas if nota])
        cantidades.append((id_estudiante, cantidad))
    
    # Algoritmo de selección
    n = len(cantidades)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if cantidades[j][1] > cantidades[max_idx][1]:
                max_idx = j
        cantidades[i], cantidades[max_idx] = cantidades[max_idx], cantidades[i]
    
    return cantidades   