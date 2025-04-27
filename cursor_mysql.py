import csv
import mysql.connector

conexion= mysql.connector.connect(
     host='localhost',
    user='root',
    password='root',
    database='ddm'
)
cursor = conexion.cursor()

# Leer el CSV
with open('tc.csv', encoding='utf-8') as archivo:
    reader = csv.reader(archivo)
    filas = list(reader)
# Procesar en bloques de 4
for i in range(0, len(filas), 4):
    if i + 3 >= len(filas):  # Checar que existan 4 filas
        print(f"Bloque incompleto en el índice {i}. Se detiene.")
        break

    nombre = filas[i][0]
    materia = filas[i+1][0]
    descripcion = filas[i+2][0]
    fecha = filas[i+3][0]

    # Insertar en MySQL
    cursor.execute("""
        INSERT INTO informacion (nombre, materia, descripcion, fecha)
        VALUES (%s, %s, %s, %s)
    """, (nombre, materia, descripcion, fecha))
conexion.commit()
cursor.close()
conexion.close()