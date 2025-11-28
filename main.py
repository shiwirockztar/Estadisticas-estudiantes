# Implemente aquí los menús y el programa principal que invoca las funciones de los otros módulos
import modules.functions as func
import time

#seleccion = func.menu() # 1. Mostrar menú principal al usuario
notas_estudiantes = func.cargar_notas()  # Diccionario para almacenar las notas de los estudiantes

while True:

    # 2. Cargar datos desde archivo
    #    Esta opción permite leer el archivo database.csv
    #    El usuario debe seleccionar esta opción para leer
    #    y cargar las estructuras de datos del programa.

    # 3. Eliminar estudiante
    #    y se elimina al estudiante y sus notas.

    # 4. Mayor nota de estudiante
    #    Dado un estudiante, se debe buscar su mayor nota
    #    y retornar el código del curso donde la obtuvo.

    # 5. Ordenar promedios de estudiantes
    #    Se deben ordenar los estudiantes según su promedio
    #    de notas usando obligatoriamente burbuja.
    #    Luego imprimir por pantalla.

    # 6. Ordenar estudiantes por cantidad de cursos
    #    Se deben ordenar usando obligatoriamente selección
    #    según la cantidad de materias cursadas
    #    y luego imprimir el resultado.

    # 7. Opción de salir del programa
    #    Si el usuario selecciona esta opción, finalizar la ejecución.

    seleccion = ""  # Variable para recibir opción del usuario

    time.sleep(2.5)
    func.limpiar_pantalla()  # Limpiar pantalla antes de mostrar el menú
    seleccion = func.menu() # 1. Mostrar menú 

    # 8. Verificar qué opción eligió el usuario y ejecutar su bloque correspondiente
    if seleccion == "1":
        # a. Llamar funcionalidad de cargar archivo
        path = input("Ingrese la ruta del archivo de notas (o presione Enter para usar la ruta por defecto): ")
        if path.strip() == "":
            notas_estudiantes = func.cargar_notas()
        else:
            notas_estudiantes = func.cargar_notas(path)
        print("Datos cargados exitosamente.")
        for estudiante, notas in notas_estudiantes.items():
            print(f"Estudiante ID: {estudiante}, Notas: {notas}")
        pass

    elif seleccion == "2":
        # a. Solicitar documento
        documento = input("Ingrese el número de documento del estudiante a eliminar: ")
        # b. Eliminar estudiante y sus notas
        func.eliminar_estudiante(notas_estudiantes, documento) #    El usuario ingresa un número de documento
        for estudiante, notas in notas_estudiantes.items():
            print(f"Estudiante ID: {estudiante}, Notas: {notas}")
        #assert notas_estudiantes == {}, "No se han cargado los datos correctamente, vuelva a cargarlo e intentalo nuevamente."
        pass

    elif seleccion == "3":
        # a. Solicitar identificación del estudiante
        documento = input("Ingrese el número de documento del estudiante a comparar : ")
        # b. Buscar su mayor nota
        mayor_nota = func.mayor_nota_estudiante(notas_estudiantes, documento)
        print("notas estudiantes : ",notas_estudiantes)
        # c. Mostrar resultado al usuario
        if mayor_nota[0] is not None:
            print(f"La mayor nota del estudiante {documento} es: {mayor_nota[0]} en el Curso {mayor_nota[1]+1}")
        else:
            print(f"No se encontró al estudiante con ID {documento}.")
        pass

    elif seleccion == "4":
        # a. Aplicar burbuja a los promedios
        ordenados_burbuja = func.ordenar_promedios_burbuja(notas_estudiantes)
        # b. Mostrar lista ordenada
        print("Estudiantes ordenados por promedio (Burbuja):")
        for estudiante, promedio, x in ordenados_burbuja:
            print(f"Estudiante ID: {estudiante}, Promedio: {promedio}")
        pass

    elif seleccion == "5":
        # a. Aplicar selección según cursos matriculados
        ordenados_seleccion = func.ordenar_materias_seleccion(notas_estudiantes)
        # b. Mostrar resultado
        print("Estudiantes ordenados por cantidad de cursos (Selección):")
        for estudiante, promedio, cantidad_cursos in ordenados_seleccion:
            print(f"Estudiante ID: {estudiante}, Cantidad de cursos: {cantidad_cursos}")
        pass

    elif seleccion == "6":
        # a. Salir del programa
        break

    # 9. Si el usuario ingresa una opción inválida, volver a mostrar el menú
