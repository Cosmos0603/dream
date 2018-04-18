from player import Player
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc, usage,size):
        self.name = name
        self.desc = desc
        self.loc = None
        self.usage = usage
        self.size = size

    def describe(self):
        clear()
        print("This item occupies "+str(self.size)+ " size of the bag." )
        print(self.desc)
        for u in self.usage:
            if self.usage[u] != 0:
                print("usage: increase {} by {}".format(u, self.usage[u]))
        print()
        input("Press enter to continue...")

    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)

class Weapon(Item):
    def __init__(self, name, desc, usage, pattern,size):
        self.name = name
        self.desc = desc
        self.loc = None
        self.usage = usage
        self.pattern = pattern
        self.size = size
    def describe(self):
        clear()
        print("This is a weapon called " + str(self.name) + ".")
        print("It occupies " + str(self.size) + " size of the bag.")
        print(str(self.desc))
        for u in self.usage:
            if self.usage[u] != 0:
                print("usage: increase {} by {}".format(u, self.usage[u]))
        print("It has attack frequency: " + str(self.pattern[0]))
        print("It has damage percentage: " + str(self.pattern[1]))
        print("It has defense percentage: " + str(self.pattern[2]))
        print()
        input("Press enter to continue...")

class Armor(Item):
    def describe(self):
        clear()
        print("This is an armor called "+ str(self.name) + ".")
        print("This item occupies "+str(self.size)+ " size of the bag." )
        print(self.desc)
        for u in self.usage:
            if self.usage[u] != 0:
                print("usage: increase {} by {}".format(u, self.usage[u]))
        print()
        input("Press enter to continue...")
