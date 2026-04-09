### Condicionales en Python ###
my_condition = True

if my_condition:
    print("La condición es verdadera se ejecuta el if")

my_condition = 5*5

if my_condition == 10:
    print("La condición es verdadera se ejecuta el segundo if")

if my_condition > 10 and my_condition < 20:
    print("Es mayor a 10 y menor a 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual a 10 o mayor o igual a 20 y diferente a 25")

print("La ejecución continúa") 