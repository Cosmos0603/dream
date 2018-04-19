from room import Room
from player import Player
from item import Item
from item import Weapon 
from item import Armor
from monster import Monster
import os
import updater
import random
import pickle

#function def

#function to initialize world

Roomlist = []
Weaponlist = []
Armorlist = []
Itemlist = []
Monsterlist = []

#setup world

def createWorld():

    #set up rooms
    hall1 = Room("hall1","This is level 1. You are in Hallway",1,False)
    a1 = Room("a1","This is level 1. You are in room 1",1,False)
    b1 = Room("b1","This is level 1. You are in room 2",1,False)
    c1 = Room("c1","This is level 1. You are in room 3",1,False)
    d1 = Room("d1","This is level 1. You are in room 4",1,True)
    e1 = Room("e1","This is level 1. You are in room 5",1,False)
    Room.connectRooms(a1, "hall1", hall1, "a1")
    Room.connectRooms(b1, "hall1", hall1, "b1")
    Room.connectRooms(c1, "hall1", hall1, "c1")
    Room.connectRooms(d1, "hall1", hall1, "d1")
    Room.connectRooms(e1, "hall1", hall1, "e1")
    hall2 = Room("hall2","This is level 2. You are in Hallway",2,False)
    a2 = Room("a2","This is level 2. You are in room 1",2,False)
    b2 = Room("b2","This is level 2. You are in room 2",2,True)
    c2 = Room("c2","This is level 2. You are in room 3",2,False)
    d2 = Room("d2","This is level 2. You are in room 4",2,False)
    e2 = Room("e2","This is level 2. You are in room 5",2,False)
    Room.connectRooms(a2, "hall2", hall2, "a2")
    Room.connectRooms(b2, "hall2", hall2, "b2")
    Room.connectRooms(c2, "hall2", hall2, "c2")
    Room.connectRooms(d2, "hall2", hall2, "d2")
    Room.connectRooms(e2, "hall2", hall2, "e2")
    hall3 = Room("hall3","This is level 3. You are in Hallway",3,False)
    a3 = Room("a3","This is level 3. You are in room 1",3,False)
    b3 = Room("b3","This is level 3. You are in room 2",3,False)
    c3 = Room("c3","This is level 3. You are in room 3",3,False)
    d3 = Room("d3","This is level 3. You are in room 4",3,False)
    e3 = Room("e3","This is level 3. You are in room 5",3,True)
    Room.connectRooms(a3, "hall3", hall3, "a3")
    Room.connectRooms(b3, "hall3", hall3, "b3")
    Room.connectRooms(c3, "hall3", hall3, "c3")
    Room.connectRooms(d3, "hall3", hall3, "d3")
    Room.connectRooms(e3, "hall3", hall3, "e3")
    hall4 = Room("hall4","This is level 4. You are in Hallway",4,False)
    a4 = Room("a4","This is level 4. You are in room 1",4,True)
    b4 = Room("b4","This is level 4. You are in room 2",4,False)
    c4 = Room("c4","This is level 4. You are in room 3",4,False)
    d4 = Room("d4","This is level 4. You are in room 4",4,False)
    e4 = Room("e4","This is level 4. You are in room 5",4,False)
    Room.connectRooms(a4, "hall4", hall4, "a4")
    Room.connectRooms(b4, "hall4", hall4, "b4")
    Room.connectRooms(c4, "hall4", hall4, "c4")
    Room.connectRooms(d4, "hall4", hall4, "d4")
    Room.connectRooms(e4, "hall4", hall4, "e4")
    hall5 = Room("hall5","This is level 5. You are in Hallway",5,False)
    a5 = Room("a5","This is level 5. You are in room 1",5,False)
    b5 = Room("b5","This is level 5. You are in room 2",5,False)
    c5 = Room("c5","This is level 5. You are in room 3",5,False)
    d5 = Room("d5","This is level 5. You are in room 4",5,False)
    e5 = Room("e5","This is level 5. You are in room 5",5,False)
    Room.connectRooms(a5, "hall5", hall5, "a5")
    Room.connectRooms(b5, "hall5", hall5, "b5")
    Room.connectRooms(c5, "hall5", hall5, "c5")
    Room.connectRooms(d5, "hall5", hall5, "d5")
    Room.connectRooms(e5, "hall5", hall5, "e5")
    Roomlist.append(hall1)
    Roomlist.append(hall2)
    Roomlist.append(hall3)
    Roomlist.append(hall4)
    Roomlist.append(hall5)
    Roomlist.append(a1)
    Roomlist.append(b1)
    Roomlist.append(c1)
    Roomlist.append(d1)
    Roomlist.append(e1)
    Roomlist.append(a2)
    Roomlist.append(b2)
    Roomlist.append(c2)
    Roomlist.append(d2)
    Roomlist.append(e2)
    Roomlist.append(a3)
    Roomlist.append(b3)
    Roomlist.append(c3)
    Roomlist.append(d3)
    Roomlist.append(e3)
    Roomlist.append(a4)
    Roomlist.append(b4)
    Roomlist.append(c4)
    Roomlist.append(d4)
    Roomlist.append(e4)
    Roomlist.append(a5)
    Roomlist.append(b5)
    Roomlist.append(c5)
    Roomlist.append(d5)
    Roomlist.append(e5)

    

    #set up items
    Rock = Item("Rock", "This is just a rock.", {}, 1, False)
    Rock.putInRoom(b1)
    Itemlist.append(Rock)

    Bandage = Item("Bandage", "This is a Bandage that can increase hp.", {'hp': 10}, 1, True)
    Bandage.putInRoom(c1)
    Itemlist.append(Bandage)

    Bandage = Item("Bandage", "This is a Bandage that can increase hp.", {'hp': 10}, 1, True)
    Bandage.putInRoom(c1)
    Itemlist.append(Bandage)

    Bandage = Item("Bandage", "This is a Bandage that can increase hp.", {'hp': 10}, 1, True)
    Bandage.putInRoom(c1)
    Itemlist.append(Bandage)

    Bandage1 = Item("Bandage1", "This is a Bandage that can increase hp.", {'hp': 10}, 1, True)
    Bandage1.putInRoom(c1)
    Itemlist.append(Bandage1)

    Bandage2 = Item("Bandage2", "This is a Bandage that can increase hp.", {'hp': 10}, 1, True)
    Bandage2.putInRoom(c1)
    Itemlist.append(Bandage2)

    Bandage3 = Item("Bandage3", "This is a Bandage that can increase hp.", {'hp': 10}, 1, True)
    Bandage3.putInRoom(c1)
    Itemlist.append(Bandage3)

    Bandage4 = Item("Bandage4", "This is a Bandage that can increase hp.", {'hp': 10}, 1, True)
    Bandage4.putInRoom(c1)
    Itemlist.append(Bandage4)

    Bandage5 = Item("Bandage5", "This is a Bandage that can increase hp.", {'hp': 10}, 1, True)
    Bandage5.putInRoom(c1)
    Itemlist.append(Bandage5)

    Crowbar = Weapon("Crowbar", "Common Tool.", {'strength': 3}, [1, 0.60, 0.60], 1, True)
    Crowbar.putInRoom(a1)
    Weaponlist.append(Crowbar)

    lilyshield = Armor("lilyshield","This is a shield made by Lily, the maker of the game.", {'defend': 10, 'strength': -2, 'agility':-0.05}, 2, True)
    lilyshield.putInRoom(a1)
    Armorlist.append(lilyshield)

    #set up player's location
    player.location = hall1

    #set up monsters
    Bob = Monster("Bob the monster", 20, {"normal":[3 ,5, 2], "flying":[1, 10, 8]}, b1)
    Monsterlist.append(Bob)

