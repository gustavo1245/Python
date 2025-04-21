#gustavo soto
#14-04-25
#

import random

opciones = [
    'no persigas la felicidad, creala'
    'todas las cosas son dificiles antes de ser faciles'
    'el pajaro madrugador '
    'alguien en tu vida necesita una carta de tu parte'
    'no solo pienses actua'
    'tu cosazon se acelera'
    'la fortuna que busca esta en otra galleta'
    'ayuda estoy prisionero en una panaderia china'
]

def fortuna():
    fortuna = random.randint(0, len(opciones)-1)
    print(opciones[fortuna])

fortuna()
fortuna()
fortuna()