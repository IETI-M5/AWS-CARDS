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
            if(Enemigo.getroot().tag == "PlayerConfig"):
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
                print("***************************")
                print("* 1. Cargar cartas        *")
                print("* 2. Carga cartas Enemigo *")
                print("***************************")
            elif(state == 1):
                print("**************************************")
                print("* 1. Cargar cartas                   *")
                print("* 2. Carga cartas Enemigo            *")
                print("* 3. Crear mazo aleatorio            *")
                print("* 4. Crear mazo ofensivo             *")
                print("* 5. Crear mazo defensivo            *")
                print("* 6. Crear mazo equilibrado          *")
                print("* 7. Crear mazo aleatorio Enemigo    *")
                print("* 8. Crear mazo ofensivo Enemigo     *")
                print("* 9. Crear mazo defensivo Enemigo    *")
                print("* 10. Crear mazo equilibrado Enemigo *")
                print("**************************************")

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
                    if (opt < 1 or opt > 10):
                        print("Opcion invalida!", end="\n\n")
                    else:
                        break
                except ValueError:
                    print("Solo se puede seleccionar opciones numericas!")

        if(opt == 1):
            print("Cargando mi baraja...")
            out = cargar_cartas(0)
            if(out):
                print(("Mi baraja cargada!"), end="\n\n")
                state = 1
            elif (out == 0):
                print("ERROR! Archivo no encontrado! (myBaraja.xml)")
            elif (out == 2):
                print("ERROR! La raiz del archivo (myBaraja.xml) no coincide!")
        elif(opt == 2):
            print("Cargando baraja enemiga...")
            out = cargar_cartas(1)
            if(out):
                print("Baraja enemiga cargada!", end="\n\n")
                state = 1
            elif (out == 0):
                print("ERROR! Archivo no encontrado! (Enemigo.xml)")
            elif (out == 2):
                print("ERROR! La raiz del archivo (Enemigo.xml) no coincide!")

menu()