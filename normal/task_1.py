import random


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor


    def _calculate_damage(self, opponent):
        damage_dealt = self.damage * (1 - opponent.armor / 100)
        return round(damage_dealt, 2)


    def attack(self, opponent):
        damage_dealt = self._calculate_damage(opponent)
        opponent.health -= damage_dealt
        print(f"{self.name} атакует {opponent.name}, нанося {damage_dealt} урона!")
        if opponent.health <= 0:
            print(f"{opponent.name} побеждён!")
        else:
            print(f"У {opponent.name} осталось {opponent.health} здоровья.\n")


class Player(Person):
    def __init__(self, name, health=100, damage=20, armor=10):
        super().__init__(name, health, damage, armor)


class Enemy(Person):
    def __init__(self, name, health=80, damage=15, armor=5):
        super().__init__(name, health, damage, armor)


class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_fight(self):
        print("Бой начинается!")
        turn = random.choice([self.player, self.enemy])
        while self.player.health > 0 and self.enemy.health > 0:
            if turn == self.player:
                self.player.attack(self.enemy)
                turn = self.enemy
            else:
                self.enemy.attack(self.player)
                turn = self.player
        print("Бой завершён!")


player = Player(name="Игрок")
enemy = Enemy(name="Враг")

game = Game(player, enemy)
game.start_fight()
