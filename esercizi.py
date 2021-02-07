esercizio = input("Scegli un esercizo da 24 a 27: ")
if esercizio == "24":
    print("ESERCIZIO 24")
    print("Programma calcolo percentuale voti")
    candidato1 = input("Chi è il primo candidato? ")
    punti1 = int(input("Quanti sono i voti di " + candidato1 + "? "))
    candidato2 = input("Chi è il secondo candidato? ")
    punti2 = int(input("Quanti sono i voti di " + candidato2 + "? "))
    percentuale1 = (punti1*100)/(punti1+punti2)
    percentuale2 = (punti2*100)/(punti1+punti2)
    print("Questa e la percentuale di", candidato1, ":", percentuale1, "%")
    print("Questa e la percentuale di", candidato2, ":", percentuale2, "%")

#-------------------

elif esercizio == "25":
    print("ESERCIZIO 25")
    candidato1 = input("Chi è il primo candidato? ")
    voti1 = int(input("Quanti voti ha " + candidato1 + "?"))
    candidato2 = input("Chi è il secondo candidato? ")
    voti2 = int(input("Quanti voti ha " + candidato2 + "?"))
    candidati = [candidato1, candidato2]
    candidati.sort()
    print(candidati)
    if voti1 < voti2:
        print(candidato2, candidato1)
    elif voti2 < voti1:
        print(candidato1, candidato2)

#-------------------

elif esercizio == "26":
    print("ESERCIZIO 26")
    print("Programma calcolo media stipendio")
    stipendi = []
    while True:
        stipendio = int(input("Quant'è lo stipendio? "))
        if stipendio == -1:
            break
        else:
            stipendi.append(stipendio)
    totstipendi = len(stipendi)
    sumstipendi = sum(stipendi)
    media = sumstipendi/sumstipendi
    print("Questa è la media degli stipendi dei dipendenti: ", media, "$")

#-------------------

elif esercizio == "27":
    print("ESERCIZIO 27")
    print("Programma calcolo veicoli transitati")
    auto = []
    c = 0
    while True:
        transito = int(input("Quante auto sono transitate oggi? "))
        if transito == 0:
            break
        else:
            c += 1
            auto.append(transito)
    sumauto = sum(auto)
    print("Queste sono le auto transitate in totale: ", sumauto, "in", c, "giorni")