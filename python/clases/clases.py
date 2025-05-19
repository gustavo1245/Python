#gustavo soto
#19/05/2025

#esto ya no sirve por que todo esta dentro del metodo
# class Personaje:
#     nombre = "Default"
#     fuerza = 0
#     inteligencia = 0
#     defensa = 0
#     vida = 0

    def __init__ (self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

        #atributos

    def atributos (self)
        print(self.nombre, ";", sep = "")
        print("fuerza: ", self.fuerza)
        print("inteligencia: ", self.inteligencia)
        print("defensa: ", self.defensa)
        print("vida:", self.vida)

        #subir de nivel

    def subir_nivel (self, fuerza, inteligencia, defensa,):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "Ha muerto")

    def daño (self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = serlf.daño (enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("la vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

    def det_fuerza(self):
        return self.fuerza

    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("Error, la fuerza no puede ser negativa")
        self.fuerza = fuerza

    def Guerero():
        def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
            super()__init__(self, nombre, fuerza, inteligencia, defensa, vida)
            self.espada = espada

        def cambiar_arma(self):
            opcion = int(input("elige un arma: (1) Acero Valiyrio, daño 10. (2) Espada de acero enano, daño 40."))
            if opcion == 1:
                self.espada = 10
                print("Has cambiado tu espada por Acero Valiyrio")
            elif opcion == 2:
                self.espada = 40
                print("Has cambiado tu espada por Espada de acero")
            else:
                print("Opcion no valida")
                self.espada = 0
                print("No has cambiado tu espada")

        def atributos(self):
            super().atributos()
            print("Espada: ", self.espada)

        def daño (self, enemigo):
            return self.fuerza * self.espada - enemigo.defensa
        
        class Mago(Personaje):
            def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
                super().__init__(nombre, fuerza, inteligencia, defensa, vida)
                self.libro = libro
            
            def atributos (self):
                super().atributos()
                print("Libro: ", self.libro)
            
            def daño (self, enemigo):
                return (self.inteligencia * self.libro) - enemigo.defensa


kaldrogo = Guerero("Kaldrogo", 20, 30, 20, 100, 5)
mi_personaje = Personaje("xkiller", 10, 20, 10, 100)
gandalf = Mago("Gandalf", 20, 30, 20, 100, 5)



kaldrogo.atributos()
print("___________________________")
mi_personaje.atributos()
print("___________________________")
gandalf.atributos()
print("___________________________")

mi_personaje.atacar(kaldrogo)
kaldrogo.atacar(mi_personaje)  

kaldrogo.cambiar_arma()
print(kaldrogo.espada)
mi_personaje.atributos()

# print(kaldrogo.esta_vivo)
# kaldrogo.espada()




# mi_enemigo = Personaje("Blaster", 8, 5, 3, 5) 
# mi_personaje.atacar(mi_enemigo)

print(mi_personaje.get_fuerza(-5))




#mi_personaje.morir()
# mi_personaje.fuerza = 0




# mi_personaje.atributos()
# mi_enemigo.atributos()

 # print(mi_personaje.daño(mi_enemigo))




print(mi_personaje.esta_vivo())







# mi_personaje.nombre = "xkiller"
# mi_personaje.fuerza = 40



print(mi_personaje)
print("el nombre del jugador es: ", mi_personaje.nombre)
print("la fuerza del personaje es: ", mi_personaje.fuerza)