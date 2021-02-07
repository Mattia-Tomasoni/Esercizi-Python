'''
Le prenotazioni per la partecipazione a un convegno sono
memorizzate secondo l'ordine di arrivo(suggerimento: utilizza
una struttura di coda per memorizzare i dati dei partecipanti).
Scrivi un programma che comprenda due funzionalità:
• l'operazione per registrare i dati dei partecipanti
• l'operazione per visualizzare i nomi dei partecipani a cui
  si deve inviare una lettera di conferma: si tratta dei nomi
  dell'elenco, eliminando quelli ai quali è già stata inviata
  e che sono registrati in un apposito elenco. La funzione 
  che produce l'elenco deve anche aggiornare l'elenco dei 
  partecipanti ai quali è già stata inviata la lettera.
'''
print("ESERCIZIO 34")
print("PROGRAMMA CONFERME PRENOTAZIONI")

prenotazioni = []
conferma_si = []

while True:

    print()

    #Richiesta dei nomi dei partecipanti
    partecipante = input("Come si chiama il partecipante(+ per finire)? ") 

    if partecipante != "+":
        prenotazioni.append(partecipante)
        invito = input("Ha già ricevuto l'invito? ").upper()

        #Filtro per gli inviti
        if invito == "SI":
            conferma_si.append(prenotazioni.pop(prenotazioni.index(partecipante)))

        else:
            pass
    
    else:
        break

#Visualizza le liste
print("Queste sono le persone che hanno già ricevuto la conferma:")
for e in conferma_si:
    print(e.capitalize())

print()

print("Queste sono le persone che non hanno ricevuto la conferma:")  
for e in prenotazioni:
    print(e.capitalize())