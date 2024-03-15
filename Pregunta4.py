listado_alumnos =[]

num_alumnos = int(input("Ingrese la cantidad de alumnos a registrar:"))

for i in range(num_alumnos):
    nombre_alumno = input(f"Ingrese el nombre del alumno {i+1}:")
    notas_alumno =[]
    for j in range(3):
        nota = float(input(f"Ingrese la calificacion {j+1} del alumno {nombre_alumno}:"))
        notas_alumno.append(nota)

    alumno = {
        'Alumno' : nombre_alumno,
        'Notas'  : notas_alumno
     }   
    
    listado_alumnos.append(alumno)


print("\nlistado completo de alumnos:")
for alumno in listado_alumnos:
    print(alumno)