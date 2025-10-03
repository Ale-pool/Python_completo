# Podemos afirmar que la función enumerate()
# es trasformar una lista de elementos normales a una lista con subtuplas, que contienen la posición de cada elemento y su valor
# En este caso se estudiara sobre una función en específico
# enumerate()
# la funcion enumerate(iterable, start=0) nos per una secuencia(lista, tupla,cadena, etc)
# y al mismo tiempo obtener el indice de cada elemento
#  sin numerate manejas normal -> for i in range(len(iterable))

# elementos = ["Hola", 6, "Bien", [1,2,4]]
# for i,e in enumerate(elementos):
#     print(i,e)

# queremos mostar los elementos de una lista con su posición

Frutas = ["manzana", "pera", "uva"]

for indice, fruta in enumerate(Frutas):
    print(f"indice : {indice}, Frutas : {fruta}")

# Si queremos cambiar el inicio del indice (no desde 0)

nombres = ["Ana", "Luis", "Carlos"]

for numero, nombre in enumerate(nombres, start=1):
    print(f"{numero} : {nombre}")


# Si queremos Buscar un elemento por su posición

colores = ["rojo", "verde", "azul", "amarillo"]

for elemento, color in enumerate(colores):
    if color == "rojo":
        print("el color amarillo esta en la posición", elemento)


#Ejemplo 4: Iterar cadenas con posición
#Descripción: Queremos recorrer una palabra y mostrar la posición de cada letra.

palabra = "Python"

for indice, cadena in enumerate(palabra):
     print(f"Letra : {indice} : {cadena}")


#Ejemplo 5: Usar enumerate para actualizar una lista
# usar enumera  para actualizar una lista

"""
Descripción: Queremos recorrer una lista de números y reemplazar los valores negativos por 0, usando el índice que nos da enumerate.
"""

numeros = [5, -3, 7, -1, 4]

for i, num in enumerate(numeros):
      if num < 0:
           numeros[i]  = 0   # modificamos utilizando el indice

print(numeros)


"""
Ejemplo 6: Enumerar diccionarios (avanzado)

Descripción: Queremos numerar pares clave-valor de un diccionario.
"""

edades = {"Ana": 25, "Luis": 30, "Carlos": 28}

for i, (nombre, edad) in enumerate(edades.items(), start=1):
    print(f"{i}. {nombre} -> {edad} años")

"""
Conclusiones 

enumerate() es ideal cuando necesitas índices + valores al mismo tiempo.

Puedes usar start para cambiar el índice inicial.

Funciona con listas, cadenas, tuplas, sets, diccionarios y cualquier iterable.

Es muy útil en búsquedas, modificaciones y numeración de elementos.
"""


# Ejercicio:

"""
En este ejercicio se te va a facilitar una variable iniciales que contiene una lista con un número indeterminado de cadenas de texto.

Tu objetivo es modificar las cadenas de esa lista por la letra inicial de cada cadena en la lista utilizando, si lo requieres, la función enumerate.

Supongamos que iniciales tiene el siguiente valor ["Hola", "Mundo"], tu objetivo sería transformar esos valores a ["H", "M"].
"""

iniciales = ["Hola", "Mundo", "Python", "Es", "Genial"]
for i, palabra in enumerate(iniciales):
    iniciales[i] = palabra[0]

print(iniciales)


# ejercicio 2
"""

Iteraciones y conversiones
Pide al usuario que introduzca un número entero por teclado entre 1 y 9 (ambos incluidos) y guárdalo en la variable numero.
 Debes asegurarte de que esa variable numero contiene un numero entero del 1 al 9, utiliza un bucle para repetir la lectura hasta 
 que se cumpla esa condición.
"""
while(True):
    numero = int(input("Introduce un número entero entre 1 y 9: "))
    if 1 <= numero <= 9:
        break
    else:
        print("Número inválido. Inténtalo de nuevo.")


# ejercicio 3

"""
Genera una lista llamada multiplos que contenga los múltiplos de numero en el rango de 1 a 100 (ambos incluidos)
 utilizando la conversión de un range a list con un paso: list(range(Min,Max,Paso)).
"""
multiplos = list(range(numero, 101, numero))
print(multiplos)