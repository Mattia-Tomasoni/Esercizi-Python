'''
ESERCIZIO 14 PAG 189

Organizza in una struttura di dati i valori degli occupati
negli ultimi dieci anni. Utilizza un dizionario, assegnand
il ruolo di chiave all'anno. Inserisci i dati da tastiera
e memorizzabili nel contenitore. Calcola poi il valore medio
dei dieci anni e visualizzane il risultato.
'''

from statistics import mean#Dalla libreria statistics importa la funzione mean

dati_occupati = {}
lista_occupati = []

c = 1

while True:
    occupati = input("Quanti sono gli occupati il "+ str(c) + "° anno(* = fine)? ")
    
    if occupati == "*":
        break#Interrompe il ciclo

    else:
        occupati = int(occupati)#Trasforma occupati da str a int
        dati_occupati[str(c) + "° anno"] = occupati#Aggiunge al dizionario una chiave e le assoce il suo valore
        lista_occupati.append(occupati)#Aggiunge occupati a lista_occupati

        c += 1

    print()

print()

print("Questa è la lista di occupati per anno: ")

for e in dati_occupati:
    print(e, ":", dati_occupati[e])

print()

print("Questa è la media di lavoratori annui: ", mean(lista_occupati))