'''
ESERCIZIO 1 PAG 192

Crea una classe Atleta per rappresentare le informazioni su un
giocatore. La classe deve contenere un attributo booleano
chiamato visitaMedica.

ESERCIZIO 2 PAG 192

Aggiungi alla classe Atleta un metodo per assegnare all'atleta
il nome della squadra dove gioca.

ESERCIZIO 3 PAG 192

Aggiungi alla classe Atleta un metodo chiamato effettua_visita
che ponga l'attributo visitaMedica uguale a True.

ESERCIZIO 4 PAG 192

Aggiungi alla classe Atleta un metodo per visualizzare i dati
del giocatore.
'''

class Atleta:
    def __init__(self, name, age, visitaMedica, team):
        self.name = name
        self.age = age
        self.visitaMedica = visitaMedica
        self.team = team

    def info(self):
        print("Questo è", self.name,)

        print("Ha", self.age, "anni")

        if self.visitaMedica == False:
            print(self.name, "non ha fatto la visita medica")
            
        else:
            print(self.name, "ha già fatto la visita medica")

        print("Gioca nella squadra:", self.team)

    def effettua_visita(self):
        if self.visitaMedica == False:
            choice = input("Vuoi effettuare la visita medica? ").upper()

            if choice == "SI":
                print(self.name, "è andato a fare la visita medica")
                self.visitaMedica = True

                print()

                self.info()

            else:
                print(self.name, "non va a fare la visita medica")

        else:
            print(self.name, "è apposto con la visita medica")

    def main(self):
        self.info()

        print()

        self.effettua_visita()


while True:
    scelta = input("Vuoi identificare un'atleta(+ = fine)? ")

    if scelta == "+":
        break
    
    else:
        name = input("Qual è il suo nome? ")
        age = int(input("Qual è l'età di " + name + "?"))
        visitamedica = input("Ha fatto la visita medica? ").upper()

        if visitamedica == "SI":
            visitamedica = True
        else:
            visitamedica = False

        team = input("Di che team fa parte? ")
        
        a1 = Atleta(name, age, visitamedica, team)
        a1.main()

        print()