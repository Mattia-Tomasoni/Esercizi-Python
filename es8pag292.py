'''
ESERCIZIO 8 PAG 292

Crea una classe Quadrato con l'attributo lato e i metodi
per il calcolo del perimetro e dell'area
'''
class Figura:
    def __init(self, n_lati):
        self.n_lati = n_lati

class Quadrato(Figura):
    def __init__(self, n_lati, lato):
        super().__init__(n_lati)
        self.lato = lato

    def Perimetro(self):
        perimetro = self.lato * self.n_lati
        return perimetro

    def Area(self):
        area = self.lato ** 2
        return area

while True:
    scelta = input("Vuoi descrivere un quadrato(+ = fine)? ")

    if scelta == "+":
        break

    else:
        n_lati = int(input("Quanti lati ha? "))
        lato = int(input("Quant'è lungo il lato? "))

        quadrato = Quadrato(n_lati, lato)
        print("Questo è il suo perimetro: ", quadrato.Perimetro(), "cm. Questa è l'area: ", quadrato.Area())
