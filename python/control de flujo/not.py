#gustavo soto
#02-04-25
#tratalero tralala

respuesta = input ('¿estas cansado? (si / no):').strip().lower()

cansado = respuesta == 'si'

if not cansado:
    print('!es hora de programar')
else:
    print('tomate tu time')