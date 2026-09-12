def calcular_precio(precio, fn):
    return fn(precio)

def precio_normal(precio):
    return precio

def precio_estudiante(precio):
    return precio * 0.8

def precio_vip(precio):
    return precio * 0.7

precio = 500
print(calcular_precio(precio, precio_normal))
print(calcular_precio(precio, precio_estudiante))
print(calcular_precio(precio, precio_vip))