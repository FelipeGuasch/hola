# tuplas

# las tuplas son listas inmutables es decir no se pueden modificar
# las tuplas se definen con () y cada elemento separado con comas ,

# ejemplo

tupla = (1,2,3,4,5)

tupla_2 = (1, "hola", 3.5, True, [1,2,3], (1,2,3))

print(tupla[3])

# tupla[3] = 0 # genera un error

print(len(tupla))

# cuantos elementos repetidos hay
tupla_3 = (1,2,3,4,4,4,4,5)

print(tupla_3.count(4))

# concadenar dos tuplas

tupla_4 = (1,2,3)
tupla_5 = (4,5,6)
print(tupla_4 + tupla_5)

# ejercicio 1 crear una tupla y acceder a sus elementos
#crea una tupla con al menos 5 elementos de diferentes tipos(por ejemplo, entero, flotante, cadena, etc.). luego, accede y muestra el primer y ultimo elemento de la tupla 

tupla0 = (1, False, "probando", 6.6, (1,2,23), "otro texto", 25)
print(tupla0[0])
print(tupla0[-1])

# ejercicio 2 concadenar 2 tuplas 
# dadas 2 tuplas, concadenalas para formar una nueva tupla 

tupla1 = (1,2,3)
tupla2 = ('a','b','c')
print(tupla1 + tupla2)
#tupla3 = tupla1 + tupla2
#print(tupla3)

# conjuntos 

# los conjuntos son colecciones no ordenadas y sin elementos duplicados. son utiles para realizar operaciones de conjuntos como uniones, intersecciones, etc

# ejemplo

conjunto = {1,2,3,4,5,5,1,2,3,4}
print(conjunto)

#conjunto vacio
conjunto_vacio = set()

#conjunto_2 = {1,"juan", 5.3, True, (1,2,3), [1,2,3]}
#print(conjunto_2)
#los conjuntos no pueden contener listas 

# no tienen orden
conjunto_3 = {1,2,3,4,5}
# print(conjunto[0]) #error

#añadir elementos

conjunto_3.add(6)
print(conjunto_3)

#eliminar un elemento

conjunto_3.remove(2)
print(conjunto_3)

# union A U B

conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9,0}
conjunto_union = conjunto_a.union(conjunto_b)
print(conjunto_union)

# Interseccion a u b
conjunto_a = {1,2,3,4,5}
conjunto_b = {4,5,6,7,8}
conjunto_interseccion = conjunto_a.intersection(conjunto_b)
print(conjunto_interseccion)

# diferencia a - b

conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9,0}
conjunto_diferencia = conjunto_a.difference(conjunto_b)
print(conjunto_diferencia)

# diferencia simetrica (A U B) - (A u B) = (A - B) - (B - A)

conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9,0}
conjunto_diferencia_simetrica = conjunto_a.symmetric_difference(conjunto_b)
print(conjunto_diferencia_simetrica)

conjunto9 = set()

conjunto9.add(3)
conjunto9.add('c')
conjunto9.add(5.4)
print(conjunto9)

# ejercicio 2: crear un nuevo conjunto a partir del conjunto a = {1,2,3,4,5} cuyos valores sean el cuadrado de los elementos del conjunto a

A = {1,2,3,4,5}
B = set()

for elemento in A:
    B.add(elemento**2)
print(B)

# ejercicio 3 estudiantes en diferentes clases en la universidad, hay dos cursos: matematicas y literatura. tienes
#las listas de estudiantes que estan en ambos cursos 
# matematicas: ana, luis, pedro, maria
# lenguaje: juan, maria, ana, sofia

matematicas = {'ana','luis', 'pedro', 'maria'}
lenguaje = {'juan', 'maria','ana', 'sofia' }

estudiantes = matematicas.intersection(lenguaje)
print(estudiantes)

# diccionario

# un diccionario es una coleccion que utiliza para almacenar valores que tienen una relacion entre si. se diferencia de los conjuntos porque tiene una clave y valor. se definen con {}
# y separan los elementos por ,

# ejemplo 
diccionario = {
    "nombre" : "luigi",
    "apellido" : "bross",
    "apodo" : "mario verde"
}

print(diccionario['nombre'])
print(diccionario['apellido'])
print(diccionario['apodo'])

# largo del diccionario
print(len(diccionario))

#como agregar un elemento

diccionario["color"] = "verde"
print(diccionario)

#modificar elemento

diccionario['apodo'] = "el otro mario"
print(diccionario)

#como eliminar un elemento
diccionario.pop("apodo")
print(diccionario)

#retornas las claves/keys

print(diccionario.keys())

#retornar los valores

print(diccionario.values())

nombre = input("ingrese nombre: ")
edad = int(input("ingrese edad: "))
direccion = input("ingrese direccion: ")
telefono = input("ingrese telefono: ")

diccionario_1 = {}
diccionario_1["nombre"] = nombre
diccionario_1["edad"] = edad
diccionario_1["direccion"] = direccion
diccionario_1["telefono"] = telefono
print(diccionario_1)

diccionario_2 ={
    "nombre" : nombre,
    "edad" : edad,
    "direccion" : direccion,
    "telefono" : telefono
}
print(diccionario_2)

# escribir un programa que guarde los precios de las frutas de la tabla pregunta al usuario por una fruta , un numero de kilos y muestra por pantalla 
# fruta = platano, manzana, pera, naranja
# precio = 1.35, 0.80, 0.85, 0.75

frutas = {'platano' : 1.35, 'manzana': 0.80, 'pera': 0.85, 'naranja': 0.75}

fruta = input("¿que fruta queri conchetumare casero: ? ")
kg = float(input("¿cuantos kilos quiere: ? "))

if fruta in frutas:
    print(f"{kg} kilos de {fruta} vale ${kg * frutas[fruta]}")
else:
    print(f"{fruta} no se encuentra disponible")