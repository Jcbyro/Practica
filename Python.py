print("Hello world")
                                                            ##### Variables #####
name = input("Nombre: ")
print("Hola, " + name)
                                                            ##### Formating Strings #####
#Tambien se puede escribir como
print(f"Hola, {name}")

                                                            ##### Conditions #####
num = int(input("Numero: "))
if num > 0:
    print("El numero es positivo")
elif num < 0:
    print("El numero es negativo")
else:
    print("El numero es 0")

                                                            ##### Sequences #####
                                                            ### Strings ###
Name = "Harry"
print(Name[0]) #Primera letra
print(Name[1]) #Segunda letra
print(Name[2]) #Tercera letra+
print(Name[3]) #Cuarta letra
print(Name[4]) #Quinta letra
#Tambien se puede escribir como

                                                            ### Lists ###
Nombres = ["Harry", "Ron", "Hermione"]
print(Nombres)
print(Nombres[1]) #Imprime el segundo elemento de la lista
Nombres.append("Draco") #.append (Agrega algo a la lista)
Nombres.sort() #.sort (Ordena la lista)
print(Nombres)

                                                            ### Tuples ###
point = (12.5, 10.6)

                                                            ### Sets ###
s = set() #Crea un set vacio
s.add(1) #Añade 1 al set
s.add(2)
s.add(3)
s.add(4)
s.add(3)
s.add(1)
s.remove(2) #Quita 2 del set
print(s)
print(f"El set tiene {len(s)} elementos") #len() me da la cantidad de elementos en el set que se ponga entre ()

                                                            ### Dictionaries ###
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
print(houses["Harry"]) #Imprime la casa de Harry
houses["Hermione"] = "Gryffindor"
print(houses["Hermione"])

                                                            ### Loops ###
for i in [0, 1, 2, 3, 4, 5]:
    print(i)
#Tambien se puede escribir como
for i in range(6):
    print(i)

Names = ["Harry", "Ron", "Hermione"]
for o in Names:
    print(o)

Nombre = "Harry"
for char in Nombre:   #Igual a print(Name[])
    print(char)

                                                            ##### Modules #####
def square(x):
    return x * x
for i in range(10):
    print(f"El cuadrado de {i} es {square(i)}")

                                                            ##### Object-Oriented Programming #####
class Point(): #Crea una nueva clase llamada "Point"
    def __init__(self, x, y):
        self.x = x #Asigna es valor de x
        self.y = y #Asigna es valor de y
p = Point(2, 8)
print(p.x) #Imprime el valor de x en p (es 2)
print(p.y) #Imprime el valor de y en p (es 8)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def add_passengers(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    def open_seats(self):
        return self.capacity - len(self.passengers)
flight = Flight(3) #Dice que la capacidad es de 3 pasajeros
people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person):
        print(f"{person} fue añadida al vuelo")
    else:
        print(f"No hay espacio disponible para {person}")

                                                            ##### Functional Programming #####
                                                            ### Decorators ###
def announce(f):
    def wrapper():
        print("A punto de correr la funcion")
        f()
        print("Fue terminada la funcion")
    return wrapper
@announce
def hello():
    print("Hola, mundillo!")
hello()

                                                            ##### Lambda Functions #####
# square = lambda x: x * x #
#Ejem.:
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]
#
def f(person):
    return person["name"]   #Esto crea un "key" que funciona para que el programa sepa que diccionario usar
                            #(es decir que use a "name" para ordenar en vez de "house")
people.sort(key=f)
#
#Lo que puse entre # tambien se puede escribir usando Lambda de esta manera
people.sort(key=lambda person: person["name"])
print(people)

                                                            ##### Exceptions #####
import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error, input invalido")
    sys.exit(1) #System exit
try:
    result = x / y
except ZeroDivisionError:
    print("Error, no se puede dividir por 0")
    sys.exit(1)
print(f"{x} / {y} = {result}")