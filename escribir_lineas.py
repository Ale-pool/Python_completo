import sys


# salidad
# vamos a usar el .format para formatear cadenas, esto nos sirve para insertar variables dentro de cadenas

v = "Otra cadena"
n = 44
c = " un texto {}, y un numero {}".format(v, n)
print(c)


# podemos hacerlo de otra forma de otra forma
print("{v}, {v}, {v}".format(v=v))
