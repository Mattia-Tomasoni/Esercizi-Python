'''
In Svezia, i bambini giocano spesso utilizzando un linguaggio un po' particolare detto
"rövarspràket", che significa "linguaggio dei furfanti": consiste nel raddoppiare ogni
consonante di una parola e inserire una "o" nel mezzo. Ad esempio la parola
"mangiare" diventa "momanongogiarore".

Scrivi un programma in grado di tradurre una parola o frase passata tramite input in
"rövarspràket".

Dopo aver tradotto la frase, il programma dovrò chiedere all'utente se intende
tradurne un'altra, e in caso di risposta positiva, dovrà attendere l'inserimento di una
nuova parola da parte dell'utente.
'''

print("ESERCIZIO 3")
print("PROGRAMMA RÖVARSPRÀKET")

vietate = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U", "à", "è", "é", "ì", "ò", "ù", 
";", ",", ":", ".", "?", "!", "'", "'", '"', '"', "(", ")", "/", " "]

while True:
    scelta = input("Vuoi tradurre: Si o No? ")

    if scelta == "Si" or scelta == "SI" or scelta == "si":
        rövarspràket = ""
        parola = input("Qual è la parola/frase? ")

        for lettere in parola:

            if lettere not in vietate:
                rövarspràket = rövarspràket + lettere + "o" + lettere
            else:
                rövarspràket = rövarspràket + lettere

        print("Queste sono le parole/frasi: ", parola)
        print("Queste è la traduzione: ", rövarspràket)
        print()

    elif scelta == "No" or scelta == "NO" or scelta == "no":
        break