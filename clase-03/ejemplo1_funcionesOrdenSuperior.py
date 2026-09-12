"""
Las funciones de orden superior nos permiten encapsular
el comportamiento de una funcion y usarlo en otra enviando
la funcion como argumento.
Cabe mencionar que el comportamiento de la funcion enviada como argumento
no se puede extender localmente por la misma logica de estas funciones.
"""

def sumar(x, y):
    return x + y

def multiplicar(x, y):
    return x * y

def operar(x, y, fn):
    return fn(x, y)

print(operar(2, 5, sumar))
print(operar(100, 50, multiplicar))