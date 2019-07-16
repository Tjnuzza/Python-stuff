'''
Advantage/disadvantage calculation for D&D fifth edition
By Tjnuzza
'''

from random import randint

def main():
    NormalRoll()
    AdvantageRoll()
    DisadvantageRoll()
    #End Main
    
def NormalRoll():#10000 normal d20 rolls
    RollTotal = 0
    for count in range(10000):
        RollTotal += randint(1,20)
    RollAverage = RollTotal/10000
    RollAverage = round(RollAverage, 1)
    print('Normal Roll Average: ', RollAverage)
    #End NormalRoll
    
def AdvantageRoll():#Roll 2d20 and keep the higher roll
    RollTotal = 0
    for count in range(10000):
        die1 = randint(1,20)
        die2 = randint(1,20)
        if die1 > die2:
            RollTotal += die1
        else:
            RollTotal += die2
    RollAverage = RollTotal/10000
    RollAverage = round(RollAverage, 1)
    print('Advantage Roll Average: ', RollAverage)
    #End AdvantageRoll
    
def DisadvantageRoll():#Roll 2d20 and keep the lower roll
    RollTotal = 0
    for count in range(10000):
        die1 = randint(1,20)
        die2 = randint(1,20)
        if die1 < die2:
            RollTotal += die1
        else:
            RollTotal += die2
    RollAverage = RollTotal/10000
    RollAverage = round(RollAverage, 1)
    print('Disadvantage Roll Average: ', RollAverage)
    #End DisadvantageRoll
    
main()