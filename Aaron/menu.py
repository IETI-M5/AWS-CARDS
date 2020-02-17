import xml.etree.ElementTree as ET

state = 0

'''

str(type_tag[0].text).lstrip().rstrip()


def test():

    root = ET.parse('myBaraja.xml')
    result = ''

    for type_tag in root.findall('deck/card'):
        value = type_tag.get('summonPoints')
        print()

        print(type_tag.attrib)
        print("Summon points-> " + str(value))

'''

baraja_local = None
baraja_enemigo = None

def cargar_cartas(sujeto):
    if(sujeto == 0):
        global myBaraja
        try:
            myBaraja = ET.parse('myBaraja.xml')
            return 1
        except FileNotFoundError:
            return 0
    elif(sujeto == 1):
        global Enemigo
        try:
            Enemigo = ET.parse('Enemigo.xml')
            return 1
        except FileNotFoundError:
            return 0

def menu():
    global state
    while True:
        while True:
            if(state == 0):
                print("1. Cargar cartas")
                print("2. Carga cartas Enemigo")
                #print("99. TEST FUNCTION")
            elif(state == 1):
                print("1. Cargar cartas")
                print("2. Carga cartas Enemigo")
                print("3. Crear mazo aleatorio")
                print("4. Crear mazo ofensivo")
                print("5. Crear mazo defensivo")
                print("6. Crear mazo equilibrado")
                print("7. Crear mazo aleatorio Enemigo")
                print("8. Crear mazo ofensivo Enemigo")
                print("9. Crear mazo defensivo Enemigo")
                print("10. Crear mazo equilibrado Enemigo")
                print("11. Luchar Jugador vs Jugador")
                print("12. Luchar Jugador vs Bot (arcade)")
                print("13. Luchar Jugador vs Bot (liga)")

            opt = input("Selecciona una opcion: ")

            if (state == 0):
                try:
                    opt = int(opt)
                    if (opt < 1 or opt > 2):
                        print("Opcion invalida!", end="\n\n")
                    else:
                        break
                except ValueError:
                    print("Solo se puede seleccionar opciones numericas!")
            elif (state == 1):
                try:
                    opt = int(opt)
                    if (opt < 1 or opt > 13):
                        print("Opcion invalida!", end="\n\n")
                    else:
                        break
                except ValueError:
                    print("Solo se puede seleccionar opciones numericas!")

        if(opt == 1):
            print("Cargando mi baraja...")
            if(cargar_cartas(0)):
                print("Mi baraja cargada!", end="\n\n")
                state = 1
            else:
                print("ERROR! Archivo no encontrado! (myBaraja.xml)")
        elif(opt == 2):
            print("Cargando baraja enemiga...")
            if(cargar_cartas(1)):
                print("Baraja enemiga cargada!", end="\n\n")
                state = 1
            else:
                print("ERROR! Archivo no encontrado! (Enemigo.xml)")

menu()