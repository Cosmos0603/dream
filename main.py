from room import Room
from player import Player
from item import Item
from monster import Monster
import os
import updater

#function def

#setup world
def createWorld():

    #set up rooms
    hall1 = Room("You are in Hallway",1,False)
    a1 = Room("You are in room 1",1,False)
    b1 = Room("You are in room 2",1,False)
    c1 = Room("You are in room 3",1,False)
    d1 = Room("You are in room 4",1,False)
    e1 = Room("You are in room 5",1,False)
    Room.connectRooms(a1, "hall1", hall1, "a1")
    Room.connectRooms(b1, "hall1", hall1, "b1")
    Room.connectRooms(c1, "hall1", hall1, "c1")
    Room.connectRooms(d1, "hall1", hall1, "d1")
    Room.connectRooms(e1, "hall1", hall1, "e1")

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

    


