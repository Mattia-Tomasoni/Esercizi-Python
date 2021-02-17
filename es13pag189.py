'''
ESERCIZIO 13 PAG 189

Acquisisci da tastiera un elenco di parole, memorizzandole in
una lista, finchè l'utente segnala la fine dell'inserimento
con un asterisco *. Visualizza alla fine il numero delle
parole memorizzate. Ordina alfabeticamente la lista delle
parole e visualizzala, ordinata in modo crescente e decrescente
'''

lista_parole = []

while True:
    parola = input("Inserisci la parola(* = fine): ").lower()
    
    if parola == "*":
        break#Interrompe il ciclo

    else:
        lista_parole.append(parola)#Aggiunge parola a lista_parole

    print()

lista_parole.sort()#Ordina la lista secondo i valori dei caratteri della tabella ASCII

print("Questa è la lista in ordine alfabetico crescente: ")

for e in lista_parole:
    print(e)

print()

print("Questa è la lista in ordine alfabetico decrescente: ")

lista_parole.reverse()#Inverte la lista

for e in lista_parole:
    print(e)