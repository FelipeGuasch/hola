#ejercicio: cree un programa que almaceneen un archivo la fecha y hora en que se ejecuto ese archivo, ademas debe mantener un registro de todas las 
import datetime
print(datetime.datetime.now())

def guardar_registro():
    with open("log.txt","a", encoding="utf-8") as archivo:
        archivo.write(str(datetime.datetime.now()))
        archivo.write("\n")
guardar_registro()