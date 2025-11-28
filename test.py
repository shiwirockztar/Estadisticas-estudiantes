import modules.functions as func
notas_dict = func.cargar_notas()  
ordenados = func.ordenar_materias_seleccion(notas_dict)
print("Estudiantes ordenados por cantidad de cursos (Selección):")
print(ordenados)


