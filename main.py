class rueda:
    def __init__(self):
        self.ancho = input("Ancho de la rueda: ")
        self.rodadura = input("Rodadura de la rueda: ")
        self.diametro = input("Diametro de la rueda: ")
        self.presion = 0
    def move_to(self):
        self.presion= input("Presion de la rueda: ")

    def print_info(self):
        print(self.ancho, "/",self.rodadura, "R", self.diametro)
    def print_pressure(self):
        self.pressure= self.presion
        print(self.pressure, "bares")

    def set_pressure(self):
        pass


rueda1 = rueda()
rueda1.set_pressure()
rueda1.print_info()
rueda1.print_pressure()
