'''
Scrivi un programma che data in ingresso una lista A contenente n parole.
restituisca in output una lista B di interi che rappresentano la lunghezza delle parole
contenute in A.
'''

print("ESERCIZIO 2")
print("POGRAMMA CALCOLO LETTERE")

A = []
B = []

while True:
    parola = input("Qual è la parola?, inserisci 0 per finire ")
    if parola == "0":
        break
    else:
        A.append(parola)
        B.append(len(parola))

print("Queste sono le parole: ", A)
print("Queste sono le loro rispettive lunghezze: ", B)