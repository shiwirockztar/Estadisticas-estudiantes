import modules.functions as func
notas_dict = func.cargar_notas("./database/notas_estudiantes.csv")
for estudiante, notas in notas_dict.items():
    print(f"Estudiante ID: {estudiante}, Notas: {notas}")
nuevas_notas = func.eliminar_estudiante(notas_dict, "1033492448")
#print(nuevas_notas)
for estudiante, notas in nuevas_notas.items():
    print(f"Estudiante ID: {estudiante}, Notas: {notas}")



