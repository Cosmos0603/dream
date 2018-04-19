import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    #player initialization
    def __init__(self):
        self.location = None
        self.items = []
        self.bagsize = 5
        self.curcarry = 0
        #attackPattern: {name: [frequency, damage%, defense%] }
        self.attackPattern = {"normal":[1,0.5,0.5]}

        #player attributes
        self.attributes = {
            'hp':100,
            'mp':100,
            'exp':0,
            'level':1,
            'money':0,
            'strength':10,
            'defend':0,
            'agility':0.3
        }
        #player's weapon
        self.weapon = None
        #player's armor
        self.armor = None
        self.alive = True
        self.fighting = False

    #show status
    def showStatus(self):
        clear()
        print("Player Status:")
        print()
        for key in self.attributes:
            print('{}: {}'.format(key, self.attributes[key]))
        print()
        if self.weapon != None:
            print("Your weapon is: "+ str(self.weapon.name) + ".")
        if self.armor != None:
            print("Your armor is: "+ str(self.armor.name) + ".")
        if len(self.attackPattern) != 1:
            print("Your attack frequency is: " + str(self.attackPattern[str(self.weapon.name)][0]) + ".")
            print("Your damage percentage is: " + str(self.attackPattern[str(self.weapon.name)][1]) + ".")
            print("Your defend percentage is: " + str(self.attackPattern[str(self.weapon.name)][2]) + ".")
        else:
            print("Your attack frequency is: " + str(self.attackPattern['normal'][0]) + ".")
            print("Your damage percentage is: " + str(self.attackPattern['normal'][1]) + ".")
            print("Your defend percentage is: " + str(self.attackPattern['normal'][2]) + ".")
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
        if self.curcarry + item.size <= self.bagsize:
            self.items.append(item)
            self.curcarry = self.curcarry + item.size
            item.loc = self
            self.location.removeItem(item)
            clear()
            print("You have picked up {}".format(item.name))
            print()
            input("Press enter to continue...")
        else:
            clear()
            print("Your bag is full. You can not pick up more items.")
            print("You can drop items to pick up this item.")
            print()
            input("Press enter to continue")

    #drop item
    def drop(self, item):
        self.location.addItem(item)
        item.loc = self.location
        self.items.remove(item)
        self.curcarry = self.curcarry - item.size
        clear()
        print("You have dropped {}".format(item.name))
        print()
        input("Press enter to continue...")

    #equip weapon 
    def equipW(self, weapon):
        self.weapon = weapon
        for k in weapon.usage:
            self.increaseStatus(k,weapon.usage[k])
        self.attackPattern[weapon.name] = weapon.pattern 

    #unequip weapon 
    def unequipW(self, weapon):
        self.weapon = None 
        for k in weapon.usage:
            self.increaseStatus(k,-weapon.usage[k])
        del self.attackPattern[weapon.name]

    #equip armor
    def equipA(self, armor):
        self.armor = armor
        for k in armor.usage:
            self.increaseStatus(k,armor.usage[k])

    #unequip armor 
    def unequipA(self, armor):
        self.armor = None
        for k in armor.usage:
            self.increaseStatus(k,-armor.usage[k])

    #show items in inventory
    def showInventory(self):
        clear()
        print("You can at most carry "+str(self.bagsize)+" size of items.")
        print()
        print("You are currently carrying " + str(self.curcarry) + " size of items:")
        print()
        if len(self.items) == 0:
            print("Nothing!")
            print("Go find something, noob!")
        else:
            itemnames = []
            itemlist = []
            for i in self.items:
                if i.name not in itemnames:
                    itemlist.append([i.name, 1])
                    itemnames.append(i.name)
                else:
                    for k in itemlist:
                        if k[0] == i.name:
                            k[1] = k[1] + 1 
            for j in itemlist:
                print(str(j[0]) + " *" + str(j[1]))
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

