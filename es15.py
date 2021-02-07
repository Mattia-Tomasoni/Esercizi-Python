'''
Dato un elenco di nazioni contenuto in una lista e uno delle
rispettive capitali in una seconda lista(nazione e relativa
capitale si trovano nella medesima posizione delle rispettive
liste), visualizza la capitale di una nazione della quale viene
fornito da tastiera il none, segnalando con un messaggio di
errore il caso in cui la nazione richiesta non sia compresa
nell'elenco.
'''

print("ESERCIZIO 15")
print("PROGRAMMA TROVA LA CAPITALE")

nazione = ["Italia", "Inghilterra", "Cina", "Russia", "Stati Uniti", "Australia", "Danimarca", "Germania", "Francia"]
capitale = ["Roma", "Londra", "Pechino", "Mosca", "Washington", "Canberra", "Copenaghen", "Berlino", "Parigi"]

print("Queste sono le nazioni:")

for stato in nazione:
    print(stato)

stato = input("Di quale stato vuoi conoscere la capitale: ")

if stato in nazione:
    print(stato, " ha come capitale", capitale.pop(nazione.index(stato)))

else:
    print("Errore: ", stato, " non è presente")