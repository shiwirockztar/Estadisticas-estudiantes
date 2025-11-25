# Módulo que contiene las funciones relacionadas con el procesamiento de datos estadísticos de estudiantes
import csv

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
    print(dic_usuarios)
    return datos
