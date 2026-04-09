### Listas ###

my_list = list() # Creación de una lista vacía utilizando la función list()
my_other_list = [] # Creación de una lista vacía utilizando corchetes

print(len(my_list)) # Función para obtener la longitud de una lista

my_list = [35, 24, 62, 52, 30, 30, 17]

print(f"La lista tine los suiguientes numeros:\n {my_list}") # Imprime la lista completa
print(f"La longitud de la lista es: {len(my_list)}") # Imprime la longitud de la lista

print("----------------")

my_other_list = ["Pedro", 28, 1.75, "Contrera", True]
my_other_list.append("Python") # Agrega un elemento al final de la lista
my_other_list.insert(7, "Programador") # Inserta un elemento en una posición específica de la lista
print(f"La lista tiene los siguientes elementos:\n {my_other_list}") # Imprime la lista completa
print(f"La longitud de la lista es: {len(my_other_list)}") # Imprime la longitud de la lista    

print("----------------")
print(type(my_other_list)) # Imprime el tipo de dato de la lista
print(type(my_other_list[0])) # Imprime el tipo de dato del último elemento de la lista
print(my_list.count(30)) # Cuenta cuántas veces aparece el número 30 en la lista
    
name, age, height, surname, is_single, language,occupation  = my_other_list # Desempaquetado de la lista en variables individuales
print(f"Nombre: {name}, Edad: {age}, Altura: {height}, Apellido: {surname}, Soltero: {is_single}, Lenguaje: {language}, Ocupación: {occupation}") # Imprime las variables desempaquetadas
