import Ciclo
import Condicionales
import Operadores


def menu():
    print("***********************************************************************************************************")
    print("             BIENVENIDO AL PROGRAMA QUE ALMACENA LA MISCELANEA DE EJERCICIOS DE PYTHON")
    print("                                    DESARROLLADO POR: Fabio Garcia")
    print("***********************************************************************************************************")
    print("1. Operadores")
    print("2. Condicionales")
    print("3. Operadores")
    print("99. Salir")
    menu = int(input("Elija la opcion que desea ejecutar\n"))

    # Valida que la opcion sea valida
    while menu < 1 or menu > 3 and menu != 99:
        print("La opcion digitada no es valida, por favor intente nuevamente")
        menu = int(input("Elija la opcion que desea ejecutar\n"))

    if menu == 1:
        submenuOperadores()
    elif menu == 2:
        submenuCondicionales()
    elif menu == 3:
        submenuCiclos()
    elif menu == 99:
        print("Programa terminado")


def submenuOperadores():
    print("***********************************************************************************************")
    print("                                 Menu Operadores")
    print("***********************************************************************************************")
    print("1. Calcular el área de un triángulo.")
    print("2. Ingresar dos números por teclado y sumarlos.")
    print("3. Ingresar un número y visualizar el número elevado al cuadrado.")
    print("4. Escribir un algoritmo que convierta de euros a dólares.")
    print("5. Escribir un algoritmo que pida el lado de un cuadrado y muestre el valor del área y del perímetro.")
    print("6. Escribir un algoritmo que determine el área y el volúmen de un cilindro.")
    print("7 .Realizar un algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma" +
          " y el área (pi*r)^2 del círculo inscrito.")
    print("8. Calcular el promedio de tres (3) números ingresados por teclado.")
    print("9. Atras")

    # Validar que la opción digitada sea correcta
    opcion = int(input("Digite la opcion del programa que quiere ejecutar\n"))
    while opcion < 1 or opcion > 9:
        print("La opcion digitada no es valida, por favor intente nuevamente")
        opcion = int(input("Digite la opcion del programa que quiere ejecutar\n"))

    if opcion == 1:
        Operadores.operadores1()
    elif opcion == 2:
        Operadores.operadores2()
    elif opcion == 3:
        Operadores.operadores3()
    elif opcion == 4:
        Operadores.operadores4()
    elif opcion == 5:
        Operadores.operadores5()
    elif opcion == 6:
        Operadores.operadores6()
    elif opcion == 7:
        Operadores.operadores7()
    elif opcion == 8:
        Operadores.operadores8()
    elif opcion == 9:
        menu()


def submenuCondicionales():
    print("***********************************************************************************************")
    print("                                    Menu Condicionales")
    print("***********************************************************************************************")
    print("1. Escribir un algoritmo para saber si el número ingresado por teclado es positivo o negativo.")
    print("2. Escribir un algoritmo que reciba dos números por teclado y diga cuál es el mayor y cuál el menor.")
    print("3. Escriba un programa que lea tres números enteros positivos y que calcule e imprima en"
          + " pantalla el menor y el mayor de ellos.")
    print("4. Dados dos números A y B, sumarlos si A es menor que B o sino restarlos.")
    print("5. Dados dos números A y B encontrar el cociente entre A y B. Recordar que la división por cero no\n "
          + "está definida, en ese caso debe aparecer una leyenda anunciando que la división no es posible.")
    print(
        "6. Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos.")
    print("7. Escribir un algoritmo que determine si un año es bisiesto o no.")
    print("8. Atras")

    # Validar que la opción digitada sea correcta
    opcion = int(input("Digite la opcion del programa que quiere ejecutar\n"))
    while opcion < 1 or opcion > 8:
        print("La opcion digitada no es valida, por favor intente nuevamente")
        opcion = int(input("Digite la opcion del programa que quiere ejecutar\n"))

    if opcion == 1:
        Condicionales.condicionales1()
    elif opcion == 2:
        Condicionales.condicionales2()
    elif opcion == 3:
        Condicionales.condicionales3()
    elif opcion == 4:
        Condicionales.condicionales4()
    elif opcion == 5:
        Condicionales.condicionales5()
    elif opcion == 6:
        Condicionales.condicionales6()
    elif opcion == 7:
        Condicionales.condicionales7()
    elif opcion == 8:
        menu()


def submenuCiclos():
    print("***********************************************************************************************")
    print("                                 Menu Ciclos")
    print("***********************************************************************************************")
    print("1. Imprimir todos los múltiplos de 3 que hay entre 1 y 100.")
    print("2. Imprimir los números impares entre 0 y 100.")
    print("3. Imprimir los números pares del 1 al 100..")
    print("4. Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30.")
    print("5. Escribir un programa que sume los cuadrados de los cien primeros números naturales, "
          "mostrando el resultado en pantalla..")
    print("6. Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los "
          "números comprendidos entre ellos en secuencia ascendente.")
    print("7 .Sumar todos los números que se digitan por teclado mientras no sea cero.")
    print("8. Atras")

    # Validar que la opción digitada sea correcta
    opcion = int(input("Digite la opcion del programa que quiere ejecutar\n"))
    while opcion < 1 or opcion > 8:
        print("La opcion digitada no es valida, por favor intente nuevamente")
        opcion = int(input("Digite la opcion del programa que quiere ejecutar\n"))

    if opcion == 1:
        Ciclo.ciclos1()
    elif opcion == 2:
        Ciclo.ciclos2()
    elif opcion == 3:
        Ciclo.ciclos3()
    elif opcion == 4:
        Ciclo.ciclos4()
    elif opcion == 5:
        Ciclo.ciclos5()
    elif opcion == 6:
        Ciclo.ciclos6()
    elif opcion == 7:
        Ciclo.ciclos7()
    elif opcion == 8:
        menu()
