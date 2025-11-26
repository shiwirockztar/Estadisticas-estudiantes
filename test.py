import modules.functions as func
notas_dict = func.cargar_notas("./database/notas_estudiantes.csv")
for estudiante, notas in notas_dict.items():
    print(f"Estudiante ID: {estudiante}, Notas: {notas}")
mayor_nota = func.mayor_nota_estudiante(notas_dict, "1033492448")
print(f"La mayor nota del estudiante 1033492448 es: {mayor_nota[0]} en el Curso{mayor_nota[1]+1}")


