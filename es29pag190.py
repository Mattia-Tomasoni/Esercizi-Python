'''
ESERCIZIO 29 PAG 190

Nella maggior parte dei sistemi fiscali la tassazione dei
redditi avviene con aliquote progressive(o a scaglioni di
reddito). Considera le seguenti aloquote:
00.000€ < x <= 15.000€ : 23%
15.000€ < x <= 28.000€ : 27%
28.000€ < x <= 55.000€ : 38%
55.000€ < x <= 75.000€ : 41%
75.000€ < x <=    ∞    : 43%
Scrivi un programma che legga un reddito da tastiera e calcoli
l'importo dell'imposta sul reddito e la tassazione media.
Nell'esempio, per un reddito di 45.000€ e un'imposta di
13.420€, la tassazione media è 13.420/45.000*100= 29,82%
Si nota che un reddito di 45.000€ si colloca nella fascia
limitata dal valore di 55.000€ e implica un'imposta di:
6960+(45.000 - 28.000)*38/100.
L'osservazione suggerisce di creare opportune strutture dati
da utilizzare nel calcolo dell'imposta. Per esempio si può
creare un dizionario che associa al limite superiore di ogni
fascia di reddito una tupla con: limite inferiore della fascia,
imposta dovuta per le fasce precedenti, aliquota della fascia.
Per trattare l'ultima fascia si introduce un limite superiore
impossibile da raggiungere, come 10**12(ovverp 1000 miliardi).
Il dizionario si costruisce a programma partendo dagli array:
limiti = [15.000, 28.0000, 55.000, 75.0000, 1000000000000]
aliquota = [23, 27, 38, 41, 43]
'''

from math import inf

limiti = [0, 15000, 28000, 55000, 75000, inf]
tassa = [23/100, 27/100, 38/100, 41/100, 43/100]
costante = [0, 600, 3680, 5330, 6830]

while True:
    reddito = input("Quant'è il reddito(* = fine)? ")

    if reddito == "*":
        break#Interrompe il ciclo

    else:
        reddito = float(reddito)#rende il reddito un float

        if reddito < 0:
            print("Il reddito non può essere inferiore a zero")

        else:

            a = 0#Contatore a
            b = 1#Contatore b

            for n in limiti:#Ciclo for
                if limiti[a] < reddito < limiti[b]:
                    imposta = tassa[a] * reddito - costante[a]#Calcola l'imposta

                a += 1
                b += 1
                c += 1

                if a > 4:
                    a = a - 1
                if b > 5:
                    b = b - 1

            percentuale = imposta/reddito * 100 #Calcola la tassazione media

            print()
            print("Questo è il reddito: " + str(reddito) + "€")#Stampa il testo scritto e il valore del reddito come str
            print("Questa è l'imposta': " + str(round(imposta, 2)) + "€")#Stampa il testo scritto e il valore dell'imposta arrotonadata al centesimo come str
            print("Questa è la tassazione media: " + str(round(percentuale, 2)) + "%")#Stampa il testo scritto e il valore della tassazione media arrotondata al centesimo come str

        print()