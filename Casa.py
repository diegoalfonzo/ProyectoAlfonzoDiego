class Casa:
    def __init__(self,numero,direccion):
        self.numero=numero
        self.direccion=direccion

    def mostrar(self):
        print(f"Numero: {self.numero}\ndireccion: {self.direccion}")