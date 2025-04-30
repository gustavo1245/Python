#gustavo soto
#28-04-25

def pedir_numero():
    while True:
        try:
            numero =int(input("Escribe un numero entero:"))
            print("gracias tu numero es:", numero)
            break
        except ValueError:
            print("eso no es un numero valido.")
pedi_numero_repetido()