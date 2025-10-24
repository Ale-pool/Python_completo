# # -*- coding: utf-8 -*-
# """
# Created on Thu Oct 23 15:29:35 2025

# @author: alexv
# """

# # FUNCIONES
# """
# - Una función es un bloque de codigo reutizable, que realiza una tarea (opcionalmente )
#  devuelve un resultado
 
# - Porque usarlas? 

# Reutilización de codigo -> evita duplicados
# Modularidad -> divide el problema en piezas manejables
# Legibilidad -> Nombres descriptivos que muestran intención
# Testibilidad -> cada función se puede probar aisladamente
# Abstracción -> Ocultas detalles internos

# sintaxis basica de una función:
    
#     def saludar(nombre):
#         print(f"Hola, {nombre} como estas")


#     saludar("Alex")
    

# - def  + nombre + parentesis + : -> 
# - bloque indentando es el cuerpo
# - return devuelve valores, si no hay return devuelve None



# """

# def sumar(a, b):
#     return a  +  b

# r = sumar(2, 10)


# # parametros y argumentos (posicioanes y nombrados)
# # - parametro: es el nombre de la variable que se especifica en la definición de la función. Actúa como un marcador de posición para el valor que se le pasará.
# # - Argumento: es el valor real que se pasa a la función cuando esta es llamada o ejecutada.

# def info(nombre, edad):
#     print(f"Mi nombre es {nombre}, y tengo {edad} años")
    

# # info("Alex", 24) # argumentos posicionales
# info(edad = 25, nombre = "Luis") # argumentos nombrados Keywords


# # Valores por defecto

# def saludar(nombre= "Invitado"):
#     print(f"Hola, {nombre}")
    
    
# saludar()
# saludar("Luis")

# # parametros args y kwargs(flexibilidad)
# # - args => recibe una tupla, con argumentos posicionales extra
# # kwargs => recibe un diccionario con argumentos nombradas extra
# # Usos: wrappers, APIs flexibles, forwarding de argumentos.
# def mi_funcion(a, *args, **kwargs):
#     print("a:", a)
#     print("args :", args)
#     print("kwargs :", kwargs) 
    
# mi_funcion("Hola", 2, 3,7, l = 4,  x=10, y=20)

# # Anotaciones de tipos (type hints)
# # No afectan la ejecución, ayudan a lectura y herramientas (mypy, linters).



# # from typing import List, Tuple, Dict, Optional
# """
# def promedio(nums: List[float]) -> Optional[float]:  
#     if not nums:
#         return None
#     return sum(nums) / len(nums)
# """
# """
# -> Optional[float]: Esto es una anotación de retorno. Le dice al programador que la función puede devolver dos tipos de valores:

# Un número de punto flotante (float) (el promedio calculado).

# El valor None (en el caso de la lista vacía).

# Docstring de funciones (documentación interna de la función)

def factorial(n: int) -> int:  # -> int la funcion esta diseñada para recibir un entero
    """
    Calcula el factorial de un número entero no negativo n.

    Parámetros:
    n (int): Un número entero no negativo cuyo factorial se va a calcular.

    Retorna:
    int: El factorial de n.

    Ejemplos:
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    if n == 0: return 1
    prod = 1
    for i in range(1, n + 1):
        prod *=  i
    return prod

print(factorial(7))
help(factorial)


# Ámbito (scope) y variables locales vs globales
#Variables definidas en función → locales.
#Variables fuera → globales (evitar su uso excesivo).

x = 10 # global

def prueba():
    x = 5 # local
    print(x)
    
#prueba()
#print(x)

# Closures (funciones que recuerdan su entorno)
#Una función que devuelve otra y la interna «recuerda» variables.


def multiplicador(factor):
    def multiplicar(n):
        return n * factor
    return multiplicar

doble = multiplicador(4)
print(doble(5))

# Funciones de orden superior (recibir o devolver funciones)
def aplicar(f, lista):
    return [f(x) for x in lista]

print(aplicar(lambda x: x*2, [1,2,3]))  # [2,4,6]



def super_funion(*args, **kwargs):
    t = 0
    for a in args:
        t+= a
    print("Sumatorio indeterminado", t)
    for k in kwargs:
        print(k, " ", kwargs[k])
        
super_funion(12.23,33.24,45.24, nombre = "Alex", edad = 24)

def cuenta_atras(num):
    num -=1
    if num > 0:
        print(num)
        #cuenta_atras(num)
    else:
        print("bommm!")

cuenta_atras(10)


def factorial(num):
    if num > 1:
        num = num * factorial(num -1)
    return num
    
factorial(7)

def suma(n):
    if  n > 1:
        n = n + suma(n-1)
    return n


suma(3)