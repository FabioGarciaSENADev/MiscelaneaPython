# EjerciciosCondicionales
def condicionales1():
    # Escribir un algoritmo para saber si el número ingresado por teclado es positivo o negativo.
    print("******************************************************************************************")
    print("             Programa para saber si un numero es positivo o negativo")
    print("******************************************************************************************")
    num = int(input("Ingrese el numero a comprobar:\n"))
    if num > 0:
        print(f"El numero {num} es positivo")
    elif num == 0:
        print(f"El numero {num} no es ni positivo ni negativo")
    else:
        print(f"El numero {num} es negativo")


def condicionales2():
    # Escribir un algoritmo que reciba dos números por teclado y diga cuál es el mayor y cuál el menor.
    print("******************************************************************************************")
    print("         Programa para saber numero mayor y numero menor entre 2 opciones")
    print("******************************************************************************************")
    num1 = int(input("Ingrese el primer numero:\n"))
    num2 = int(input("Ingrese el segundo numero:\n"))
    if num1 > num2:
        print(f"El primer numero {num1} es mayor al segundo numero {num2}")
    else:
        print(f"El primer numero {num1} es menor al segundo numero {num2}")


def condicionales3():
    # Escriba un programa que lea tres números enteros positivos y que calcule e imprima en
    # pantalla el menor y el mayor de ellos.
    print("******************************************************************************************")
    print("     Programa para saber que numero es mayor y que numero es menor entre 3 opciones")
    print("******************************************************************************************")
    num1 = int(input("Ingrese el primer numero:\n"))
    num2 = int(input("Ingrese el segundo numero:\n"))
    num3 = int(input("Ingrese el tercer numero:\n"))
    if num1>num2 and num1>num3:
        mayor=num1
    elif num2>num1 and num2>num3:
        mayor=num2
    else:
        mayor=num3

    if num1<num2 and num1<num3:
        menor=num1
    elif num2<num1 and num2<num3:
        menor=num2
    else:
        menor=num3

    print(f"De los 3 numeros dados {num1}, {num2} y {num3} el numero mayor es {mayor} y el numero menor es {menor}.")


def condicionales4():
    # Dados dos números A y B, sumarlos si A es menor que B o sino restarlos.
    print("******************************************************************************************")
    print("     Programa para sumar 2 numeros si A es mayor a B, de lo contrario se restaran")
    print("******************************************************************************************")
    num1 = int(input("Ingrese el primer numero o numero A:\n"))
    num2 = int(input("Ingrese el segundo numero o numero B:\n"))
    if num1 < num2:
        print("Como el numero A es menor al numero B los numero fueron sumados y el resultado es " + str(num1 + num2))
    else:
        print("Como el numero A es mayor al numero B los numero fueron restados y el resultado es " + str(num1 - num2))


def condicionales5():
    # Dados dos números A y B encontrar el cociente entre A y B. Recordar que la división por cero
    # no está definida, en ese caso debe aparecer una leyenda anunciando que la división no es posible.
    print("******************************************************************************************")
    print("           Programa para dividir un numero, notifica si se intenta dividir por 0")
    print("******************************************************************************************")
    dividendo=int(input("Ingrese el numero a dividir:\n"))
    divisor=int(input("Ingrese la cantidad por el cual quiere dividir:\n"))
    if divisor==0:
        print("No es posible dividir por 0")
    else:
        resultado= dividendo/divisor
        print(f"El resultado de dividir {dividendo} entre {divisor} es {round(resultado, 2)}")


def condicionales6():
    # Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos.
    print("******************************************************************************************")
    print("    Programa para sumar 2 numeros si uno es negativo, de lo contrario se multiplicaran")
    print("******************************************************************************************")
    num1 = int(input("Ingrese el primer numero:\n"))
    num2 = int(input("Ingrese el segundo numero:\n"))
    if num1 < 0 or num2 < 0:
        print(
            "Uno de los numeros era negativo por lo tanto los numeros se sumaron y el resultado es " + str(num1 + num2))
    else:
        print("Ambos numeros son positivos por lo tanto los numeros se multiplicaron y el resultado es "
              + str(num1 * num2))


def condicionales7():
    # Escribir un algoritmo que determine si un año es bisiesto o no.
    """
       Para saber si un año es bisiesto se deben cumplir estas condiciones:
       1.El año debe ser divisible entre 4
       2.El año no debe ser divisible entre 100
       3.El año debe ser divisible entre 400
       Si 1 y 2 se cumple el año es bisiesto, pero si 2 no se cumple evaluamos 3, si 1 y 3 se cumple el año es bisiesto
       """
    print("******************************************************************************************")
    print("                     Programa para saber si un año es bisiesto")
    print("******************************************************************************************")
    agno = int(input("Ingrese el año a evaluar:\n"))
    if agno % 4 == 0:
        if agno % 100 != 0 or agno % 400 == 0:
            print(f"El año {agno} es bisiesto")
        else:
            print(f"El año {agno} no es bisiesto")
    else:
        print(f"El año {agno} no es bisiesto")



