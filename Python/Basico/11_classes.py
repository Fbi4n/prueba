### Clases ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson) # Imprime la clase MyEmptyPerson
print(type(MyEmptyPerson)) # Imprime el tipo de dato de la clase MyEmptyPerson  

print("-----------------")
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height    

person = Person("Alice", 30, 170)
print(f"Nombre: {person.name}, Edad: {person.age}, Altura en cm: {person.height}") # Imprime los atributos del objeto person  

print("-----------------")
class MyPerson:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}" # Atributo que combina el nombre y el apellido  

my_person = MyPerson("Pedro", "Contrera")
print(my_person.full_name) # Imprime el atributo full_name del objeto my_person