#function to clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#function to print current situation info
def printSituation():
    clear()
    print(player.location.desc)
    print()

    #monster info
    if player.location.hasMonsters():
        print("This room contains the following monsters:")
        for m in player.location.monsters:
            print(m.name)
        print()

    #item info
    if player.location.hasItems():
        print("This room contains the following items:")
        itemnames = []
        itemlist = []
        for i in player.location.items:
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

    #exit info
    print("You can go in the following directions:")
    for e in player.location.exitNames():
        print(e)
    print()
    #show help
    print("enter 'help' to get more information")
    print()

#function to print current fight info
def printfight():
    clear()
    player.showStatus()
    for k in player.location.monsters:
        k.showStatus()

    

#helper function
def showHelp():
    clear()
    print("Info: ")
    print("me -- show your current status")
    print("inventory -- show items in your inventory")
    print("inspect <item_name> -- inspect given item in current room")
    print("iteminfo <item_name> -- check info of given item in your inventory")

    print()
    print("Movement: ")
    print("go <place_name> -- moves you to the given place")
    print("teleport -- moves you to the upper level")

    print()
    print("Item: ")
    print("pickup <item_name> -- pick up the item")
    print("drop <item_name> -- drop item in your inventory")
    print("use <item_name> -- use item in your inventory")
    print("equip/unequip <item_name> -- equip/unequip a weapon or armor in your inventory")

    print()
    print("Monster: ")
    print("fight <monster_name> -- enter the fighting mode with a certain monster")
    print("fight mode: ")
    print("attack -- attack the monster")
    print("useitem -- check inventory and choose a usable item to use in a fight")
    print("escape -- escape from the fight")

    print()
    print("Gameplay: ")
    print("exit -- quit the game")
    print("save -- save the game")

    print()
    input("Press enter to continue...")

