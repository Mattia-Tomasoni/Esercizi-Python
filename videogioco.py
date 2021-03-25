import random

n = 10

def Hp_calc(PotS, IVs, EVs, Lv):
    Hp = (((2 * PotS + IVs + (EVs / 4)) * Lv) / 100) + Lv + 10
    return Hp

def stats_calc(PotS, IVs, EVs, Lv):
    stats = ((((2 * PotS + IVs + (EVs / 4)) * Lv) / 100) + 5)
    return stats

def damage(Lv, Pow, A, D):
    dam = ((((2 * Lv) / 5 + 2) * Pow * (A / D)) / 50 + 2) 
    return dam

def end(HpNemico, HpTuoi):
    if HpNemico <= 0:
        print("Battaglia finita")
        print("Hai vinto")

    elif HpTuoi <= 0:
        print("Battaglia finita")
        print("Hai perso")
    
    else:
        pass

def position(n):
    x = random.randint(0, n - 2)
    return x

def movimento(pokemon, entities_list, field):
    while True:
        direction = input("UP, DOWN, RIGHT, LEFT? ").upper()
        if direction == "UP" or direction == "DOWN" or direction == "RIGHT" or direction == "LEFT":
            last_x = pokemon.x
            last_y = pokemon.y
            pokemon.move(direction)
            pokemon.limits(field, last_x, last_y)
            pokemon.field.draw()

            for e in entities_list[1:]:
                if pokemon.x == e.x - 1 or pokemon.x == e.x + 1 and pokemon.y == e.y - 1 or pokemon.y == e.y + 1:
                    pokemon.fight(e)
                    pokemon.field.draw()
        
        elif direction == "":
            pass
        
        else:
            break

class Entity:
    def __init__(self, x, y, field):
        self.x = x
        self.y = y
        self.field = field
        self.field.entities.append(self)

    def move(self, direction):
            if direction == "DOWN" and self.y > self.field.h - 1:
                self.y += 1

            elif direction == "UP" and self.y > 0:
                self.y -= 1

            elif direction == "RIGHT" and self.x < self.field.w - 1:
                self.x += 1

            elif direction == "LEFT" and self.x > 0:
                self.x -= 1

    def limits(self, field, last_x, last_y):
        for e in field.entities[1:]:
            if e.y == self.y and e.x == self.x:
                self.y = last_y
                self.x = last_x

class Pokemon(Entity):
    def __init__(self, name, x, y, field, Lv, HpB, AtkB, DefB, SpAtkB, SpDefB, SpdB):
        super().__init__(x, y, field)
        self.name = name
        self.HpB = HpB
        self.Lv = Lv
        self.AtkB = AtkB
        self.DefB = DefB
        self.SpAtkB = SpAtkB
        self.SpDefB =SpDefB
        self.SpdB = SpdB

        IVs = {"Hp" : random.randint(0, 31),
               "Atk" : random.randint(0, 31),
               "Def" : random.randint(0, 31),
               "SpAtk" : random.randint(0, 31),
               "SpDef" : random.randint(0, 31),
               "Spd" : random.randint(0, 31)
            }

        self.Hp = Hp_calc(self.HpB, IVs["Hp"], 0, self.Lv)
        self.Atk = stats_calc(self.AtkB, IVs["Atk"], 0, self.Lv)
        self.Def = stats_calc(self.DefB, IVs["Def"], 0, self.Lv)
        self.SpAtk = stats_calc(self.SpAtkB, IVs["SpAtk"], 0, self.Lv)
        self.SpDef = stats_calc(self.SpDefB, IVs["SpDef"], 0, self.Lv)
        self.Spd = stats_calc(self.SpdB, IVs["Spd"], 0, self.Lv)

    def info(self):
        print("Questo è", self.name)
        print("È di livello", self.Lv)
        print("Punti vita", self.Hp)
        print("Attacco", self.Atk)
        print("Difesa", self.Def)
        print("Attacco speciale", self.SpAtk)
        print("Difesa speciale", self.SpDef)
        print("Velocità", self.Spd)

    def fight(self, enemy):
        print("Stai combattendo contro", enemy.name)

        while True:
            if self.Hp > 0 and enemy.Hp > 0:
                choice = input("Attacco fisico o speciale(1, 2)?")

                if choice == "1":
                    attacco = self.Atk
                    difesa = enemy.Def

                elif choice == "2":
                    attacco = self.SpAtk
                    difesa = enemy.SpDef

                choice_2 = random.randint(1, 2)

                if choice_2 == 1:
                    attaco_2 = enemy.Atk
                    difesa_2 = self.Def
                
                elif choice_2 == 2:
                    attaco_2 = enemy.SpAtk
                    difesa_2 = self.SpDef

                if self.Spd > enemy.Spd or self.Spd == enemy.Spd:
                
                    print(self.name, "attacca")
                    enemy.Hp -= damage(self.Lv, 10, attacco, difesa)
                    print("Hp nemici:", enemy.Hp)

                    if enemy.Hp > 0:

                        print(enemy.name, "nemico attacca")
                        self.Hp -= damage(enemy.Lv, 10, attaco_2, difesa_2)
                        print("Hp tuoi:", self.Hp)

                elif self.Spd < enemy.Spd:

                    print(enemy.name, "nemico attacca")
                    print("Hp tuoi:", self.Hp)
                    self.Hp -= damage(self.Lv, 10, attaco_2, difesa_2)

                    if self.Hp > 0:

                        print(self.name, "attacca")
                        enemy.Hp -= damage(enemy.Lv, 10, attacco, difesa)
                        print("Hp nemici:", enemy.Hp)

                end(enemy.Hp, self.Hp)

            else:
                break

class Field:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.entities = []

    def draw(self):
        for y in range(self.h):
            for x in range(self.w):
                for e in self.entities:
                    if y == e.y and x == e.x:
                        print("[X]", end = "")
                        break
                else:
                    print("[ ]", end = "")
            print()
             



field = Field(n, n)
p1 = Pokemon("chamander", n - 1, n - 1, field, 5, 39, 52, 43, 60, 50, 63)
p2 = Pokemon("rattata", position(n), position(n), field, 2, 30, 56, 35, 25, 35, 72)
p3 = Pokemon("pidgey", position(n), position(n), field, 3, 40, 45, 40, 35, 35, 56)
field.draw()

movimento(p1, field.entities, field)