import os

directorio = os.getcwd()
print("directorio"+directorio)

os.system('mkdir navidad')

os.system('mkdir dir1 dir2 dir3 dir4')

patch = "C:/Users/IngXX/Documents/GitHub/hola"

lista_dir = os.listdir(patch)
print(lista_dir)

print(os.name)

if os.path.exists("C:/Users/IngXX/Documents/GitHub/hola"):
    print("la ruta existe")
else:
    print("la ruta no existe")
    print("creando carpeta....")
    os.mkdir("C:/Users/IngXX/Documents/GitHub/hola")