### Strings Python ###
my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string)) # Función para obtener la longitud de un string
print(len(my_other_string)) # Concatenación de strings
print(my_string + " " + my_other_string) # Concatenación de strings con espacio

my_new_line_string = "Este es un string\ncon salto de línea"
print(my_new_line_string) # Imprime el string con salto de línea

my_tab_string = "Este es un string\tcon tabulación"
print(my_tab_string) # Imprime el string con tabulación

my_scaped_string = "Este es un string con comillas \"dobles\" y comillas \'simples\'"
print(my_scaped_string) # Imprime el string con comillas escapadas

print("----------------")
### Formateo de Strings ###
name, surname, age = "Pedro", "Contrera", 28

print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Formateo de strings con f-strings (Python 3.6+)        

print("----------------")
### Desempaquetado de caracteres ###
first_char = name[0]
last_char = name[-1]
print(f"Primer carácter: {first_char}")
print(f"Último carácter: {last_char}")  


print("----------------")
### División de caracteres ###
substring = name[2:4] # Obtiene los caracteres desde el índice 0 hasta el 4 (excluyendo el 4)
print(f"Subcadena: {substring}")    


print("----------------")
### Funciones ###
print(name.upper()) # Convierte el string a mayúsculas
print(name.lower()) # Convierte el string a minúsculas      
print(name.isupper()) # Verifica si el string está en mayúsculas
print(name.islower()) # Verifica si el string está en minúsculas
print(name.startswith("P")) # Verifica si el string comienza con "P"
print(name.endswith("a")) # Verifica si el string termina con "a"
print(name.split("e")) # Divide el string en una lista utilizando "e" como separador
print(name.find("d")) # Encuentra la posición de la primera aparición de "d" en el string
print(name.replace("e", "x")) # Reemplaza todas las apariciones de "e" por "x" en el string
print(surname.count("a")) # Cuenta el número de apariciones de "a" en el string
