#Variables
my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))


my_bool_variable = False
print(my_bool_variable)

#Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

#funciones del sistema
print(len(my_string_variable))

#Variables de una sola línea >>>>Cuidado con su Uso!
name, surname, alias, age = "Pedro", "Contrera", "Fabian", 28
print("Mi nombre es:", name, surname, "y tengo", age, "años.")


#Inputs
first_name = input("¿Cuál es tu nombre? ")
age = input("¿Cuál es tu edad? ")

print(first_name)
print(age)

#Forzamos el tipo de dato 
address: str = "Mi dirección es:"
address = True
address = 5
address = 1.5
address = 3 + 1j
print(type(address))
