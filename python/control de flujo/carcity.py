#gustavo soto
#02-04-25
#fantasilandia

print("Caja de fantasilandia")

usuario = input('ingresa tu nombre:')
altura = int(input('¿cuanto mides? (cm):'))
creditos =int(input('¿cuantos creditos tienes?:'))

if altura >= 137 and creditos >= 10:
    print ('Disfruta el viaje!')
elif creditos < 10 and altura > 137:
    print('no tienes suficientes creditos')
elif altura < 137 and creditos > 10:
    print('no eres lo suficientemente alto para viajar')
else:
    print('no a cumplido ninguno de los requisitos')