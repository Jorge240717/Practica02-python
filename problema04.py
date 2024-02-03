def ingresar_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i + 1} del alumno {nombre}: "))
        notas.append(nota)
    return {"Alumno": nombre, "Notas": notas}
def imprimir_listado(alumnos):
    print("\nListado de Alumnos:")
    for alumno in alumnos:
        print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")
num_alumnos = int(input("Ingrese la cantidad de alumnos: "))
lista_alumnos = []
for _ in range(num_alumnos):
    nuevo_alumno = ingresar_alumno()
    lista_alumnos.append(nuevo_alumno)
imprimir_listado(lista_alumnos)