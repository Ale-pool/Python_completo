# Vamos a tener los tres diferentes ejercicos optativos de la seccion 8 del curso de Python
"""
**1) Formatea los siguientes valores para mostrar el resultado indicado:**

* "Hola Mundo" → Alineado a la derecha en 20 caracteres
* "Hola Mundo" → Truncamiento en el cuarto carácter (índice 3)
* "Hola Mundo" → Alineamiento al centro en 20 caracteres con truncamiento en el segundo carácter (índice 1)
* 150 → Formateo a 5 números enteros rellenados con ceros
* 7887 → Formateo a 7 números enteros rellenados con espacios
* 20.02 → Formateo a 3 números enteros y 3 números decimales

"""

# formatear los siguientes valores

print(" ############### EJERCICIOS 1 ############### ")
# str
mensaje = "Hola mundo"
print("{:>20}".format(mensaje))
print("{:.3}".format(mensaje)) # truncamiento indice 3
print("{:^20.1}".format(mensaje))

# numeros
numero_1 = 150
numero_2 = 7887
numero_3 = 20.02

# formateo a 5 numeros enteros rellenados con cero
print("{:05d}".format(numero_1))

# formatea a 7 numeros enteros rellenandos con espacios 

print("{:7d}".format(numero_2))

# formateo a 3 numeros enteros y 3 numero decimales
print("{:07.3f}".format(numero_3))



"""
**2) Crea un script llamado tabla.py que realice las siguientes tareas:**
* Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
* El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
* En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
* El script contendrá un bucle for que itere el número de veces del primer argumento.
* Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
* Dentro del segundo for ejecuta una instrucción ** print(" * ", end='')**, (end='' evita el salto de línea).
* Ejecuta el código y observa el resultado.

** Ahora intenta deducir dónde y cómo añadir otra instruccion print para dibujar una tabla.**

*Recordatorio: Los argumentos se envían como cadenas separadas por espacios, si quieres enviar varias palabras como un argumento deberás indicarlas entre comillas dobles "esto es un argumento". Para capturar los argumentos debes utilizar el módulo **sys** y su lista **argv**:*
```python
import sys
print(sys.argv) # argumentos enviados
"""


print(" ############### EJERCICIOS 2 ############### ")
import sys

if len(sys.argv) == 3:
	filas = int(sys.argv[1])
	columnas = int(sys.argv[2])

	if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
		print("Error - Filas o columnas incorrectos")
		print("Ejemplo: tabla.py [1-9] [1-9]")
	else:
		# Aqui empieza la lógica
		for f in range(filas):
			print("")
			for c in range(columnas):
				print(" * ", end='')

else:
	print("Error - Argumentos incorrectos")
	print("Ejemplo: tabla.py [1-9] [1-9]")
	

