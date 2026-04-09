### Loops ###

# Bucle while
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1 # Incrementa el valor de la condición en 1
else:
    print("Mi condición es mayor o igual a 10") 

print("Ya se ha cumplido la condición")

print("----------------")   

### Bucle for
my_list = [35, 24, 62, 52, 30, 30, 17]
suma = 0
for element in my_list[-1:]: # Itera sobre cada elemento de la lista desde el último elemento hasta el final de la lista
    suma += element
    print(element) # Imprime cada elemento de la lista
print(f"La suma de los elementos es: {suma}") # Imprime la suma de los elementos de la lista

print("----------------")
my_other_list = ["Pedro", 28, 1.75, "Contrera", True]   
for element in my_other_list: # Itera sobre cada elemento de la lista desde el último elemento hasta el final de la lista
    print(element) #
    if element == "Contrera":
        break # Detiene la ejecución del bucle cuando se encuentra el elemento "Contrera"
    print("Se ejecuta el bucle") # Imprime un mensaje indicando que se ejecuta el bucle
else:
    print("El bucle for ha finalizado") # Imprime un mensaje indicando que el bucle for ha finalizado   