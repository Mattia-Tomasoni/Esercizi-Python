'''
ESERCIZIO 21 PAG 293

Data la classe Motocilco creata nel problema 7, deriva la
classe Ciclomotore. Aggiungi le proprietà opportune e
modifica il metodo che consente di visualizzare i valori
delle proprietà
'''

class Motociclo:
        def __init__(self, nome, marca, prezzo, carburante, motore, n_ruote):
            self.nome = nome
            self.marca = marca
            self.prezzo = prezzo
            self.carburante = carburante
            self.motore = motore
            self.n_ruote = n_ruote

        def info(self):
            print("Questa è la moto", self.nome, "di", self.marca)
            print("Il prezzo è", self.prezzo, "€")
            print("Ha bisogno di questo carburante:", self.carburante)
            print("Ha", self.n_ruote, "ruote e un motore:", self.motore)

class Ciclomotore(Motociclo):
    def __init__(self, nome, marca, prezzo, carburante, motore, n_ruote, modello, velocità_max, cilindrata, freni, anno_uscita):
        super().__init__(nome, marca, prezzo, carburante, motore, n_ruote)
        self.modello = modello
        self.velocità_max = velocità_max
        self.cilindrata = cilindrata
        self.freni = freni
        self.anno_uscita = anno_uscita
    
    def info(self):
        super().info()
        print("Questo è il modello:", self.modello)
        print("Questa è la sua velocità massima:", self.velocità_max, "km/h")
        print("Questa è la cilindrata:", self.cilindrata)
        print("Questi sono i freni:", self.freni)
        print("È uscito nel", self.anno_uscita)

while True:
    scelta = input("Vuoi descrivere un ciclo motore(+ = fine)? ")

    if scelta == "+":
        break

    else:
        nome = input("Qual è il nome? ")
        marca = input("Qual è il marca? ")
        prezzo = input("Quant'è il prezzo? ")
        carburante = input("Che carburante accetta? ")
        motore = input("Qual è il motore? ")
        n_ruote = input("Quante ruote ha? ")
        modello = input("Qual è il modello? ")
        velocità_max = input("Che velocità raggiunge? ")
        cilindrata = input("Qual è la cilindrata? ")
        freni = input("Quali sono i freni? ")
        anno_uscita = input("Quando è uscito? ")
 
        macchina = Ciclomotore(nome, marca, prezzo, carburante, motore, n_ruote, modello, velocità_max, cilindrata, freni, anno_uscita)
        macchina.info()