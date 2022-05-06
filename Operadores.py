import math


# Area de funciones
def operadores1():
    # Calcular el área de un triángulo.
    print("************************************************************************")
    print("            Programa para calcular el area de un triangulo ")
    print("************************************************************************")
    base = input("Ingrese la base del triangulo:\n")
    altura = input("Ingrese la altura del triangulo:\n")
    areaTriangulo = int(base) * int(altura) / 2
    print("El area de su triangulo es " + str(areaTriangulo))


def operadores2():
    # Ingresar dos números por teclado y sumarlos.
    print("************************************************************************")
    print("                   Programa para sumar dos numeros")
    print("************************************************************************")
    num1 = float(input("Ingrese numero uno:\n"))
    num2 = float(input("Ingrese numero dos:\n"))
    print(f"El resultado de la suma de {num1} + {num2} es " + str(num1 + num2))


def operadores3():
    # Ingresar un número y visualizar el número elevado al cuadrado.
    print("************************************************************************")
    print("             Programa para elevar un numero al cuadrado")
    print("************************************************************************")
    num1 = float(input("Ingrese el numero a elevar al cuadrado:\n"))
    print(f"El resultado de elevar {num1} al cuadrado es " + str(num1 ** 2))


def operadores4():
    # Escribir un algoritmo que convierta de euros a dólares.
    print("************************************************************************")
    print("                 Programa para convertir euros a dolares")
    print("************************************************************************")
    euro = 1.05
    dolares = int(input("Ingresa la cantidad de dolares a coverir a euros:\n"))
    print(f"Sus {dolares} dolares equivalen a " + str(round(dolares / euro, 2)) + " euros")


def operadores5():
    # Escribir un algoritmo que pida el lado de un cuadrado y muestre el valor del área y del perímetro.
    print("******************************************************************************")
    print("        Programa para determinar el area y el perimetro de un cuadrado")
    print("******************************************************************************")
    lado = float(input("Ingrese el valor de un lado de su cuadrado:\n"))
    perimetro = 4 * lado
    area = lado * lado
    print(f"El perimetro de su cuadrado es {perimetro} y el area es {area}")


def operadores6():
    # Escribir un algoritmo que determine el área y el volúmen de un cilindro.
    print("****************************************************************************")
    print("         Programa para determinar el area y el volumen de un cilindro")
    print("****************************************************************************")
    altura = float(input("Ingrese la altura del cilindro:\n"))
    radio = float(input("Ingrese el radio del cilindro:\n"))
    area = (2 * math.pi * radio * altura) + (2 * math.pi * (radio ** 2))
    volumen = math.pi * (radio ** 2) * altura
    print(f"El valor del area de su cilindro es {round(area, 2)} y el volumen es {round(volumen, 2)}")


def operadores7():
    # Realizar un algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma y
    # el área (pi*r)^2 del círculo inscrito.
    print("***********************************************************************************")
    print("       Programa para determinar el area y la longitud de una circunferencia")
    print("***********************************************************************************")
    radio = float(input("Ingrese el valor del radio de su circunferencia:\n"))
    area = math.pi * (radio ** 2)
    longitud = 2 * radio * math.pi
    print(f"El area de su circunferencia es {round(area, 2)} y la longitud es {round(longitud, 2)}")


def operadores8():
    # Calcular el promedio de tres (3) números ingresados por teclado.
    print("************************************************************************")
    print("         Programa para calcular el promedio de tres numeros")
    print("************************************************************************")
    num1 = float(input("Ingrese numero uno:\n"))
    num2 = float(input("Ingrese numero dos:\n"))
    num3 = float(input("Ingrese numero tres:\n"))
    promedio = (num1 + num2 + num3) / 3
    print(f"El promedio de los numeros ingresados es {promedio}")
