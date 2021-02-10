'''
I nomi delle città e i corrispondenti Codici di Avviamento 
Postale(CAP) vengono inseriti da tastiera e memorizzati in un
dizionario, dove il CAP è la chiave. Fornito poi da tastiera 
il nome di una città, costruisci un programma che visualizzi
il suo CAP oppure un messaggio nel caso la città non sia
compresa nell'elenco. 
Analogalmente, fornendo il CAP restituisce il nome della città
oppure un messaggio di errore.
'''

print("ESERCIZIO 28")
print("PROGRAMMA CAP")

cap_e_citta = {}
citta_e_cap = {}

while True:
    citta = input("Qual è la città(fine per finire)? ").upper()#Inserire il nome della città

    if citta == "FINE":
        break

    else:
        cap = input("Quaò è il CAP di " + citta.lower().capitalize() + "? ")#Inserire il suo CAP
        cap_e_citta[cap] = citta#Aggiunta degli elementi al dizionario dove il CAP è la chiave e la città è il valore
        citta_e_cap[citta] = cap#Aggiunta degli elementi al dizionario dove la città è la chiave e il CAP è il valore

    print()

print()

while True:
    scelta = input("Vuoi trovare il CAP o la città(fine per finire)? ").upper()

    if scelta == "CAP":

        while True:
            nome_citta = input(("Qual è il nome della città(fine per finire)? ")).upper()#Inserire il nome della città

            if nome_citta in citta_e_cap:
                print("Il CAP di", nome_citta.lower().capitalize(), "è:", citta_e_cap[nome_citta])

            elif nome_citta == "FINE":
                break

            else:
                print("La città non è presente")

            print()

    elif scelta == "FINE":
        break

    else:

        while True:
            cap = input("Qual è il CAP della città(fine per finire)").upper()#Inserire il CAP

            if cap in cap_e_citta:
                print("La città avente il CAP:", cap, "è:", cap_e_citta[cap].lower().capitalize())

            elif cap == "FINE":
                break
            
            else:
                print("Il CAP non è presente")

            print()

    print()