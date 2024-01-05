#escribir un programa que pregunte al usuario los numeros ganadores de la loteria, los almacene  en una lista y los muestre por pantalla de menor a mayor

nros_ganadores = []
for i in range (6):
    nros_ganadores.append(int(input("ingrese los numeros ganadores: ")))
nros_ganadores.sort()
print("los numeros ganadores son,"+ str(nros_ganadores))

#ejercicio 2
#escribir un programa que almacene en una lista los siguientes valores y 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los valores sin utilizar min y max

valores = [50,75,46,22,80,65,8]
minimo = valores[0]
maximo = valores[0]

for valor in valores:
    if valor < minimo:
        minimo = valor
    if valor > maximo:
        maximo = valor
print(f"el minimo es {minimo} y el maximo es {maximo}")

#ejercicio 3 
# escribir un programa que almacenen los vectores (1,2,3) y (-1,0,2) en dos tuplas y muestre por pantalla su producto escalar

a = (1,2,3)
b = (-1,0,2)
producto = 0
for i in range(len(a)):
    producto = producto + (a[i]* b[i])
print(f"el producto de los vectores es "+str(producto))    
#ejercicio 4
# escribir un programa que almacene las matrices A Y B en una tupla y muestre por pantalla 
#su producto
# A = ((1,2,3)
#      (4,5,6))

# B = ((-1,0)
#       (0,1)
#        (-1,1))
A = ((1,2,3),
      (4,5,6))

B =     ((-1,0),
        (0,1),
        (-1,1))
resultado = [[0,0],
             [0,0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            resultado[i][j] += A[i][k] * B[k][j]

for i in resultado:
    print(i)