# EjerciciosCiclos

def ciclos1():
    # Imprimir todos los múltiplos de 3 que hay entre 1 y 100.
    print("*************************************************************************************")
    print("     Programa para imprimir todos los múltiplos de 3 que hay entre 1 y 100.")
    print("*************************************************************************************")
    input("Presione enter para ejecutar el programa\n")
    contador = 0
    for i in range(1, 101):
        if i % 3 == 0:
            contador += 1
            if contador % 10 != 0:
                print(str(i), end=" ")
            else:
                print(str(i))


def ciclos2():
    # Imprimir los números impares entre 0 y 100.
    print("*************************************************************************************")
    print("         Programa para imprimir todos los numero impares entre 0 y 100")
    print("*************************************************************************************")
    input("Por favor pulse enter para iniciar el programa")
    contador = 0
    for i in range(1, 101):
        if i % 2 != 0:
            contador += 1
            if contador % 10 != 0:
                print(str(i), end=" ")
            else:
                print(str(i))


def ciclos3():
    # Imprimir los números pares del 1 al 100.
    print("*************************************************************************************")
    print("             Programa para mostrar todos los numeros pares de 1 al 100.")
    print("*************************************************************************************")
    input("Por favor pulse enter para iniciar el programa")
    contador = 0
    for i in range(1, 101):
        if i % 2 == 0:
            contador += 1
            if contador % 10 != 0:
                print(str(i), end=" ")
            else:
                print(str(i))


def ciclos4():
    # Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30.
    print("*************************************************************************************")
    print("         Programa para imprimir  los cuadrados de los números del 1 al 30")
    print("*************************************************************************************")
    input("Por favor pulse enter para iniciar el programa")
    for i in range(1, 31):
        potencia = i * i
        print(f"El cuadrado de {i} es {potencia}")


def ciclos5():
    # Escribir un programa que sume los cuadrados de los cien primeros números naturales,
    # mostrando el resultado en pantalla.
    print("*************************************************************************************")
    print("     Programa para sumar los cuadrados de los primeros 100 numeros naturales")
    print("*************************************************************************************")
    input("Presione enter para ejecutar el programa")
    acumulador =0
    for i in range(1, 101):
        potencia=i*i
        acumulador+=potencia
        print(f"El cuadrado de {i} es {potencia} y la suma hasta el momento es de {acumulador}")


def ciclos6():
    # Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los
    # números comprendidos entre ellos en secuencia ascendente.
    print("******************************************************************************************************")
    print("  Programa para generar y mostrar a partir de 2 numeros (el primero debe ser menor al segundo),")
    print("             todos los números comprendidos entre ellos en secuencia ascendente")
    print("******************************************************************************************************")
    numero1 = int(input("Ingrese el primer numero:\n"))
    numero2 = int(input("Ingrese el segundo numero, recuerde que este debe ser menor al anterior:\n"))
    while numero1 > numero2:
        print("El numero ingresado es mayor al primer numero, por favor intentelo nuevamente")
        numero2 = input("Ingrese nuevamente el segundo numero:\n")

    print(f"Los numero comprendidos entre el numero {numero1} y el numero {numero2} son:")
    contador=0
    for i in range(numero1 + 1, numero2):
        contador+=1
        if contador%10!=0:
            print(str(i), end="  ")
        else:
            print(str(i))


def ciclos7():
    # Sumar todos los números que se digitan por teclado mientras no sea cero.
    print("*************************************************************************************")
    print("             Programa para sumar todos los números que se digiten,")
    print("                    el programa termina cuando se digite 0")
    print("*************************************************************************************")
    numero = int(input("Ingrese el primer numero a sumar o 0 para terminar el programa:\n"))
    acumulador = numero
    while numero != 0:
        numero = int(input("Ingrese otro numero para sumar o 0 para terminar el programa:\n"))
        acumulador += numero
        if numero!=0:
            print(f"La suma en este momento es de --> {acumulador} <--")

    print("Programa terminado")

