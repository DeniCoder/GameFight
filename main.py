from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self, target):
        """Метод атаки, который уменьшает здоровье цели."""
        pass


class Sword(Weapon):
    def attack(self, target):
        damage = 20  # Урон от меча
        print(f"Воин атаковал монстра мечом, нанесено {damage} урона.")
        target.take_damage(damage)


class Bow(Weapon):
    def attack(self, target):
        damage = 15  # Урон от лука
        print(f"Воин выстрелил в монстра из лука, нанесено {damage} урона.")
        target.take_damage(damage)


class Fighter():
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
        self.health = 100

    def take_damage(self, damage):
        """Уменьшает здоровье бойца на указанное количество урона."""
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"Осталось {self.health} здоровья.")

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon

    def attack(self, target):
        """Атака противника текущим оружием."""
        self.weapon.attack(target)


class Monster():
    def __init__(self, name):
        self.name = name
        self.health = 100

    def take_damage(self, damage):
        """Уменьшает здоровье монстра на указанное количество урона."""
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"Осталось {self.health} здоровья.")

    def attack(self, target):
        """Атака противника."""
        damage = 10  # Урон от монстра
        print(f"Монстр атаковал {target.name}, нанесено {damage} урона.")
        target.take_damage(damage)


# Создаем бойцов
fighter = Fighter("Денис", Sword())
monster = Monster("Монстр Лера")

# Основной цикл боя
while fighter.health > 0 and monster.health > 0:
    monster.attack(fighter)
    fighter.attack(monster)
    fighter.change_weapon(Bow())  # Меняем оружие
    fighter.attack(monster)

# Определяем победителя
if fighter.health > 0 and monster.health <= 0:
    print("Победа! Монстр убит")
elif fighter.health <= 0 and monster.health > 0:
    print("Поражение! Воин убит")