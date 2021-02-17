'''
ESERCIZIO 31 PAG 191

Un'azienda vende prodotti in tutta l'italia e la rete di
vendita è suddivisa in quattro zone: Nord, Centro, Sud e Isole
Dopo aver acquisito in un array il fatturato nelle quattro 
zone, calcola:
• il totale del fatturato;
• i valori in percentuale delle vendite nelle quattro zone
  rispetto al totale
'''

zone = ["Nord", "Centro", "Sud", "Isole"]

fatturati = []

for e in zone:
    soldi = float(input("Quant'è il fatturato della zona " + e +" è? "))
    fatturati.append(soldi)#Aggiunge soldi a fatturati

    print()

print("Questo è il totale del fatturato:" , sum(fatturati), "€")#Ti stamoa il testo e il valore totale del fatturato

print()

c = 0

for n in fatturati:#Ciclo for
  percentuale = float(n*100/sum(fatturati))#Ti calcola le rispettive percentuali per ogni fatturato
  print("La percentuale del fatturato della zona", zone[c],"di:", str(n), "€ è:", str(round(percentuale, 2)), "%")

  print()
    
  c += 1