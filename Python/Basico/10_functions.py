### Funciones Python ###
def my_function():
    print("Esta es una función")


my_function() # Llamada a la función para ejecutarla

def sum_two_values(value_1, value_2):
    print(value_1 + value_2) # Imprime la suma de los dos valores

sum_two_values(5, 7) # Llamada a la función con dos argumentos para ejecutar la suma  
sum_two_values(235, 185) # Llamada a la función con dos argumentos para ejecutar la suma  

def sum_two_values_and_return(value_1, value_2):
   return value_1 + value_2 # Devuelve la suma de los dos valores

result = sum_two_values_and_return(10, 5) # Llamada a la función con dos argumentos para ejecutar la suma y devolver el resultado
print(f"La suma es: {result}")
