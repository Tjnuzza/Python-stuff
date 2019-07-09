'''Tom Nuzzarello
Random character generator for DnD 5e
Now with PHB options only'''

from random import randrange

def main():
    character = ['background','race','class']
    #We won't roll for subclass just yet
    for i in range(100):
        character[0] = getBackground()
        character[1] = getRace()
        character[2] = getClass()
        print(character)
        #end for
    #end main

def getBackground():
    backgroundList = ['acolyte','charlatan','criminal','entertainer','folk hero','guild artisan','hermit','noble','outlander','sage','sailor','soldier','urchin']
    return backgroundList[randrange(12)]

def getRace():
    raceList = ['dwarf','elf','halfling','human','dragonborn','half-elf','half-orc','gnome','tiefling']
    return raceList[randrange(8)]

def getClass():
    classList = ['barbarian','bard','cleric','druid','fighter','monk','paladin','ranger','rogue','sorceror','warlock','wizard']
    return classList[randrange(11)]

main()
