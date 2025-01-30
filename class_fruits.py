class bombe(fruits):
    def __init__(self, name, color):
        super().__init__(name, "bombe")
        super().__init__(color, "noir")
    def se_couper(self):
        return f"{self.name} se coupe en 2"
        #if couper en 2 alors fin de game

class ice(fruits):
    def __init__(self, name, color):
        super().__init__(name, "glaçon")
        super().__init__(color, "blanc")
    def se_couper(self):
        return f"{self.name} se coupe en 2"
        #if couper en 2 alors freeze du temps pdt 4 secondes 