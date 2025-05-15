#gustavo soto
#30-04-25
#9/11

def funcion (a,b, *args, **kwargs):
    print("a=, a")
    print("b=, b")
    for arg in args:
        print("arg=", arg)
    for key , value in kwargs.items():
        print(key, "=", value)

funcion(1,2,14,21,24,36,37,89,78,56, "juanito","pepe","pedrito","el pepe"
        ,"ramon",x="luis",y="sol",c="mexico",)