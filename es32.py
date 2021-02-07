'''
Implementa l'algoritmo per il calcolo della soluzione di un'equazione
di un'equazione di primo grado ax+b=0. Il processo risolutivo dipende
dai valori assunti dai coefficienti a e b secondo la tabella che segue
'''

print("PROGRAMMA EQUAZIONE")
print()

while True:
    print("Abbiamo questa equazione ax+b=0")
    a = int(input("Quant'è a? "))
    b = int(input("Quant'è b? "))
    if a == 0 and b == 0:
        print("L'equazione ", a ,"x+", b ,"=0 è indeterminata")
    elif a == 0 and b != 0:
        print("L'equazione ", a ,"x+", b ,"=0 è impossibile")
    elif a != 0 and b == 0:
        print("L'equazione ", a ,"x+", b ,"=0 risulta 0")
    elif a != 0 and b != 0:
        print("L'equazione ", a, "x+", b, "=0 risulta ", -(b/a))

    continua = input("Vuoi continuare? ")
    if continua == "SI" or continua =="Si" or continua == "si":
        print()
    elif continua == "NO" or continua == "No" or continua == "no":
        break