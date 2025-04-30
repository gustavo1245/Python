#gustavo soto
#28-04-25
#

def pedir_numero ():
    try:
        numero = int(input("Escribe un numero entero:"))
        print("¡Gracias! tu numero es:", numero)
    except ValueError:
        print("Eso no es un numero valido. Intenta otra vez.")
pedir_numero()