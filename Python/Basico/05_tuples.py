### Tuplas ###
my_tuple = ()
my_other_tuple = ()


my_tuple = (28, 1.75, "Pedro", "Contrera", "Pedro")
print(my_tuple) # Imprime la tupla vacía
print(type(my_tuple)) # Imprime el tipo de dato de la tupla vacía

print(my_tuple[0])# Imprime el primer elemento de la tupla 
print(my_tuple[-1])# Imprime el último elemento de la tupla        

print(my_tuple.count("Pedro")) # Cuenta cuántas veces aparece "Pedro" en la tupla
print(my_tuple.index("Contrera")) # Imprime el índice de la primera aparición de "Contrera" en la tupla     
print(f"Elementos de la tupla desde el índice 2 hasta el 4: {my_tuple[2:4]}") # Imprime los elementos de la tupla desde el índice 2 hasta el 4