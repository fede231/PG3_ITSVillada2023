class Familia:
    def __init__(self, nombre_papa, nombre_mama, hijos=[]):
        self.nombre_papa = nombre_papa
        self.nombre_mama = nombre_mama
        self.hijos = hijos
    
    def __str__(self):
        hijos_str = ', '.join(self.hijos)
        return f"Papá: {self.nombre_papa}, Mamá: {self.nombre_mama}, Hijos: {hijos_str}"

familia = Familia("Pablo", "Sofia", ["Jacob", "Mateo", "Ismael", "Pepito"])
print(familia)