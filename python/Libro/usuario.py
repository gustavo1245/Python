#gustavo soto
#29/05/25
from tarjeta import TarjetaCredito

class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0
        def agregar_tarjeta(self, tarjeta):
            """Agrega una nueva tarjeta al usuario."""
            self.tarjetas.append(tarjeta)
            print(f"Tarjeta añadida para el usuario {self.nombre}. ahora tiene {len(self.tarjetas)} tarjeta(s).")

    def hacer_comprar(self, monto, indice_tarjeta=0):
        """Realiza una compra en la tarjeta especificada (por indice)."""
        if 0 <= indice_tarjeta < len(self.tarjetas):
            self.tarjetas[indice_tarjeta].pago(monto)
        else:
            print(f"No existe la tarjeta con indice{indice_tarjeta}.")
            return self
    
    def pagar_tarjeta(self, monto, indice_tarjeta=0):
        """Realiza un pago en la tarjeta espeificada (por indice)."""
        if 0 <= indice_tarjeta < len(self.tarjetas):
            self.tarjetas[indice_tarjeta].pago(monto)
        else:
            print(f"No existe la tarjeta con indice {indice_tarjeta}.")
        return self
    
    def mostrar_info_usuario(self):
        """Muestra el saldo de todas las tarjetas del usuario."""
        print(f"saldo de las tarjetas del usuario {self.nombre}:")
        for i, tarjetas in enumerate(self.tarjetas, 1):
            print(f"Tarjeta {i}: Saldo a pagar: ${tarjetas.saldo_pagar:,}")
            return self