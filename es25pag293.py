'''
ESERCIZIO 25 PAG 293

Crea la classe Triangolo, la classe derivata TriangoloIsocele
e, da quest'ultima, la classe derivata TriangoloEquilatero
'''

from math import sqrt

class Triangolo:
    def __init__(self, lato1, lato2, lato3):
        self.lato1 = lato1
        self.lato2 = lato2
        self.lato3 = lato3

    def Perimetro(self):
        perimetro = self.lato1 + self.lato2 + self.lato3
        return perimetro

    def SemiPerimetro(self):
        semi_perimetro = self.Perimetro() / 2
        return semi_perimetro

    def Area(self):
        area = sqrt(self.SemiPerimetro() * (self.SemiPerimetro() - self.lato1) * (self.SemiPerimetro() - self.lato2) * (self.SemiPerimetro() - self.lato3))
        return area

    def Info(self):
        print("Questo è il perimetro:", self.Perimetro(), "cm")
        print("Questa è l'area:", self.Area(), "cm")

class TriangoloIsoscele(Triangolo):
    def __init__(self, lato1, lato2, lato3):
        super().__init__(lato1, lato2, lato3)

    def Altezza(self):
        if self.lato1 == self.lato2:
            altezza = sqrt(self.lato1 ** 2 - (self.lato3 / 2) ** 2)
            return altezza

        elif self.lato2 == self.lato3:
            altezza = sqrt(self.lato2 ** 2 - (self.lato1 / 2) ** 2)
            return altezza

        elif self.lato1 == self.lato3:
            altezza = sqrt(self.lato1 ** 2 - (self.lato2 / 2) ** 2)
            return altezza

    def Area(self):
        if self.lato1 == self.lato2:
            area = self.Altezza() * self.lato3 / 2
            return area

        elif self.lato2 == self.lato3:
            area = self.Altezza() * self.lato1 / 2
            return area

        elif self.lato1 == self.lato3:
            area = self.Altezza() * self.lato2 / 2
            return area

    def Info(self):
        super().Info()
        
class TriangoloEquilatero(TriangoloIsoscele):
    def __init__(self, lato1, lato2, lato3):
        super().__init__(lato1, lato2, lato3)

    def Altezza(self):
        altezza = sqrt(self.lato1 ** 2 - (self.lato2 / 2) ** 2)
        return altezza
    
    def Area(self):
        area = self.Altezza() * self.lato1 / 2
        return area

    def Info(self):
        super().Info()

while True:
    scelta = input("Vuoi calcolare perimetro e area(* = fine)? ").upper()

    if scelta == "*":
        break

    else:
        lato1 = int(input("Quant'è il primo lato? "))
        lato2 = int(input("Quant'è il secondo lato? "))
        lato3 = int(input("Quant'è il terzo lato? ")) 

        if  lato1 == lato2 and lato2 == lato3 and lato1 == lato3:
            figura = TriangoloEquilatero(lato1, lato2, lato3)
            figura.Info()
        
        elif lato1 == lato2 or lato2 == lato3 or lato1 == lato3:
            figura = TriangoloIsoscele(lato1, lato2, lato3)
            figura.Info()

        else:
            figura = Triangolo(lato1, lato2, lato3)
            figura.Info()