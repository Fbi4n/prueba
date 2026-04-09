### Excepciones en Python ###
n1 = 5
n2 = "5"
#n2 = 5 # Convertimos el string a entero para evitar el error al sumar un entero con un string

### Try except ###
try:
    print(n1 + n2)
    print("La suma se ha realizado correctamente")
except:# Si se produce un error en el bloque try, se ejecuta el bloque except
    print("Se ha producido un error al intentar sumar un entero con un string")

### Try except else ###
try:
    print(n1 + n2)
    print("La suma se ha realizado correctamente")
except:
    print("Se ha producido un error al intentar sumar un entero con un string")
else:# Si no se produce ningún error en el bloque try, se ejecuta el bloque else
    print("La suma se ha realizado correctamente, no se han producido errores")
finally:# El bloque finally se ejecuta siempre, haya habido un error o no en el bloque try
    print("La ejecución del bloque try except ha finalizado") # El bloque finally se ejecuta siempre, haya habido un error o no en el bloque try


