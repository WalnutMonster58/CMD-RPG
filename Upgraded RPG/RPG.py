#Original made on Nov. 3rd, 2021. This ver. made on 11/10/21
#Made by Tyler Siegmund
import random
print("Choose your class")
playerClass = str(input())
if playerClass == "mage":
    class MA(object):
        """docstring for mage."""

        def __init__(self, damage, health, mana, critChance):

            self.damage = damage
            self.health = health
            self.mana = mana
            self.critChance = critChance
    mage = MA(random.randint(1,100), 1000, 200, 10)

while playerClass.mage.health > 0:
    print("alive)")
