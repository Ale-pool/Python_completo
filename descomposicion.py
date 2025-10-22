"""
**3) [Avanzado] Crea un script llamado descomposicion.py que realice las siguientes tareas:**
* Debe tomar 1 argumento que será un número entero positivo.
* En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.

** El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número:**

```
> 3647
```
** El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo: **

```
> 0007
  0040
  0600
  3000
```
*Pista: Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa*
"""	
print("################ FIN EJERCICIOS 3 ############### ")

import sys 

if len(sys.argv) == 2: # si se reciben dos argumentos 
    numero = int(sys.argv[1]) # convertimos el argumento a entero y escribrimos argv[1] ya que argv[0] es el nombre del script y argv[1] es el argumento
    if numero < 0 or numero > 9999: # si el numero es menos a 0 o mayor a 9999 ya que 9999 es el maximo numero de 4 digitos
        print("Error - Numero incorrecto.")
        print("Ejemplo: descomposicion.py [0-9999]")
    else:
        cadena = str(numero)
        longitud = len(cadena)

        for i in range(longitud):
            print( "{:04d}".format( int(cadena[longitud-1-i]) * 10 ** i )) # imprimimos la cadena en orden inverso con el formato que queremos, tambien con el operador de potencia ** 


else:
    print("Error - Argumentos incorrectos.")
    print("Ejemplo: descomposicion.py 3647")


    len()