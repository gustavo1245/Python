#gustavo soto
#28-04-25

def mostrar_elemento():
    frutas = ["manzana","banana","naranja","palta"]
    try:
        indice = int(input("elige una posicion (0 a 3):"))
        print("fruta elegida:", frutas[indice])
    except IndexError:
        print("Esta posicion no existe en la lista")
    except ValueError:
        print("Deves ingresar numero")
mostrar_elemento()