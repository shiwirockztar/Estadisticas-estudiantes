# Módulo que contiene las funciones relacionadas con el procesamiento de datos estadísticos de estudiantes



def cargar_datos_desde_archivo(nombre_archivo):
    '''
    Carga los datos desde un archivo CSV y retorna las estructuras de datos necesarias.
    Parámetros:
        nombre_archivo (str): Nombre del archivo CSV a cargar.
    Retorna:
        dict: Diccionario con los datos de estudiantes y sus notas.
    '''
    datos = {}
    # Lógica para leer el archivo CSV y cargar los datos en el diccionario
    return datos

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