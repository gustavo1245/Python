#gustavo soto
#28-04-25

#acceder a un valor en un diccionario
#sin que se rompa el programa si la clave no existe

def buscar_canta():
    cantante={
        "nombre":"luis miguel"
        "pais" : "puerto rico"
    }
    try:
        clave = input("¿Que quieres saber? (nombre o pais):")
        print("resultado:", cantante[clave])
    except KeyError:
        print("nou")
buscar_cantante()