'''
Crea un programma che scriva la differenza di due numero a e b se il
loro prodotto è maggiore di 10, oppure la loro somma se il prodotto 
è minore o uguale a 10. Esegui poi il programma con diverse coppie di
valori per a e b: (-5, 2), (5, -5), (10, 2), (-4, -5), (5, 4), (-3, -2)
'''

print("PROGRAMMA a E b")
print()

while True:

    a = int(input("Quant'è a? "))
    b = int(input("Quant'è b? "))
    prodotto = a * b
    print("Questo è il prodotto: ", prodotto)
    if prodotto > 10:
        differenza = a - b
        print("Questa è la differenza: ", differenza)
    elif prodotto <= 10:
        somma = a + b
        print("Questa è la somma: ", somma)

    continua = input("Vuoi continuare? ")
    if continua == "SI" or continua =="Si" or continua == "si":
        print()
    elif continua == "NO" or continua == "No" or continua == "no":
        break