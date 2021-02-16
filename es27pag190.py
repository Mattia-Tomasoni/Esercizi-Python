'''
ESERCIZIO 27 PAG 190

Organizza con un dizionario la rubrica con i nomi delle
persone e i rispettivi numeri telefonici. Fornito poi il nome
della persona, il programma visualizza il suo numero di
telefono oppure un messaggio nel caso la persona non sia
presente nella rubrica.
'''

nomi_e_telefoni = {}

c = 1

while True:
    nome = input("Qual è il nome della " + str(c) + "° persona(fine per finire)? ").upper()#Inserire il nome della persona
    
    if nome == "FINE":
        break#Interrompe il ciclo
    
    else:
        telefono = input("Qual è il numero di telefono di " + nome.lower().capitalize() + "? ")#Inserire il numero di telefono
        nomi_e_telefoni[nome] = telefono #Aggiunta degli elementi al dizionario dove il nome è la chiave e il telefono è il valore
    
    c += 1

    print()

print()

while True:
    trovare_nome = input("Che nome vuoi cercare(fine per finire)? ").upper()#Inserire il nome da trovare
    
    if trovare_nome in nomi_e_telefoni:
        print("Il numero di telefono di", trovare_nome.lower().capitalize(), "è", nomi_e_telefoni[trovare_nome])#Ti stampa oltre a la frase il nome e il suo numero di telefono
        
    elif trovare_nome == "FINE":
        break#Interrompe il ciclo
    
    else:
        print("Il nome non è presente")
        
    print()
