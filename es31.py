'''
TESTO:
Fornisci la rappresentazione in binario di un numero decimale. Dopo aver acquisito il valor del Numero
da trasformare, si esegue la divisione del numero per 2 e si calcola quoziente e resto.Il resto è la prima
cifra della rappresentazione binaria ì. Si ripete il rpocedimento assegnando il quoziente ottenuto a
Numero e ricalcolando la divisione per 2; la ripetizione prosegue mentre il quoziente ottenuto si mantiene
diverso da 0. La rappresentazione binaria del numero decimale è costituita dalle cifre binarie
ottenute come resti, lette in ordine inverso.
Confronta poi il risultato con il valore ottenuto dalla funzione predefinita del linguaggio per convertire
un numero decimale in binario.
'''

print("ESERCIZIO 31")
print("Programma conversione decimale-binario")

numero_binario = []
numero_iniziale = int(input("Qual è il numero? "))
numero = numero_iniziale

while True:
    divisione = numero / 2
    meno = divisione - 0.1
    n = round(meno, 0)
    a = int(numero % 2)

    if n == 0:
        numero_binario.append(a)
        break
    else:
        numero_binario.append(a)
        numero = round(meno, 0)

numero_binario.reverse()
print("Questo è il numero decimale:", numero_iniziale)
print("Questo è il numero binario:", numero_binario)