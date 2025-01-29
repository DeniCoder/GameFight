from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Воин атакует монстра мечом")

class Bow(Weapon):
    def attack(self):

        print("Воин стреляет в монстра из лука")

class Fighter():
    def __init__(self,name, weapon):
        self.name = name
        self.weapon = weapon
        self.health = 100

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon

class Monster():
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self):
        print("Монстр идет в атаку")

fighter = Fighter("Денис", Sword())
monster = Monster("Монстр Лера")

while fighter.health > 0 and monster.health > 0:
    monster.attack()
    fighter.attack()
    fighter.change_weapon(Bow())
    fighter.attack()

if fighter.health > 0 and monster.health <= 0:
    print("Победа! Монстр убит")
elif fighter.health <= 0 and monster.health > 0:
    print("Поражение! Воин убит")