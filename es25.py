'''
I voti assegnati a 30 studenti di una classe in una prova di
italiano sono memorizzati in un dizionario che ha per chiave
la matricola, mentre il valore associato è il voto. Elenca i
risultati in ordine crescente di voto e successivamente
visualizza quali voti diversi tra loro sono stati assegnati,
riducendo a uno i voti uguali.
'''

print("ESERCIZIO 25")
print("PROGRAMMA VOTI")

#Prima parte
nomi_studenti = []
voti_studenti = []
nomi_e_voti = {}

n_studenti = int(input("Quanti sono gli studenti? "))

c = 1

for n in range(n_studenti):

    nome_studente = input("Come si chiama il " + str(c) + "° studente? ")
    voto_studente = int(input("Qual è il voto di " + nome_studente + "? "))
    nomi_studenti.append(nome_studente)
    voti_studenti.append(voto_studente)
    nomi_e_voti[nome_studente] = voto_studente

    c += 1

#Seconda parte
nomi_studenti_crescente = []
voti_studenti_crescente = []

while len(voti_studenti) != 0:
    voti_studenti_crescente.append(min(voti_studenti))
    nomi_studenti_crescente.append(nomi_studenti.pop(voti_studenti.index(min(voti_studenti))))

    for voto in voti_studenti:

        if voto == min(voti_studenti):
            voti_studenti.remove(min(voti_studenti))


studenti = []
voti_e_nomi = {}

for voti in voti_studenti_crescente:

    for studente in nomi_studenti_crescente:

        if nomi_e_voti[studente] == voti:
            studenti.append(studente)

    voti_e_nomi[voti] = studenti

    studenti = []

print("Questi sono i voti e i nomi di chi li ha presi:")
for e in voti_e_nomi:
    print(e, ":", voti_e_nomi[e])