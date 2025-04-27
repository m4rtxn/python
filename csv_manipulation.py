import csv

# with open ('data_ddm_tst.csv',mode='r', newline='',encoding='utf-8') as archivo:
#     lector=csv.reader(archivo)

#     for fila in lector:
#         print(fila)


# newData = [
#     ['Nuevo Nombre 2'],
#     ['Nuevo nombre 3']
# ]

# with open ('ddm_data_test2.csv',mode='w',newline='',encoding='utf-8') as datacsv:
#     informacion=csv.writer(datacsv)

#     informacion.writerow(newData)

# with open('ddm_data_test2.csv',mode='r',newline='',encoding='utf-8') as datacsv:
#     informacion_read=csv.reader(datacsv)

#     for i in informacion_read:
#         print(i)

datos_nuevos = [['x1'], ['x2'], ['x3'],['x4']]

# with open ('datos1col.csv', mode='r',newline='',encoding='utf-8') as datacsv:
#     informacion_read=csv.reader(datacsv)

#     for i in informacion_read:
#         print(i)  

with open('datos1col.csv', mode='a', newline='',encoding='utf-8') as datacsv:
    informacion_write=csv.writer(datacsv)

    informacion_write.writerows(datos_nuevos)
with open ('datos1col.csv', mode='r',newline='',encoding='utf-8') as datacsv:
    informacion_read=csv.reader(datacsv)

    for i in informacion_read:
        print(i)  


# with open('ddm_data_test2.csv',mode='r',newline='',encoding='utf-8') as datacsv:
#      informacion_read=csv.reader(datacsv)

#      for i in informacion_read:
#          print(i)