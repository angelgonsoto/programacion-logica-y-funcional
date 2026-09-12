class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def es_mayor(self, fn):
        return fn(self.edad)

def mayor_Mexico(edad):
    return edad >= 18

def mayor_USA(edad):
    return edad >= 21

persona1 = Persona("Pedro", 18)

if persona1.es_mayor(mayor_Mexico):
    print("Es mayor en Mexico")
else:
    print("No es mayor en Mexico")

if persona1.es_mayor(mayor_USA):
    print("Es mayor en USA")
else:
    print("No es mayor en USA")