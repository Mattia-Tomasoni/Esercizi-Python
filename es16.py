'''
Risolvi il problema precedente partendo da due liste generano
un dizionario con la nazione come chiave e la capitale come
valore. Successivamente interroga il dizionario per 
visuallizare la capitale di una nazione.
'''

print("ESERCIZIO 15")
print("PROGRAMMA TROVA LA CAPITALE")

nazioni = ["Italia", "Inghilterra", "Cina", "Russia", "Stati Uniti", "Australia", "Danimarca", "Germania", "Francia"]
capitali = ["Roma", "Londra", "Pechino", "Mosca", "Washington", "Canberra", "Copenaghen", "Berlino", "Parigi"]

stati = {nazioni[a] : capitali[a] for a in range(len(nazioni))}

print("Queste sono le nazioni: ")
for e in stati:
    print(e)

paese = input("Di quale nazione vuoi sapere la capitale: ")

if paese in stati:
    print(paese, " ha come capitale: ", stati[paese])

else:
    print("Errore: ", paese, "non è presente")