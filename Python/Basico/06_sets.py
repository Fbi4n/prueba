### Sets ###
my_set = set()
my_other_set = {"Pedro", "Contrera", 28, 1.75}

print(type(my_set)) # Imprime el tipo de dato del set vacío
print(type(my_other_set)) # Imprime el tipo de dato del set con elementos

print(len(my_other_set)) # Imprime la longitud del set con elementos

my_other_set.add("Python") # Agrega un elemento al set

print(my_other_set) # Set no es una estructura ordenada y no admite repetidos
