#ejejcicio 1 crea una tupla y acceder a sus elementos 
#crea una tupla con al menos 5 elentos de diferentes tipos(por ejemplo, entero, foltante, cadena , etc), luego, accede y muestre el primer y ultimo elemento del tupla  
tupla = (1, False, "probando", 6.6, (1,2,23), "otro texto", 25)
print(tupla[0])
print(tupla[-1])

#ejejcicio 2 concadenar 2 tuplas
#dadas 2 tuplas, concadenadas para formar una nueva tupla 

tupla1 = (1,2,3)
tupla2 = ('a','b','c')
print(tupla1 + tupla2)
#tupla3 = tupla 1 + tupla 2
#print(tupla3)

#conjuntos

#los conjuntos son colecciones no ordenadas y sin elmentos duplicados, son utiles para realizar operaciones de conjuntos como uniones, intercecciones, etc

#ejemplo

conjunto = (1,2,3,4,5,5,4,3,2,1)
print(conjunto)

#conjunto vacio
conjunto_vacio = set()

#conjunto_2 = {1,"juan",5.3, True, (1,2,3), [1,2,3]}
#print(conjunto_2)
#los conjuntos no pueden contener listas 

#no tienen orden 
conjunto_3 = {1,2,3,4,5}
#print(conjunto[0]) #error

#añadir elementos

conjunto_3.add(6)
print(conjunto_3)  

#eleminar un elemento
conjunto_3.remove(2)
print(conjunto_3)

#conjunto A u B
conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9,0}
conjunto_union = conjunto_a.union(conjunto_b)
print(conjunto_union)

#Integracion a u b
conjunto_a = {1,2,3,4,5}
conjunto_b = {4,5,6,7,8}
conjunto_intereccion = conjunto_a.intersection(conjunto_b)
print(conjunto_intereccion)

#diferencia a - b
conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9,0}
conjunto_diferencia = conjunto_a.difference(conjunto_b)
print(conjunto_diferencia)

#diferencia simetrica (A u B) - ( A ∩ B ) - (A - B) -(B - A)
conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9,0}
conjunto_diferencia_simetrica = conjunto_a.symmetric_difference(conjunto_b)
print(conjunto_diferencia_simetrica)