'''
ESERCIZIO 26 PAG 293

Deriva dalla classe Quadrato del Problema 8 una nuova classe 
Rettangolo aggiungendo un secondo lato per l'altezza e 
riscrivendo il metodo per il calcolo del perimetro e dell'area
'''

from math import sqrt

class Quadrato:
    def __init__(self, n_lati, lato):
        self.n_lati = n_lati
        self.lato = lato

    def Perimetro(self):
        perimetro = self.lato * self.n_lati
        return perimetro

    def Area(self):
        area = self.lato ** 2
        return area

    def Info(self):
        print("Il perimetro del quadrato è:", self.Perimetro(), "cm")
        print("L'area del quadrato è:", self.Area(), "cm")  

class Rettangolo(Quadrato):
    def __init__(self, n_lati, lato, altezza):
        super().__init__(n_lati, lato)
        self.altezza = altezza

    def Perimetro(self):
        perimetro = 2 * (self.lato + self.altezza)
        return perimetro

    def Area(self):
        area = self.lato * self.altezza
        return area

    def Info(self):
        print("Il perimetro del rettangolo è:", self.Perimetro(), "cm")
        print("L'area del rettangolo è:", self.Area(), "cm")  

while True:
    scelta = input("Vuoi calcolare perimetro e area(* = fine)? ").upper()

    if scelta == "*":
        break

    else:
        n_lati = int(input("Quanti lati ha? "))
        base = int(input("Quant'è la base? "))
        altezza = int(input("Quant'è l'altezza? "))
        
        if base == altezza:
            figura = Quadrato(n_lati, base)
            figura.Info()

        else:
            figura = Rettangolo(n_lati, base, altezza)
            figura.Info()