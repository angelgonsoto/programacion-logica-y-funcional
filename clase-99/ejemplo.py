#FUNCIONES LAMBDA.

#EJEMPLO 1:
a,b = 2, 4

#Funcion normal (sumar dos numeros)
def sumar(a, b):
    return a + b

print(sumar(a, b))

#Funcion lambda (sumar dos numeros)
print(lambda a, b: a + b)

# EJEMPLO 2:
constante = lambda: 42
print(constante()) #42
cuadrado = lambda x: x**2
print(cuadrado(10))

# EJEMPLO 3:
area_triangulo = lambda base, altura: (base*altura)/2
print(area_triangulo(10, 5))

# EJEMPLO 4:
es_par = lambda n: True if n % 2 == 0 else False
print(es_par(4)) # True
print(es_par(7)) # False