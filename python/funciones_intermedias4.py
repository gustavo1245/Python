#gustavo soto
#15/05/2025

costa_rica = {

   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}

def informacionDiccionario(diccionario):
    for clave, valores in diccionario.items():
        print(f"{len(valores)} {clave.upper()}")
        for valor in valores:
            print(valor)

print("\n Iterar a traves de un diccionario con valores de la lista")    

informacionDiccionario(costa_rica)

#imprime:

# 4 CIUDADES

# San José

# Limón

# Cartago

# Puntarenas

# 5 COMIDAS

# gallo pinto

# casado

# tamales

# chifrijo

# olla de carne