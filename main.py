from room import Room
from player import Player
from item import Item
from monster import Monster
import os
import updater

#function def

#function to initialize world

Roomlist = []

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
    Rock = Item("Rock", "This is just a rock.", {})
    Rock.putInRoom(b1)

    Bandage = Item("Bandage", "This is a Bandage that can increase hp.", {'hp': 10})
    Bandage.putInRoom(c1)

    #set up player's location
    player.location = hall1

    #set up monsters
    Monster("Bob the monster", 20, b1)

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
        for i in player.location.items:
            print(i.name)
        print()

    #exit info
    print("You can go in the following directions:")
    for e in player.location.exitNames():
        print(e)
    print()
    #show hel[]
    print("input 'help' to get more information")
    print()



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

    print()
    print("Monster: ")
    print("attack <monster_name> -- attack the given monster")

    print()
    print("Gameplay: ")
    print("exit -- quit the game")

    print()
    input("Press enter to continue...")

def getRoomByName(name, L):
        for i in L:
            if i.name.lower() == name.lower():
                return i
        return False

#function def end

#game start

#create a player
player = Player()

#create the world
createWorld()
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

        elif commandWords[0].lower() == "teleport":
            checking = player.location.isPortal
            if checking != False:
                print("A huge cyclone appears and you are blowed up to the sky~")
                input("Press enter to tranverse!")
                destName = "hall" + str(player.location.layer + 1)
                dest = getRoomByName(destName, Roomlist)
                player.location = dest
                print()
                print("Welcome to level "+str(player.location.layer))
                print("The mosters are more challenging here. Be careful.")
                input("Press enter to continue...")
                print()
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
            
        #"help" --show commands instruction
        elif commandWords[0].lower() == "help":
            showHelp()

        #"exit" --exit game
        elif commandWords[0].lower() == "exit":
            playing = False

        #"observe <monster_name>" --observe certain monster
        

        #"attack <monster_name>" --attack certain monster
        elif commandWords[0].lower() == "attack":
            targetName = command[7:]
            target = player.location.getMonsterByName(targetName)
            if target != False:
                player.attackMonster(target)
            else:
                print("No such monster.")
                commandSuccess = False

        #invalid command
        else:
            print("Not a valid command")
            commandSuccess = False

    #update something after moving
    #if timePasses == True:
        #updater.updateAll()

    


