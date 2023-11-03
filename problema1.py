def sumar_5_enteros():
    # definicion de variables
    lista = []
    contadorWhile = 0
    tamano = 5
    suma = 0

    # ingresar los numeros
    while contadorWhile < tamano:
        lista.append(int(input("Ingresar numero "+str(contadorWhile+1) +": ")))
        contadorWhile +=1

    # sumamos los numeros
    contadorWhile = 0
    while contadorWhile < tamano:
        suma += lista[contadorWhile]
        contadorWhile +=1

    print("los elementosde la lista son")
    for numero in lista:
        print(numero, end=", ")

    print("\nLa suma de toso sus elementos es:")
    print(suma)

