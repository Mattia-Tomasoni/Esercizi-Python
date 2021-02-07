'''
Scrivi un programma a cui viene passata una parola e riconosce se si tratta di un
palindromo(parole che si leggono uguali anche al contrario) oppure meno.
'''

print("ESERCIZIO 1")
print("PROGRAMMA PALINDROMO")

parola = input("Qual è la parola? ")
parola_palindroma = parola[::-1]
if parola == parola_palindroma:
    print("La parola", parola, "è palindroma")
else:
    print("la parola", parola, "non è palindroma")
