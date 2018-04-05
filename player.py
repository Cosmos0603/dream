import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    #player initialization
    def __init__(self):
        self.location = None
        self.items = []

        #player attributes
        self.attributes = {
            'hp':100,
            'mp':20,
            'exp':0,
            'level':1,
            'money':0,
            'strength':0,
            'defend':0,
            'agility':0
        }

        self.alive = True

    #show status
    def showStatus(self):
        clear()
        print("Player Status:")
        print()
        for key in self.attributes:
            print('{}: {}'.format(key, self.attributes[key]))
        print()
        input("Press enter to continue...")
        
    #modify status to certain value
    def modStatus(self, key, value):
        clear()
        self.attributes[key] = value 
        print('{} is changed to {}'.format(key, self.attributes[key]))
        print()
        input("Press enter to continue...")

    #increase status to certain value
    def increaseStatus(self, key, value):
        clear()
        self.attributes[key] += value
        if value > 0:
            print('{} is increased by {}'.format(key, value))
        elif value < 0:
            print('{} is decreased by {}'.format(key, value))
        else:
            print('{} is not changed'.format(key))
        print()
        input("Press enter to continue...")


    #move player
    def goDirection(self, direction):
        self.location = self.location.getDestination(direction)

    #pickup item
    def pickup(self, item):
        self.items.append(item)
        item.loc = self
        self.location.removeItem(item)
        clear()
        print("You have picked up {}".format(item.name))
        print()
        input("Press enter to continue...")


    #drop item
    def drop(self, item):
        self.location.addItem(item)
        item.loc = self.location
        self.items.remove(item)
        clear()
        print("You have dropped {}".format(item.name))
        print()
        input("Press enter to continue...")

    #show items in inventory
    def showInventory(self):
        clear()
        print("You are currently carrying:")
        print()
        if len(self.items) == 0:
            print("Nothing!")
            print("Go find something, noob!")
        else:
            for i in self.items:
                print(i.name)
        print()
        input("Press enter to continue...")

    #find item in inventory
    def getItemByName(self, name):
        for i in self.items:
            if name.lower() == i.name.lower():
                return i
        return False

    #delete item in inventory
    def deleteItem(self, item):
        self.items.remove(item)

    #attack monster
    def attackMonster(self, mon):
        clear()
        print("You are attacking " + mon.name)
        print()
        print("Your health is " + str(self.attributes['hp']) + ".")
        print(mon.name + "'s health is " + str(mon.health) + ".")
        print()
        if self.attributes['hp'] > mon.health:
            self.attributes['hp'] -= mon.health
            print("You win. Your health is now " + str(self.attributes['hp']) + ".")
            mon.die()
        else:
            print("You lose.")
            self.alive = False
        print()
        input("Press enter to continue...")

