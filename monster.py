import random
import updater
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Monster:
    def __init__(self, name, health, pattern, room):
        self.name = name
        self.health = health
        self.room = room
        room.addMonster(self)
        updater.register(self)
        #attackPattern: [name, frequency, damage, defend]
        self.attackPattern = pattern
        self.fighting = False
    def update(self):
        if random.random() < .5:
            self.moveTo(self.room.randomNeighbor())
    def moveTo(self, room):
        self.room.removeMonster(self)
        self.room = room
        room.addMonster(self)
    def die(self):
        self.room.removeMonster(self)
        updater.deregister(self)
    #show monster's status
    def showStatus(self):
        clear()
        print(str(self.name) + " Status: ")
        print()
        print("hp: " + str(self.health))
        print("It has " + str(len(self.attackPattern)) + " attack pattern.")
        print()
        input("Press enter to continue...")