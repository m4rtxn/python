import csv


datos_nuevos = [['g1'], ['g2'], ['g3'],['g4']]
with open('datos1col.csv', mode='a', newline='',encoding='utf-8') as datacsv:
    informacion_write=csv.writer(datacsv)

    informacion_write.writerows(datos_nuevos)
with open ('datos1col.csv', mode='r',newline='',encoding='utf-8') as datacsv:
    informacion_read=csv.reader(datacsv)

    for i in informacion_read:
        print(i)  
