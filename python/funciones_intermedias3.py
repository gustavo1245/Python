#gustavo soto
# 15/05/2025

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]

def iterarDiccionario2(artista, nac):
    for diccionario in nac:
        if arrtista in diccionario:
            print(diccionario[artista])

#ejemplo de uso

iterarDiccionario2("nombre", cantantes)
iterarDiccionario2("pais", cantantes)