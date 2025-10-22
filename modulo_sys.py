"""

¿Para qué sirve sys?

En resumen, sys sirve para:

Acceder a argumentos pasados por línea de comandos.

Salir del programa con códigos de salida.

Investigar y modificar la ruta de búsqueda de módulos (sys.path) en tiempo de ejecución.

Leer/escribir en las entradas y salidas estándar (stdin/stdout/stderr).

Obtener información del intérprete (versión, plataforma, byteorder, límites).

Inspeccionar módulos cargados y estados del intérprete (por ejemplo sys.modules, sys.flags).

Controlar límites (p. ej. recursión) y medir tamaños de objetos.


"""

# l3m3nto clave es sys.argv que es una lista en la que se almacenan los argumentos pasados al script desde la línea de comandos.

# import sys
# print(sys.argv)  # Muestra la lista de argumentos pasados al script

# Útil para parsear parámetros sencillos (para casos complejos usa argparse).


# import sys
# sys.path.append('/ruta/a/mis/modulos')
# import mi_modulo_personal



# sys.modules

# Diccionario que mapea nombres de módulos cargados a los objetos módulo. Útil para introspección, recargar o ver qué ya está cargado.

# import sys, math
# # print('math' in sys.modules)  # True

import sys

print(sys.version_info) # Muestra información detallada de la versión de Python
print(sys.platform)     # Muestra la plataforma del sistema operativo
print(sys.byteorder)   # Muestra el orden de bytes (little o big endian)
print(sys.executable)  # Muestra la ruta del ejecutable de Python
print(sys.maxsize)


"""

Scripts CLI: usa sys.argv o mejor argparse para argumentos; sys.exit para indicar éxito/fallo.

Pipes y redirecciones: lee de sys.stdin y escribe en sys.stdout (útil para utilidades que encadenan procesos).

Depuración y diagnósticos: sys.version, sys.executable, sys.platform ayudan a reportar entorno en logs o errores.

Cargar módulos dinámicamente: sys.path + importlib permiten cargar módulos desde rutas no estándar (pero evita hacks; mejor empaquetar).

Testing: redirige sys.stdout/sys.stderr en tests para capturar salidas sin cambiar la lógica.

Ajustes de rendimiento/seguridad: getsizeof para estimar memoria, y setrecursionlimit solo si sabes lo que haces.

Peligros y buenas prácticas

No abuses de sys.path.append en producción: es frágil y puede causar importaciones inesperadas. Prefiere empaquetar/módulos instalables.

No aumentes setrecursionlimit sin control: riesgo de cierre inesperado por falta de memoria.

No uses sys.getrefcount como única prueba de leaks — es una herramienta CPython-específica.

Para IO, si necesitas interoperabilidad con pipelines y bytes, usa los .buffer.

Para comparar versiones, usa sys.version_info y compara tupla en vez de parsear strings.

"""