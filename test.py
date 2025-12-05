import modules.functions as func
estudiantes, cursos, notas = func.cargar_notas()  
"""
print("Antes de eliminar:")
print("Estudiantes:", estudiantes)
print("Notas:", notas)  

func.eliminar_estudiante(estudiantes, notas, '1032090603')
print("\nDespués de eliminar:") 
print("Estudiantes:", estudiantes)
print("Notas:", notas)     

print("\nProbando mayor_nota_estudiante:")
id_estudiante = '1033492448'
max_nota, curso_index = func.mayor_nota_estudiante(estudiantes, notas, id_estudiante)
if max_nota is not None:
    print(f"La mayor nota del estudiante {id_estudiante} es {max_nota} en el curso con índice {curso_index}.")
else:
    print(f"No se encontró al estudiante con ID {id_estudiante}.")  


promedios = func.obtener_promedios(notas)   
print("\nPromedios de los estudiantes:")
print(promedios) 
promedios_ordenados = func.sort_bubble(promedios)
print("\nPromedios ordenados de los estudiantes:")
print(promedios_ordenados)

print("\nEstudiantes:", estudiantes)
"""
print("\nListado de estudiantes ordenados por promedio:")
estudiantes_ordenados = func.ordenar_estudiantes_burbuja(estudiantes, notas)
print(estudiantes_ordenados)
print("\nCantidad de materias cursadas por estudiante:")
func.ordenar_materias_seleccion(estudiantes, notas)
#print(orden)