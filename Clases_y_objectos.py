# PROGRAMACIÓN ORIENTADA A OBJETOS EN PYTHON
# POO

""" 
Este paradigma de POO, nos permote escribir codigo mas organizado, reutilizable y facil de mantener.
Ademas nos permite modelar objetos del mundo real en nuestro codigo, facilitando la comprension y la colaboracion en proyectos de desarrollo de software.


¿ Que es POO?

- la Programacion Orientada a Objetos (POO) es un paradigma de programacion que se basa en el concepto de "objetos", que son instancias de clases que encapsulan datos y comportamientos relacionados.
- Los objectos son entidades que combinan:
  
  - Atributos (datos) = variables que describen las caracteristicas del objeto.
  - metodos (comportamientos) = funciones que definen las acciones que el objeto puede realizar.

  * ejemplo del mundo real:
  un objecto puede ser un "Auto":
    - Atributos: color, marca, modelo, velocidad
    - Metodos: acelerar(), frenar(), girar()


    *** ¿Que es una clase?

    - una clase es el modelo o la plantilla para crear objectos.
    Definen como seran sus atributos y metodos.
    - por ejemplo, la clase "Auto" define los atributos y metodos que tendran todos los autos creados a partir de esa clase.
    - para crear un objecto a partir de una clase, se utiliza la sintaxis de instanciacion:
    - "Auto()"
    mi_auto = Auto()
    - aqui, "mi_auto" es una instancia de la clase "Auto", y puede tener sus propios valores para los atributos definidos en la clase.


    class Auto:
      # atributos y metodos de la clase Auto
      coloir = "Rojo"
      marca = "Toyota"

      # metodos
      def arrancar(self):
            print("El auto ha arrancado")

    ¿Qué es un objeto?
    - un objecto es una instancia concreta de una clase.
    - es decir creado a partir del molde definido por la clase.
    - cuando se crea un objecto a partir de una clase, se dice que se esta instanciando la clase.

    mi_auto = Auto()
    - aqui, "mi_auto" es un objecto de la clase "Auto", y puede tener sus propios valores para los atributos definidos en la clase.
    print(mi_auto.color)  # Accediendo al atributo color del objeto mi_auto
    mi_auto.arrancar()    # Llamando al metodo arrancar del objeto mi_auto




    ***** El método __init__: el constructor ***
     - Cada vez que creas un objeto, Python ejecuta automáticamente el método especial __init__().
    Sirve para inicializar los atributos del objeto.

    class Auto:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Color: {self.color}")

# Crear objetos
auto1 = Auto("Toyota", "rojo")
auto2 = Auto("Mazda", "azul")

auto1.mostrar_info()
auto2.mostrar_info()


- self es una referencia al objeto actual. Permite acceder a los atributos y métodos de la clase dentro de sus propios métodos.
- Es similar a "this" en otros lenguajes de programación. 


**** Atributos de clase vs. atributos de instancia *****

- De clase: ruedas = 4 -> compartido por todos los objectos
- De istancia: this.color = color -> unico para cada objecto

class Auto:
    ruedas = 4  # Atributo de clase

    def __init__(self, color):
        self.color = color  # Atributo de instancia

a1 = Auto("rojo") 
a2 = Auto("azul")

print(a1.ruedas, a2.ruedas)
print(a1.color, a2.color)


# Métodos de instancia, clase y estáticos
-- metodo de istancia: operan sobre instancias de la clase (self) es decir un objecto especifico
def acelerar(self):
    print(f"El auto {self.marca} esta acelerando")

-- metodo de clase: Se asocia a la clase, no al objeto. Usa @classmethod y cls.

class Auto():
    cantidad_autos = 0

    def __init__(self, marca):
        self.marca = marca
        Auto.cantidad_autos += 1


    @classmethod
    def total_autos(cls):
        print(f"Total de autos: {cls.cantidad_autos}")



➤ Método estático

No usa self ni cls.
Se usa para funciones relacionadas con la clase, pero que no dependen de ella.

class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

print(Calculadora.sumar(5, 3))  # 8




"""