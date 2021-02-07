'''
TESTO:
Fornisci la rappresentazione in decimale di un numero binario. All'inizio si richiede il numero di cifre
di cui è composto il numero binario(lunghezza); si esegue poi una ripetizione che richiede la cifre del
numero binario una a una a partire da destra e per ciascuna calcola il prodotto della cifra binaria per
la potenza di 2 corrispondente alla posizione della cifra binaria e aggiunge il risultato alla somma; la
ripetizione viene eseguita per il contatore che va dal valore 0 al valore di lunghezza diminuito di 1.
Confronta poi il risultato con il valore ottenuto dalla funzione predefinita del linguaggio per convertire
un numero binario in decimale.
'''

print("ESERCIZIO 30")
print("Programma conversione binario-decimale")

lunghezza_binario = int(input("Quant'è lungo il numero binario? "))
numero_binario = []
numero_decimale = []
a = 0
e = 0

for n in range(1, lunghezza_binario + 1):
    a += 1
    binario = int(input("Qual è la " + str(a) +"ª cifra a partire da destra? "))
    numero_binario.append(binario)
    decimale = binario * 2**(e)
    e += 1
    numero_decimale.append((decimale))

somma_decimale = sum(numero_decimale)
numero_binario.reverse()
print("Questo è il numero binario:", numero_binario)
print("Questo è il numero:", somma_decimale)