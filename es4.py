'''
Scrivi un programma che a scelta dell'utente calcoli l'area di un quadrato, rettangolo,
triangolo e cerchio.
'''

print("ESERCIZIO 4")
print("PROGRAMMA CALCOLO AREA")

from math import pi
calcolo = input("Che area vuoi calcolare: quadrato, rettangolo, triangolo, cerchio ")

if calcolo == "quadrato":
    lato = float(input("Quant'è il lato? "))
    area = lato**2
    print("L'area del quadrato è: ", area)

elif calcolo == "rettangolo":
    altezza = float(input("Quant'è l'altezza? "))
    base = float(input("Quant'è la base? "))
    area = altezza*base
    print("L'area del rettangolo è: ", area)

elif calcolo == "triangolo":
    altezza = float(input("Quant'è l'altezza? "))
    base = float(input("Quant'è la base? "))
    area = (altezza*base)/2
    print("L'area del triangolo è: ", area)

elif calcolo == "cerchio":
    raggio = float(input("Quant'è il raggio"))
    area = (raggio**2)*pi
    print("L'area del cerchio è: ", area)