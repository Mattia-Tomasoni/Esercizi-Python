'''
TESTO:
Dato un elenco di studenti partecipanti a un agara sportiva di lancio del peso (nome studente, lancio),
visualizza il valore del lancio del vincitore(valore massimo).
'''

print("ESERCIZIO 28")
print("Programma calcolo lancio del peso")

partecipanti = []
lanci = []
numero_partecipanti = int(input("Quanti sono i partecipanti?"))
c = 0

for n in range(1, numero_partecipanti + 1):
    c += 1
    nome = input("Chi è il partecipante numero " + str(c) + "? ")
    lancio = int(input("Quant'è il lancio di " + nome + "? "))
    partecipanti.append(nome)
    lanci.append(lancio)
    
print("Questi sono i partecipanti:", partecipanti)
print("Questi sono i rispettivi lanci:", lanci)
print("Questo è il lancio maggiore", max(lanci))