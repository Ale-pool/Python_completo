# Vamos a trabajar con numeros 

a = 10
b = 3

# suma 
print("la suma es : ", a + b)

# resta 
print(f"La resta es :  {a - b}")

# multiplicacion
print(f"La multiplicacion es :  {a * b}")

# division
print(f"La division es :  {a / b}")

# Modulo: es el residuo de la division
print(f"El modulo es :  {a % b}")

# potencia
print(f"La potencia es :  {a ** b}")


# Cuando estamos hablando de numeros, podemos distinguir sobre dos tipos 
    # - enteros : son aquellos que no tienen parte decimal ejm: 10, -10, 0
    # - flotantes : son aquellos que tienen parte decimal : 10.5, -0.5, 3.14

a = - 10.5
b = 3.0
c = -9

print(type(a)) # float
print(type(b)) # float
print(type(c)) # int


# 1 = "hola"  # no se puede inciar una variable con un numero 
# num 2 = 23  # no se puede definir una variable con un espacio
num_2 = 23  # si se puede definir una variable con un guion bajo
print(num_2 * 3 )
print(num_2 ** 2)

# Reutilización 
# Al crear una estructura de cálculos con variables, podemos fácilmente adaptar sus valores para hacer distintas comprobaciones.

nota_1 = 3
nota_2 = 5
nota_media = (nota_1 + nota_2) / 2
print(nota_media)

# para hacer otras operaciones saliendo de la aritmetica basica, se podria utilizar la libreria math, para uso de pi, funciones, raiz entre otras cosa importantes
