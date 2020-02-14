a = True
while a != False:
    print("MENU PRINCIPAL")
    print("1) Cargar cartas")
    print("2) Cargar cartas Enemigo")
    print("3) Cargar mazo aleatorio")
    print("4) Cargar mazo ofensivo")
    print("5) Cargar mazo defensivo")
    print("6) Cargar mazo equilibrado")
    print("7) Cargar mazo aleatorio enemigo")
    print("8) Cargar mazo ofensivo enemigo")
    print("9) Cargar mazo defensivo enemigo")
    print("10) Cargar mazo equilibrado enemigo")
    print("11) Luchar Jugador VS Jugador")
    print("12) Luchar Jugador VS Bot (Arcade)")
    print("13) Luchar Jugador VS Bot (liga)")
    try:
        opc = int(input("Que opcion quieres utilizar? "))
    except ValueError:
        print("Opcion invalida, introduce una de las opciones anterior")
        opc = int(input("Que opcion quieres utilizar? "))

    if opc == 1:
        print("Estas en la opción 1")
    elif opc == 2:
        print("Estas en la opción 2")
    elif opc == 3:
        print("Estas en la opción 3")
    elif opc == 4:
        print("Estas en la opción 4")
    elif opc == 5:
        print("Estas en la opción 5")
    elif opc == 6:
        print("Estas en la opción 6")
    elif opc == 7:
        print("Estas en la opción 7")
    elif opc == 8:
        print("Estas en la opción 8")
    elif opc == 9:
        print("Estas en la opción 9")
    elif opc == 10:
        print("Estas en la opción 10")
    elif opc == 11:
        print("Estas en la opción 11")
    elif opc == 12:
        print("Estas en la opción 12")
    elif opc == 13:
        print("Estas en la opción 13")
    else:
        print("Opcion invalida \n")
