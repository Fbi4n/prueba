### Diccionarios en Python ###
my_dict = dict() # Creación de un diccionario vacío utilizando la función dict()
my_other_dict = {} # Creación de un diccionario vacío utilizando llaves 

my_other_dict = {"Nombre": "Pedro", "Edad": 28, "Altura": 1.75, "Apellido": "Contrera", "Soltero": True}
print(my_other_dict) # Imprime el diccionario completo
print(type(my_other_dict)) # Imprime el tipo de dato del diccionario


print(my_other_dict["Nombre"]) # Imprime el valor asociado a la clave "Nombre" en el diccionario
print(my_other_dict["Edad"]) # Imprime el valor asociado a la clave "Edad"      
print(my_other_dict["Altura"]) # Imprime el valor asociado a la clave "Altura"
print(my_other_dict["Apellido"]) # Imprime el valor asociado a la clave "Apellido"
print(my_other_dict["Soltero"]) # Imprime el valor asociado a la clave "Soltero"

print("----------------")
my_dict  = {"Nombre": "Pedro", "Edad": 28, "Altura": 1.75, "Apellido": {"Contrera", "Chavez"}}


print(f"Nombre: {my_dict['Nombre']}\nEdad: {my_dict['Edad']}\nAltura: {my_dict['Altura']}\nApellido: {my_dict['Apellido']}") # Imprime el valor asociado a la clave "Nombre"