def getthingByName(name, L):
        for i in L:
            if i.name.lower() == name.lower():
                return i
        return False



#function def end

#game start

#title
print("????\n??  ??\n??    ??\n??     ??    ??    ??    ????????    ????????      ??????????\n??     ??    ??  ??      ??    ??    ??    ??      ??  ??  ??\n??    ??     ????        ????????    ??    ??      ??  ??  ??\n??  ??       ??          ??          ??    ??      ??  ??  ??\n????         ??          ????????    ????????      ??  ??  ??\n                                            ???")
print()
print("Press 'new' to start a new game")
print("Press 'load' to load your last game")
setting = input("... ")
#create a player
if setting == 'new':
    player = Player()
#create the world
    createWorld()
    clear()
    print("You wake up at the basement of a tower. We call it level 1.")
    print("Suddenly, you realize it's a dream.")
    input("...")
    print("Even worse, you cannot wake yourself up in reality.")
    input("...")
    print("You must find a way to get out of here.")
    input("...")
    print("Good luck. Dreamer.")
    input("...")
if setting == 'load':

#load game
    Rooms = open("Rooms.pickle","rb")
    Roomlist = pickle.load(Rooms)
    Weapons = open("Weapons.pickle","rb")
    Weaponlist = pickle.load(Weapons)
    Armors = open("Armors.pickle","rb")
    Armorlist = pickle.load(Armors)
    Items = open("Items.pickle","rb")
    Itemlist = pickle.load(Items)
    Players = open("Players.pickle","rb")
    player = pickle.load(Players)
    Monsters = open("Monsters.pickle","rb")
    Monsterlist = pickle.load(Monsters)

