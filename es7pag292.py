'''
ESERCIZIO 7 PAG 292

Elenca proprietà e metodi della classe motociclo
'''
class Motociclo:
    def __init__(self, motore, n_ruote, ):
        self.motore = motore
        self.n_ruote = n_ruote

class Motocicletta(Motociclo):
    def __init__(self, nome, marca, prezzo, carburante, motore, n_ruote):
        super().__init__(motore, n_ruote)
        self.nome = nome
        self.marca = marca
        self.prezzo = prezzo
        self.carburante = carburante

    def info(self):
        print("Questa è la moto", self.nome, "di", self.marca)
        print("Il prezzo è", self.prezzo, "€")
        print("Ha bisogno di questo carburante:", self.carburante)
        print("Ha", self.n_ruote, "ruote e un motore:", self.motore)


while True:
    scelta = input("Vuoi descrivere una motocicletta(+ = fine)? ").upper()

    if scelta == "+":
        break

    else:
        nome = input("Qual è il nome? ")
        marca = input("Qual è la marca? ")
        prezzo = input("Qual è il prezzo? ")
        carburante = input("Qual è il carburante che utilizza?")
        motore = input("Qual è il motore? ")
        n_ruote = input("Quante ruote ha? ")

        motocicletta = Motocicletta(nome, marca, prezzo, carburante, motore, n_ruote)
        motocicletta.info()