def main():
    print("Valuar Cadenas AFD")
    print("1. __servidor1")
    print("2. 3servidor")
    cadena1 = '__servidor1'
    cadena2 = '3servidor'
    cadena3 = 'servidor3'
    cadena4 = '__s1'
    print("-------------------------------")
    print(str(AFD(cadena1)))
    print(str(AFD(cadena2)))
    print(str(AFD(cadena3)))
    print(str(AFD(cadena4)))

def AFD(cadena):
    estado = 0

    for i in range(len(cadena)):
        if(estado==0):
            if cadena[i] == '_':
                estado = 1
            elif cadena[i].isalpha():
                estado = 2
            else:
                print("cadena invalida")
                return
        elif(estado == 1):
            if (cadena[i] == '_'):
                estado = 1
            elif (cadena[i].isalpha()):
                estado = 3
            else:
                print("cadena invalida")
                return
        elif(estado == 2):
            if (cadena[i].isalpha()):
                estado = 2
            elif (cadena[i].isdigit()):
                estado = 4
            else:
                print("cadena invalida")
                return
        elif (estado == 3):
            if (cadena[i].isdigit()):
                estado = 4
            else:
                print("cadena invalida")
                return
        elif (estado == 4):
            return

    print("cadena valida")

if __name__ == '__main__':
    main()
