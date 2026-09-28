# RECURSIVIDAD

"""
La recursividad es una tecnica donde una función se llama a si misma
para resolver un problema dividiendolo en subproblemas más pequeños.

Estructura de una función recursiva:
* Condición que detiene la recursión.
* Llamada a si misma con datos reducidos.
"""

def cuenta_regresiva(n):
    if n <= 0:
        print("!Inicio!")
        return
    print(n)
    cuenta_regresiva(n-1)

cuenta_regresiva(5)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(4))

def suma_digitos(n):
    if (n <= 10):
        return n
    return (n % 10) + suma_digitos(n // 10)
print(suma_digitos(1234))