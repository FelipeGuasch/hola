#ejercicio2: escribir una función que calcule el maximo comun divisor de dos numeros y otra que calcule el minimo comun multiple

def mcd(a,b):
    resto = 0
    while b > 0:
        resto = b
        b = a % b 
        a = resto
    return a
print(mcd(54,72))