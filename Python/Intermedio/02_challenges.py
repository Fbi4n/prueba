### Retos ###
"""
EL FAMOSO FIZZBUZZ
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 """
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizzbuzz()  

"""
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
 """

def are_anagrams(word_one, word_two):#definimos la función que recibe dos palabras como argumentos
    if word_one.lower() == word_two.lower(): #comprobamos si las palabras son exactamente iguales
        return False #si son iguales, retornamos falso  
    return sorted(word_one.lower()) == sorted(word_two.lower()) #comparamos las palabras ordenadas alfabéticamente y en minúsculas, si son iguales, retornamos verdadero, si no, falso
    
print(are_anagrams("amor", "roma")) #llamamos a la función con dos palabras que 


"""
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
 """
def fibonacci(n):
    prev , next = 0, 1 #inicializamos los dos primeros números de la sucesión
    for i in range(n): #iteramos n veces para generar los números de la sucesión
        print(prev) #imprimimos el número actual
        prev , next = next, prev + next #actualizamos los valores de prev y next para el siguiente número de la sucesión
fibonacci(50) #llamamos a la función para imprimir los primeros 50 números de la sucesión de Fibonacci


"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
def is_prime():#definimos la función que no recibe argumentos, ya que vamos a comprobar los números del 1 al 100

    for number in range(1, 101):# iteramos desde 1 hasta 100 para comprobar si cada número es primo
        if number >= 2:# los números menores que 2 no son primos, por lo que solo comprobamos a partir del 2
            is_divisible = False# inicializamos una variable para indicar si el número es divisible por algún otro número distinto de 1 y él mismo

            for index in range(2, number):# iteramos desde 2 hasta el número actual para comprobar si es divisible por algún número en ese rango
                if number % index == 0:# si el número es divisible por index, entonces no es primo
                    is_divisible = True# marcamos que el número es divisible por otro número distinto de 1 y él mismo
                    break

            if not is_divisible:# si el número no es divisible por ningún otro número distinto de 1 y él mismo, entonces es primo
                print(number)


is_prime()#llamamos a la función para comprobar si el número 7 es primo

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
def reverse(text):# definimos la función que recibe una cadena de texto como argumento
    
    text_len = len(text)# obtenemos la longitud de la cadena de texto
    reversed_text = ""# inicializamos una variable para almacenar la cadena de texto invertida
    
    for index in range(0, text_len):# iteramos desde 0 hasta la longitud de la cadena de texto para construir la cadena de texto invertida
        reversed_text += text[text_len - index - 1]# agregamos el carácter correspondiente al índice invertido a la variable reversed_text
    return reversed_text


print(reverse("Hola mundo"))