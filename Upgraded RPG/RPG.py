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

        def __init__(self, health, damage, mana, critChance, defense, info, poisoned):
            super(enemyFox, self).__init__()
            self.health = health
            self.damage = damage
            self.mana = mana
            self.critChance = critChance
            self.defense = defense
            self.info = info
            self.poisoned = poisoned

    enemyClass = enemyFox(500, 25, 0, 5, 1, "Fox", 2)
    print("a wild fox appeared! Very... weak to say the least.")


#add more enemies below



#added enemies should go in between here

class afflictions(object):
    """docstring for afflictions."""

    def __init__(self, poison, afflicted, timer, poisoned):
        super(afflictions, self).__init__()
        self.poison = poison
        self.afflicted = afflicted
        self.timer = timer
        self.poisoned = poisoned

affliction = afflictions(100, "false", 1, "false")


#Not complete. WORK ON NEXT, STUPID!!!!!
while playerClass.health > 0:
    if enemyClass.health > 0:
            print("So, what will you do?")
            print("atk")
            print("please don't choose guard")
            print("magic")
            print("kill (test)") #Please do not delete this. Only for testing purposes

            afflictionTimer = 0
            afflictionPoison = 0

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

                if enemyClass.defense > playerClass.damage:
                    playerClass.damage = 0
                    print("wow, you got blocked. Literally!")

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
                break

            #starts magic
            if playerMove == "magic":
                if playerClass.info == "knight":
                    print("Spells: Holy Document (50 mana), healing banner (25 mana), Add more here lol")
                    knightMagic = str(input())
                    print(playerClass.health)
                    #Knight magic starts here. Creates a new variable
                    if knightMagic == "holy document":
                        if playerClass.mana >= 50:
                            enemyClass.health = enemyClass.health - 100
                            print(enemyClass.health)
                            print('The enemy quivers when shown the document written by the lord!')
                        if playerClass.mana <= 50:
                            print("Seems like you don't have enough mana, buster")
                    if knightMagic == "healing banner":
                        if playerClass.mana >= 25:
                            playerClass.health = playerClass.health + 50
                            print("You slammed your sword down and a holy illusion of a banner appeared, healing your wounds!")
                #mage magic starts here
                if playerClass.info == "mage":
                    print("fireball (50 mana), healing spell (50 mana), poison ward (100 mana)")
                    mageMagic = str(input())
                    #creates mage magic
                    if mageMagic == "fireball":
                        if playerClass.mana < 50:
                            print("You do not have enough mana")
                        if playerClass.mana >= 50:
                            enemyClass.health = enemyClass.health - 75
                            print("You hurled a ball of fire at the enemy!")

                    if mageMagic == "poison ward":
                        if playerClass.mana >= 100:
                            print("worked")
                            afflictionTimer = 5
                            afflictionPoison = 1
                            enemyClass.poisoned == 1
                            print("You got the enemy sick!")

                    if afflictionTimer >= 1:
                        print("got here")
                        if afflictionPoison == 1:
                            print("got to 3")
                            enemyClass.health = enemyClass.health - (enemyClass.health * .1)
                            afflictionTimer = afflictionTimer - 1
                            print(enemyClass.health)




                if enemyClass.health < 0:
                    break



if enemyClass.health <= 0:
    print("You win!")

if playerClass.health <= 0:
    print("You lost. I hope you didn't die to guard!")
