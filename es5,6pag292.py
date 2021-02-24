'''
ESERCIZIO 5 PAG 292

Elenca le proprietà e metodi della classe prodotto

ESERCIZIO 6 PAG 292

Definisci il metodo assegna_prezzo della classe prodotto
'''
class Prodotto():
    def __init__(self, name, weight, brand):
        self.name = name
        self.weight = weight
        self.brand = brand

    def assegna_prezzo(self, price):
        self.price = price

    def info(self):
        print("Questp è il prodotto:", self.name)
        print("Questo è il peso:", self.weight, "kg")
        print("Questa è la marca:", self.brand)
        print("Questo è il prezzo:", self.price, "€")

while True:
    choice = input("Vuoi descrivere un prodotto(+ = fine)? ").upper()

    if choice == "+":
        break

    else:
        name = input("Qual è il nome? ")
        weight = input("Quant'è il peso in kg? ")
        brand = input("Quanl è la marca? ")
        price = input("Quant'è il prezzo in €? ")

    product = Prodotto(name, weight, brand)
    product.assegna_prezzo(price)
    product.info()