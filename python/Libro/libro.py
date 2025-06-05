#gustavo soto
#26/10/25

class Libro:
#1 pregunta de prueba: inicializa sin inicializar asi: entregandoles los valores por default
    # titulo = "Sin titulo"
    # autor = "desconocido"
    # paginas = 0
    # genero = "indefinido"
    # copias_disponibles = 0

    def __init__(self, titulo, autor, paginas, genero, copias_disponibles):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.genero = genero
        self.copias_disponibles = copias_disponibles

    def atributos(self):
        print(self.titulo, ":", sep="")
        print("*Autor:", self.autor)
        print("*Paginas:", self.paginas)
        print("*Genero:", self.genero)
        print("*Copias disponibles:", self.copias_disponibles)

    def incrementar_copias(self, nuevas_copias):
        self.copias_disponibles = self.copias_disponibles + nuevas_copias
        pass

    def esta_disponible(self):
        return self.copias_disponibles > 0
    
    def agotado(self):
        self.copias_disponibles == 0
        print(self.titulo, "está agotado.")

    def prestar(self, copias=1):
        if self.copias_disponibles >= copias:
            self.copias_disponibles -= copias
            print(f"Se han prestado {copias} copias(s) '{self.titulo}'.")
        else:
            print(f"No hay suficientes copias de '{self.titulo}' para prestar {copias} copias(s).")

#asi es como modificamos el codigo con punto"."


mi_libro = Libro("principito", "Antoine de Saint-Exupéry", 154, "Cuento", 5)

print("\n ====Prestar copias====")   
mi_libro.prestar(2)
mi_libro.atributos()







#2 que sentencia indica que no haga nada de momento: con pass
#3 como entregarle valores a la clase:
#4 como se llama la funcion dentro de una clase:
#5 como ahecedo a los valores de un objeto: con punto "."
#6 que es self:
#7 como creamos el metodo atributos de una clase:
#8 como llamamos al metodo atributos de la clase:
#9 