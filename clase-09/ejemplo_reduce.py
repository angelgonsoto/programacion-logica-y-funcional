#reduce con estructuras de datos

from functools import reduce
 
ventas = [
    {"Producto": "Laptop", "monto":1500},
    {"Producto": "Mouse", "monto":350},
    {"Producto": "Teclado","monto":800},
    {"Producto": "monitor","monto":4000}
]
 
total = reduce(lambda ac,v:ac + v["monto"],ventas,0)
 
print(total)