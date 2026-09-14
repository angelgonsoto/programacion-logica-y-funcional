productos = [
    {"nombre": "Laptop", "precio": 15000, "categoria": "electronica"},
    {"nombre": "Camiseta", "precio": 250, "categoria": "ropa"},
    {"nombre": "Audifonos", "precio": 800, "categoria": "electronica"},
    {"nombre": "Zapatos", "precio": 1200, "categoria": "ropa"},
    {"nombre": "Tablet", "precio": 8000, "categoria": "electronica"},
    {"nombre": "Libro", "precio": 350, "categoria": "papeleria"},
]

resultadoFilter = filter(lambda x: x["precio"] <= 1000, productos)
print(list(resultadoFilter))

resultadoMap = list(map(lambda y: y["precio"] >= 1500, productos))
print(resultadoMap)

"""
Tema: Funciones map y filter usando expresiones lambda

filter es una funcion que filtra datos especificos de un arreglo usando una expresion
lambda

Map
"""