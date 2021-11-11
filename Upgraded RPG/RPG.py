#Original made on Nov. 3rd, 2021. This ver. made on 11/10/21
#Made by Tyler Siegmund
import random
print("Choose your class")
playerClass = str(input())
enemy = 1
enemyClass = 1
dead = 0
#Player classes
if playerClass == "mage":
    class mage(object):
        """docstring for mage."""

        def __init__(self, damage, health, mana, critChance, defense, info):

            self.damage = damage
            self.health = health
            self.mana = mana
            self.critChance = critChance
            self.defense = defense
            self.info = info

    playerClass = mage(100, 1000, 200, 10, 1, "mage")
    print(playerClass.health)

if playerClass == "knight":
    class knight(object):
        """docstring for knight."""

        def __init__(self, damage, health, mana, critChance, defense, info):
            super(knight, self).__init__()
            self.health = health
            self.damage = damage
            self.mana = mana
            self.critChance = critChance
            self.defense = defense
            self.info = info

    playerClass = knight(2500, 200, 50, 25, 1, "knight")
    print(playerClass.health)

if playerClass == "thief":
    class thief(object):
        """docstring for thief."""

        def __init__(self, damage, health, mana, critChance, defense, info):
            super(thief, self).__init__()
            self.health = health
            self.damage = damage
            self.mana = mana
            self.critChance = critChance
            self.defense = defense
            self.info = info

    playerClass = thief(300, 50, 100, 50, 1, "thief")

#add more classes below



#added classes should go in between here

if enemy == 1:
    class enemyFox(object):
        """docstring for enemyFox."""

        def __init__(self, health, damage, mana, critChance, defense, info):
            super(enemyFox, self).__init__()
            self.health = health
            self.damage = damage
            self.mana = mana
            self.critChance = critChance
            self.defense = defense
            self.info = info

    enemyClass = enemyFox(500, 25, 0, 5, 1, "Fox")
    print("a wild fox appeared! Very... weak to say the least.")


#add more enemies below



#added enemies should go in between here


#Not complete. WORK ON NEXT, STUPID!!!!!
    while playerClass.health > 0:
        if enemyClass.health > 0:
            print("So, what will you do?")
            print("atk")
            print("please don't choose guard")
            print("magic")
            print("kill (test)") #Please do not delete this. Only for testing purposes
            print(enemyClass.health )

            playerMove = str(input())
        #specifying what each move does
            if playerMove == "guard":
                playerClass.health = 0
                print("I warned you")

            if playerMove == "atk":
                if playerClass.info == "mage":
                    playerClass.damage = 100
                if playerClass.info == "knight":
                    playerClass.damage = 250
                if playerClass.info == "thief":
                    playerClass.damage = 50
                #add character damages here with character info as the if

                #adding ends here
                crit = random.randint(1,100)
                if enemyClass.info == "Fox":
                    enemyClass.defense = random.randint(0, 10)
                    print("enemy is a fox")
                if enemyClass.defense > playerClass.damage:
                    playerClass.damage = 0
                if playerClass.critChance >= crit:
                    playerClass.damage = playerClass.damage * 10
                    enemyClass.health = enemyClass.health - playerClass.damage
                    print("critical strike!")
                    print(enemyClass.health)
                    print(playerClass.damage)
                if playerClass.critChance < crit:
                    playerClass.damage = playerClass.damage - enemyClass.defense
                    enemyClass.health = enemyClass.health - playerClass.damage
                    print(enemyClass.health)
            if playerMove == "kill":
                enemyClass.health = 0
            

if enemyClass.health <= 0:
    print("You win!")

if playerClass.health <= 0:
    print("You lost. I hope you didn't die to guard!")
