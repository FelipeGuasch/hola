#1 reciba un nombre para la carpeta
import os
nombre = input("inmgrese le nombre de la carpeta: ")
os.system(f'mkdir {nombre}')

directorio = os.getcwd()
print("directorio"+directorio)
