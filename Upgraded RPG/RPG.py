#Original made on Nov. 3rd, 2021. This ver. made on 11/10/21
#Made by Tyler Siegmund
import random
print("Choose your class")
playerClass = str(input())
#Player classes
if playerClass == "mage":
    class mage(object):
        """docstring for mage."""

        def __init__(self, damage, health, mana, critChance):

            self.damage = damage
            self.health = health
            self.mana = mana
            self.critChance = critChance
    playerClass = mage(random.randint(1,100), 1000, 200, 10)
    print(playerClass.health)

if playerClass == "knight":
    class knight(object):
        """docstring for knight."""

        def __init__(self, damage, health, mana, critChance):
            super(knight, self).__init__()
            self.health = health
            self.damage = damage
            self.mana = mana
            self.critChance = critChance

    playerClass = knight(2500, random.randint(100,200), 50, 25)
    print(playerClass.health)

#Not complete. WORK ON NEXT, STUPID!!!!!
while playerClass.health > 0:
    print("alive")
