### Funciones de Orden Superior ###
from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five)) 


### Clousures ###
def sum_ten(original_value):#definimos la función que recibe un valor original como argumento
    def add(value):#definimos la función interna que recibe un valor como argumento
        return value + 10 + original_value #retornamos la suma del valor recibido, 10 y el valor original
    return add #retornamos la función interna, creando así un closure que mantiene el valor original en su contexto

add_closure = sum_ten(1)# llamamos a la función sum_ten con un valor original de 1, lo que crea un closure que mantiene ese valor en su contexto. La función add_closure ahora es una función que recibe un valor y le suma 10 y el valor original (1) cada vez que se llama.

print(add_closure(5))# llamamos a la función add_closure con un valor de 5, lo que retorna la suma de 5, 10 y el valor original (1), resultando en 16.
print(sum_ten(5)(1))# llamamos a la función sum_ten con un valor original de 5 y luego llamamos a la función interna add con un valor de 1, lo que retorna la suma de 1, 10 y el valor original (5), resultando en 16.

print("-------------")
### Built-in Higher-Order Functions ###
numbers = [2, 5, 10, 21, 30]

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))


def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

print("-------------")
### Reduce ###

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))