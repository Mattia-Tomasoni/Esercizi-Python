'''
Organizza con un dizionario i dati sui conti correnti bancari
con un numero del conto e saldo. Fornito poi il numero di
conto, il programma visualizza il saldo oppure un messaggio
nel caso in cui il conto non sia presente nella mappa.
'''

print("ESERCIZIO 35")
print("PROGRAMMA CONTI CORRENTI BANCARI")

conti_correnti = {
    "42812" : "147000 €",
    "3002341" : "123000 €",
    "42156" : "53600 €",
    "3312411" : "79910 €",
    "871192" : "237000 €",
    "69221" : "24000 €"
}

numero_conto = input("Qual è il conto: ")

if numero_conto in conti_correnti:
    print("Il saldo del conto: ", numero_conto, " è: ", conti_correnti[numero_conto])

else:
    print("Il conto: ", numero_conto, " non è presente")