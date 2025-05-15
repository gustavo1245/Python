#gustavo soto
#28-04-25

def divicion_segura():
    try:
        num1 = int(input("ingresa un numero:"))
        num2 = int(input("ingresa otro numero:"))
        resultado = num1 / num2
        print("el resultado de la divicion es:", resultado)
    except ZeroDivisionError:
        print("lo sentimos no se puede realizar esta divicion")
    except ValueError:
        print("Error. solo debes ingresar numeros")
    
divicion_segura()