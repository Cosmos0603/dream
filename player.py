import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    #player initialization
    def __init__(self):
        self.location = None
        self.items = []

        #player attributes
        self.health = 100
        self.mana = 20
        self.exp = 0
        self.level = 1
        self.money = 0
        self.strength = 0
        self.defend = 0
        self.agility = 0

        self.alive = True

    #move player
    def goDirection(self, direction):
        self.location = self.location.getDestination(direction)

    #pickup items
    def pickup(self, item):
        self.items.append(item)
        item.loc = self
        self.location.removeItem(item)

    #show items in inventory
    def showInventory(self):
        clear()
        print("You are currently carrying:")
        print()
        for i in self.items:
            print(i.name)
        print()
        input("Press enter to continue...")

    #attack monster
    def attackMonster(self, mon):
        clear()
        print("You are attacking " + mon.name)
        print()
        print("Your health is " + str(self.health) + ".")
        print(mon.name + "'s health is " + str(mon.health) + ".")
        print()
        if self.health > mon.health:
            self.health -= mon.health
            print("You win. Your health is now " + str(self.health) + ".")
            mon.die()
        else:
            print("You lose.")
            self.alive = False
        print()
        input("Press enter to continue...")

