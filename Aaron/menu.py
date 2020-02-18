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
            myBaraja = ET.parse('./XML/myBaraja.xml')
            if(myBaraja.getroot().tag == "PlayerConfig"):
                return 1
            else:
                return 2
        except FileNotFoundError:
            return 0
    elif(sujeto == 1):
        global Enemigo
        try:
            Enemigo = ET.parse('./XML/Enemigo.xml')
            if (myBaraja.getroot().tag == "PlayerConfig"):
                return 1
            else:
                return 2
        except FileNotFoundError:
            return 0

def menu():
    global state
    while True:
        while True:
            if(state == 0):
                print(str("***************************").rjust(100))
                print(str("* 1. Cargar cartas        *").rjust(100))
                print(str("* 2. Carga cartas Enemigo *").rjust(100))
                print(str("***************************").rjust(100))
                #print("99. TEST FUNCTION")
            elif(state == 1):
                print((str("**************************************").rjust(100)))
                print((str("* 1. Cargar cartas                   *").rjust(100)))
                print((str("* 2. Carga cartas Enemigo            *").rjust(100)))
                print(str("* 3. Crear mazo aleatorio            *").rjust(100))
                print(str("* 4. Crear mazo ofensivo             *").rjust(100))
                print(str("* 5. Crear mazo defensivo            *").rjust(100))
                print(str("* 6. Crear mazo equilibrado          *").rjust(100))
                print((str("* 7. Crear mazo aleatorio Enemigo    *").rjust(100)))
                print(str("* 8. Crear mazo ofensivo Enemigo     *").rjust(100))
                print(str("* 9. Crear mazo defensivo Enemigo    *").rjust(100))
                print(str("* 10. Crear mazo equilibrado Enemigo *").rjust(100))
                print(str("* 11. Luchar Jugador vs Jugador      *").rjust(100))
                print(str("* 12. Luchar Jugador vs Bot (arcade) *").rjust(100))
                print(str("* 13. Luchar Jugador vs Bot (liga)   *").rjust(100))
                print(str("**************************************").rjust(100))

            opt = input(str("Selecciona una opcion: ").rjust(100))

            if (state == 0):
                try:
                    opt = int(opt)
                    if (opt < 1 or opt > 2):
                        print(str("Opcion invalida!", end="\n\n").rjust(100))
                    else:
                        break
                except ValueError:
                    print(str("Solo se puede seleccionar opciones numericas!").rjust(100))
            elif (state == 1):
                try:
                    opt = int(opt)
                    if (opt < 1 or opt > 13):
                        print(str("Opcion invalida!", end="\n\n").rjust(100))
                    else:
                        break
                except ValueError:
                    print(str("Solo se puede seleccionar opciones numericas!").rjust(100))

        if(opt == 1):
            print(str("Cargando mi baraja...").rjust(100))
            out = cargar_cartas(0)
            if(out):
                print(str("Mi baraja cargada!").rjust(100), end="\n\n")
                state = 1
            elif (out == 0):
                print(str("ERROR! Archivo no encontrado! (myBaraja.xml)").rjust(100))
            elif (out == 2):
                print(str("ERROR! La raiz del archivo (myBaraja.xml) no coincide!").rjust(100))
        elif(opt == 2):
            print(str("Cargando baraja enemiga...").rjust(100))
            out = cargar_cartas(1)
            if(out):
                print(str("Baraja enemiga cargada!", end="\n\n").rjust(100))
                state = 1
            elif (out == 0):
                print(str("ERROR! Archivo no encontrado! (Enemigo.xml)").rjust(100))
            elif (out == 2):
                print(str("ERROR! La raiz del archivo (Enemigo.xml) no coincide!").rjust(100))

menu()