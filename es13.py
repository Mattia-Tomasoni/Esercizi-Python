'''
Verifica se un numero è pari o dispari(un numero è pari quando
il resto della divisione intera per 2 è uguale a 0).
'''

print("PROGRAMMA PARI O DISPARI")
print()

while True:

    n = int(input("Inserisci un numero: "))
    resto = n % 2
    if resto == 0:
        print("Il numero ", n, " è pari")
    elif resto == 1:
        print("Il numero", n, " è dispari")
    
    continua = input("Vuoi continuare? ")
    if continua == "SI" or continua =="Si" or continua == "si":
        print()
    elif continua == "NO" or continua == "No" or continua == "no":
        break