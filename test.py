import modules.functions as func
notas_dict = func.cargar_notas("./database/notas_estudiantes.csv")
for estudiante, notas in notas_dict.items():
    print(f"Estudiante ID: {estudiante}, Notas: {notas}")
#mayor_nota = func.mayor_nota_estudiante(notas_dict, "1033492448")
#print(f"La mayor nota del estudiante 1033492448 es: {mayor_nota[0]} en el Curso{mayor_nota[1]+1}")


print(notas_dict)

ordenados_burbuja = func.ordenar_promedios_burbuja(notas_dict)
print("Estudiantes ordenados por promedio (Burbuja):")
#print(ordenados_burbuja)
for estudiante, promedio, _ in ordenados_burbuja:
    print(f"Estudiante ID: {estudiante}, Promedio: {promedio}")

#cantidades_cursos = func.promedio_cursos_seleccion(notas_dict)
ordenados_seleccion = func.ordenar_materias_seleccion(notas_dict)
print("Estudiantes ordenados por cantidad de cursos (Selección):")
for estudiante, _, cantidad in ordenados_seleccion:
    print(f"Estudiante ID: {estudiante}, Cantidad de cursos: {cantidad}")
#print(ordenados_seleccion)