playing = True
while playing and player.alive:

    #show current situation info
    printSituation()

    #control variables initialization
    commandSuccess = False
    timePasses = False

    #ask for player command
    while not commandSuccess:
        commandSuccess = True
        command = input("What now? ")
        commandWords = command.split()  #split the commandWords into pieces by space

        #"go <place_name>" --go to certain place
        if commandWords[0].lower() == "go":   #cannot handle multi-word directions
            player.goDirection(commandWords[1]) 
            timePasses = True
        #"teleport" --tranverse to the upper layer
        elif commandWords[0].lower() == "teleport":
            checking = player.location.isPortal
            if checking != False:
                print("A huge cyclone appears and you are blowed up to the sky~")
                input("Press enter to tranverse!")
                destName = "hall" + str(player.location.layer + 1)
                dest = getthingByName(destName, Roomlist)
                player.location = dest
                print()
                print("Welcome to level "+str(player.location.layer))
                print("The mosters are more challenging here. Be careful.")
                input("Press enter to continue...")
                print()
                timePasses = True
            else:
                clear()
                print("This room has no Portal. You can only teleport in a Portal room.")
                input("Press enter to continue...")

        #"me" --show player status
        elif commandWords[0].lower() == "me":
            player.showStatus()
        
        #"inspect <item_name>"
        elif commandWords[0].lower() == "inspect":
            targetName = command[8:]
            target = player.location.getItemByName(targetName)
            if target != False:
                target.describe()
            else:
                print("No such item.")
                commandSuccess = False

        #"pickup <item_name>" --pickup items
        elif commandWords[0].lower() == "pickup":  #can handle multi-word objects
            targetName = command[7:]
            target = player.location.getItemByName(targetName)
            if target != False:
                player.pickup(target)
            else:
                print("No such item.")
                commandSuccess = False

        #"drop <item_name>" --drop items
        elif commandWords[0].lower() == "drop":
            itemName = command[5:]
            item = player.getItemByName(itemName)
            if item != False:
                player.drop(item)
            else:
                print("No such item.")
                commandSuccess = False

        #"inventory" --show inventory
        elif commandWords[0].lower() == "inventory":
            player.showInventory()        

        #"iteminfo <item_name>" --show info of certain item in inventory
        elif commandWords[0].lower() == "iteminfo":
            itemName = command[9:]
            item = player.getItemByName(itemName)
            if item != False:
                item.describe()
            else:
                print("No such item.")
                commandSuccess = False
            
        #"use <item_name>" --use item
        elif commandWords[0].lower() == "use":
            itemName = command[4:]
            item = player.getItemByName(itemName)
            if item != False:
                for u in item.usage:
                    if item.usage[u] != 0:
                        player.increaseStatus(u, item.usage[u])
                player.deleteItem(item)
            else:
                print("No such item.")
                commandSuccess = False

        #"equip <item_name>" --equip weapon or armor 
        elif commandWords[0].lower() == "equip":
            itemName = command[6:]
            item = player.getItemByName(itemName)
            if type(item) == Weapon:
                if player.weapon == None:
                    player.equipW(item)
                else:
                    print("You have another weapon equipped.")
                    print("Please first unequip before equip a new weapon.")
                    commandSuccess = False
            elif type(item) == Armor:
                if player.armor == None:
                    player.equipA(item)
                else:
                    print("You have another armor equipped.")
                    print("Please first unequip before equip a new armor.")
                    commandSuccess = False
            else:
                print("No such item.")
                commandSuccess = False

        #"unequip <item_name>" --unequip weapon or armor 
        elif commandWords[0].lower() == "unequip":
            itemName = command[8:]
            item = player.getItemByName(itemName)
            if type(item) == Weapon:
                if player.weapon != None:
                    player.unequipW(item)
                else:
                    print("You equip nothing!")
                    commandSuccess = False
            elif type(item) == Armor:
                if player.armor != None:
                    player.unequipA(item)
                else:
                    print("You equip nothing!")
                    commandSuccess = False
            else:
                print("No such item.")
                commandSuccess = False

        #"help" --show commands instruction
        elif commandWords[0].lower() == "help":
            showHelp()

        #"exit" --exit game
        elif commandWords[0].lower() == "exit":
            playing = False

        #'save' --save game
        elif commandWords[0].lower() == "save":
            Rooms = open("Rooms.pickle","wb")
            pickle.dump(Roomlist, Rooms)
            Rooms.close()
            Weapons = open("Weapons.pickle","wb")
            pickle.dump(Weaponlist, Weapons)
            Weapons.close()
            Armors = open("Armors.pickle","wb")
            pickle.dump(Armorlist, Armors)
            Armors.close()
            Items = open("Items.pickle","wb")
            pickle.dump(Itemlist, Items)
            Items.close()
            Players = open("Players.pickle","wb")
            pickle.dump(player, Players)
            Players.close()
            Monsters = open("Monsters.pickle","wb")
            pickle.dump(Monsterlist, Monsters)
            Monsters.close()
        #"observe <monster_name>" --observe certain monster
        

        #"fight <monster_name>" --fight with a certain monster
        elif commandWords[0].lower() == "fight":
            targetName = command[6:]
            target = player.location.getMonsterByName(targetName)
            if target != False:
                target.fighting = True
                player.fighting = True
                print("You are now fighting with " + str(target.name) + ".")
                input("Press enter to continue... ")
                while target.fighting and player.fighting:
                    #print fight situation 
                    clear()

                    printfight()
                    fightcommandS  = False
                    while not fightcommandS:
                        fightcommandS = True    
                        fightcommand = input("What to do?")
                        fightcommandWords = fightcommand.split()
                        monsterApattern = random.choice(list(target.attackPattern))
                        print("The attack pattern of " + str(target.name) + " now is: " + str(monsterApattern))
                        #attack the monster 
                        if fightcommandWords[0].lower() == "attack":
                            if len(player.attackPattern) > 1:
                                input("HEEEEEEEE!")
                                healthminusPER = ((player.attackPattern[player.weapon.name][1]) * (player.attributes['strength']) - target.attackPattern[monsterApattern][2] )
                                if healthminusPER > 0:
                                    target.health -= healthminusPER * player.attackPattern[player.weapon.name][0]
                                    print()
                                    print("monster's health " + str(-healthminusPER) + " * " + str(player.attackPattern[player.weapon.name][0]))
                                    input("Press enter to continue...")
                                else:
                                    print()
                                    print("Your weapon is too weak to break " + str(target.name) + "'s defense. Sad...")
                                    input("Press enter to continue...")
                                if target.health <= 0:
                                    print(target.name + " dies.")
                                    input("Press enter to continue...")
                                    target.die()
                                    target.fighting =False
                            else:
                                input("HEEEEEEEE!")
                                healthminusPER = ((player.attackPattern['normal'][1]) * (player.attributes['strength'])- target.attackPattern[monsterApattern][2] )
                                if healthminusPER > 0:
                                    target.health -= healthminusPER * player.attackPattern['normal'][0]
                                    print()
                                    print("monster's health " + str(-healthminusPER) + " * " + str(player.attackPattern['normal'][0]))
                                    input("Press enter to continue...")
                                else:
                                    print()
                                    print("Your weapon is too weak to break " + str(target.name) + "'s defense. Sad...")
                                    input("Press enter to continue...")
                                if target.health <= 0:
                                    print(target.name + " dies.")
                                    input("Press enter to continue...")
                                    target.die()
                                    target.fighting =False
                        #use items during a fight
                        elif fightcommandWords[0].lower() == "useitem":
                            if player.items != []:
                                player.showInventory()
                                usethisitemName = input("Which item to use?")
                                usethisitem = player.getItemByName(usethisitemName)
                                if usethisitem != False:
                                    if usethisitem.fightuse != False:
                                        if type(usethisitem) == Weapon:
                                            if player.weapon != None:
                                                player.unequipW(player.weapon)
                                                player.equipW(usethisitem)
                                            else:
                                                player.equipW(usethisitem)
                                        elif type(usethisitem) == Armor:
                                            if player.armor != None:
                                                player.unequipA(player.armor)
                                                player.equipA(usethisitem)
                                            else:
                                                player.equipA(usethisitem)
                                        else:
                                            for u in usethisitem.usage:
                                                if usethisitem.usage[u] != 0:
                                                    player.increaseStatus(u, usethisitem.usage[u])
                                                    player.deleteItem(usethisitem)
                                    else:
                                        print("You cannot use this item in a fight.")
                                        fightcommandS = False
                                else:
                                    print("No such item.")
                                    fightcommandS = False
                            else:
                                print("You have nothing, sadly.")
                                fightcommandS = False
                        #escape from a fight
                        elif fightcommandWords[0].lower() == "escape":
                            print("Run!!! Run!!!")
                            input("Press enter to continue...")
                            player.fighting = False

                        else:
                            print("Not a valid command in a fight.")
                            fightcommandS = False

                    #it's monster's time to attack!
                    if target.fighting != False:
                        print()
                        print("It's time for " + str(target.name) + " to attack back!")
                        input("Press enter to continue...")
                        attackcount = target.attackPattern[monsterApattern][0]
                        while attackcount > 0:
                            print()
                            input("This is attack " + str(target.attackPattern[monsterApattern][0] + 1 - attackcount))
                            randomA = random.random()
                            if randomA <= player.attributes['agility']:
                                print(str(target.name) + " misses its attack~")
                                input("Press enter to continue...")
                            else:
                                if player.weapon != None:
                                    playerhealthminusperattack = target.attackPattern[monsterApattern][1] -player.attributes['defend'] * player.attackPattern[player.weapon.name][2]
                                    if playerhealthminusperattack > 0:
                                        player.attributes['hp'] -= playerhealthminusperattack
                                else:
                                    playerhealthminusperattack = target.attackPattern[monsterApattern][1] -player.attributes['defend'] * player.attackPattern['normal'][2]
                                    if playerhealthminusperattack > 0:
                                        player.attributes['hp'] -= playerhealthminusperattack
                                print()
                                if playerhealthminusperattack > 0:
                                    print("player's health " + str(-playerhealthminusperattack))
                                    input("Press enter to continue...")
                                else:
                                    print("You have awesome defend, " + str(target.name) + " cannot harm you.")
                                    input("Press enter to continue...")
                                if player.attributes['hp'] <= 0:
                                    player.alive = False
                                    player.fighting = False
                                    print("You die.")
                                    input("Please restart the game")
                            attackcount -= 1        

        #invalid command
        else:
            print("Not a valid command")
            commandSuccess = False

    #update something after moving
    #if timePasses == True:
        #updater.updateAll()

    


