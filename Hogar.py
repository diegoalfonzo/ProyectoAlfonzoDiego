class Hogar:
    def __init__(self,persona,casa):
        self.persona=persona
        self.casa=casa

    def mostrar(self):
        self.persona.mostrar()
        self.casa.mostrar()
        #print(f"persona: {self.persona}\ncasa: {self.casa}")