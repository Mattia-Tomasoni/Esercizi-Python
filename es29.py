'''
TESTO:
Dato un elenco di città, con l'indicazione per ciascuna di esse del nome e delle temperature massima e
minima registrate in un giorno, si devono contare quante città hanno superato nel giorno un valore prefissato
per l'escursione termica, ottenuta per differenza tra temperatura massima e minima. Organizza
un programma che, dopo aver richiesto il valore da controllare dell'escursione termica, per ogni città
dell'elenco ripeta la richiesta dei dati(nome, temperatura massima e minima), calcoli l'escursione termica
e controlli se l'escursione è maggiore del valore prefissato: in questo caso, incrementa il contatore
delle città selezionate. Alla fine della ripetizione comunica il numero delle città registrato nel contatore.
'''

print("ESERCIZIO 29")
print("Programma calcolo escursione termica")

città = []
temperatura_massima = []
temperatura_minima = []
escursione_termica = []
numero_città = int(input("Quante città sono? "))
massima = int(input("Qual è l'escursione termica massima? "))
c = 0
 
for n in range(1, numero_città + 1) :
    nome_città = input("Qual è la città? ")
    temp_max = int(input("Qual è la sua temperatura massima? "))
    temp_min = int(input("Qual è la sua temperatura minima? "))
    città.append(nome_città)
    temperatura_massima.append(temp_max)
    temperatura_minima.append(temp_min)
    escursione = temp_max - temp_min
    escursione_termica.append(escursione)

    if escursione > massima:
        c += 1
        print("Questa è la sua escursione termica:", escursione, "°C non va bene")
        print()
    else:
        print("Questa è la sua escursione termica:", escursione, "°C va bene")
        print()

print("Queste sono le città prese in considerazione:", città)
print("Questi sono i valori in gradi centigradi della temperatura massima registrata in ogni città:", temperatura_massima)
print("Questi sono i valori in gradi centigradi della temperatura minima registrata in ogni città:", temperatura_minima)
print("Questi sono i valori in gradi centigradi dell'escursione termica registrata in ogni città:", escursione_termica)
print("Questo è il numero delle città che hanno superato il valore di escursione termica massima: ", c)