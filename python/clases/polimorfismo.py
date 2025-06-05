#gustavo soto
#20/05/25

class Cafe():
    def que_soy(self):
        print("Soy un cafe")

class Te():
    def que_soy(self):
        print("Soy un te")
    
def definir_bebida(bebida):
    bebida.que_soy()

definicion_bebida(Te  ())