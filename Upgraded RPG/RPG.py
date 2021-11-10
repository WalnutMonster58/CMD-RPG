#Original made on Nov. 3rd, 2021. This ver. made on 11/10/21
#Made by Tyler Siegmund
import random
print("Choose your class")
playerClass = str(input())
enemy = 1
enemyClass = 1
#Player classes
if playerClass == "mage":
    class mage(object):
        """docstring for mage."""

        def __init__(self, damage, health, mana, critChance, defense):

            self.damage = damage
            self.health = health
            self.mana = mana
            self.critChance = critChance
            self.defense = defense
    playerClass = mage(100, 1000, 200, 10, 1)
    print(playerClass.health)

if playerClass == "knight":
    class knight(object):
        """docstring for knight."""

        def __init__(self, damage, health, mana, critChance, defense):
            super(knight, self).__init__()
            self.health = health
            self.damage = damage
            self.mana = mana
            self.critChance = critChance
            self.defense = defense

    playerClass = knight(2500, 200, 50, 25, 1)
    print(playerClass.health)

if playerClass == "thief":
    class thief(object):
        """docstring for thief."""

        def __init__(self, damage, health, mana, critChance, defense):
            super(thief, self).__init__()
            self.health = health
            self.damage = damage
            self.mana = mana
            self.critChance = critChance
            self.defense = defense

    playerClass = thief(300, 50, 100, 50, 1)

#add more classes below



#added classes should go in between here

if enemy == 1:
    class enemyFox(object):
        """docstring for enemyFox."""

        def __init__(self, health, damage, mana, critChance, defense):
            super(enemyFox, self).__init__()
            self.health = health
            self.damage = damage
            self.mana = mana
            self.critChance = critChance
            self.defense = defense

    enemyClass = enemyFox(500, 25, 0, 5, 1)
    print("a wild fox appeared! Very... weak to say the least.")
    print(enemyClass.health)
    print(enemyClass.defense)

#add more enemies below



#added enemies should go in between here


#Not complete. WORK ON NEXT, STUPID!!!!!
while playerClass.health > 0:
    print("So, what will you do?")
    print("atk")
    print("please don't choose guard")
    print("magic")
    playerMove = str(input())
#specifying what each move does
    if playerMove == "guard":
        playerClass.health = 0
        print("I warned you")

    if playerMove == "atk":
        enemyClass.defense = random.randint(0, 100)
        if enemyClass.defense > playerClass.damage:
            playerClass.damage = 0
        playerClass.damage = playerClass.damage - enemyClass.defense
        enemyClass.health = enemyClass.health - playerClass.damage
        print(enemyClass.health)


if playerClass.health <= 0:
    print("You lost. I hope you didn't die to guard!")
