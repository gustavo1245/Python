#gustavo soto
#15/05/2025

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]


def iterarDiccionario(lista)
    for diccionario in lista:
        print(",".join([f"{key} - {value}" for key, value in diccionario.items()]))

iterarDiccionario (cantantes)