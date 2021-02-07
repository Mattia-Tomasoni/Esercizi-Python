'''
Costruisci un dizionario ottenuto da quello dell'esercizio 
precedente invertendo il ruolo di chiave e valore. Usa il
nuovo dizionario per trovare il nome della nazione, noto
il nome della capitale.
'''

print("ESERCIZIO 15")
print("PROGRAMMA TROVA LA nazione")

capitali = ["Roma", "Londra", "Pechino", "Mosca", "Washington", "Canberra", "Copenaghen", "Berlino", "Parigi"]
nazioni = ["Italia", "Inghilterra", "Cina", "Russia", "Stati Uniti", "Australia", "Danimarca", "Germania", "Francia"]

stati = {capitali[a] : nazioni[a] for a in range(len(capitali))}

print("Queste sono le capitali: ")
for e in stati:
    print(e)

capitale = input("Di quale capitale vuoi sapere la nazione: ")

if capitale in stati:
    print(capitale, " è la capitale di: ", stati[capitale])

else:
    print("Errore: ", e, "non è presente")