#Roulette project 2.0

from random import randint
from time import sleep

print('Welcome to Roulette')

def main():
    cash = 100#The player will start with $100
    betChoice = 0
    
    while cash > 0 and betChoice !=7:
        betChoice = menu(cash)
        
        if betChoice != 7:
            betNum, betMoney = getBet(cash, betChoice)
            betOdds = getOdds(betChoice)
            ballNum, ballColor = spinWheel()
            winner = WinLose(betChoice, betNum, ballNum, ballColor)
            cash = results(winner, cash, betMoney, betOdds)
            #End if
        #End while
    print()#This prints an empty line
    print('You have $', cash)
    print('goodbye')

def menu(cash):#This function tells the user how much money they have, and asks what they want to bet, or if they want to quit
    print()
    print('You have $', cash)
    print('1 for red/odd (pays 1:1)')
    print('2 for black/even (pays 1:1)')
    print('3 for 1-12 (pays 2:1)')
    print('4 for 13-24 (pays 2:1)')
    print('5 for 25-36 (pays 2:1)')
    print('6 for one number (pays 35:1)')
    print('7 to quit')
    
    while True:#This is the Python equivalent of a do-while loop
        betChoice = int(input('What is your choice? '))
        if betChoice >= 1 and betChoice <=7:
            break
    return betChoice

def getBet(cash, betChoice):#This function asks how much money the user wants to bet
    betNum = 0
    if betChoice == 6:#If the user bets on one number, they will be asked here
        betNum = int(input('Which number will you bet on (0-36)? '))
        
    while betNum < 0 or betNum > 36:
        print('You cannot bet on that number.')
        betNum = int(input('Which number will you bet on (0-36)? '))
    
    betMoney = int(input('How much would you like to bet? '))
    while betMoney > cash:
        print('You don\'t have that much money')
        betMoney = int(input('How much would you like to bet? '))
    while betMoney <= 0:
        print('You cannot bet that amount')
        betMoney = int(input('How much would you like to bet? '))
        
    return betNum, betMoney

def getOdds(betChoice):#Determines the multiplier if you win
    if betChoice == 6:
        betOdds = 35
    elif betChoice >= 3:
        betOdds = 2
    else:
        betOdds = 1
    return betOdds

def spinWheel():#This function chooses a random number and then assigns it a color
    print('Let\'s spin...')
    sleep(3)#Simulates the wheel spinning for 3 seconds
    ballNum = randint(0,36)
    if ballNum == 0:
        ballColor = 'green'
    elif ballNum%2 == 1:
        ballColor = 'red'
    else:
        ballColor = 'black'
        # End if
    return ballNum, ballColor

def WinLose(betChoice, betNum, ballNum, ballColor):#This function decides if you won or lost
    print('You rolled', ballNum, ',', ballColor)
    winner = False#This assumes you lost so we don't need a 'False' for every if
    
    if betChoice == 1:
        if ballColor == 'red':
            winner = True
            
    elif betChoice == 2:
        if ballColor == 'black':
            winner = True
            
    elif betChoice == 3:
        if ballNum >= 1 and ballNum <= 12:
            winner = True
            
    elif betChoice == 4:
        if ballNum >= 13 and ballNum <= 24:
            winner = True
            
    elif betChoice == 5:
        if ballNum >= 25 and ballNum <= 36:
            winner = True
            
    else:
        if ballNum == betNum:
            winner = True
            
    return winner

def results(winner, cash, betMoney, betOdds):
    
    if winner == True:
        print('You win!')
        cash += betMoney * betOdds
        
    else:
        print('You lose...')
        cash -= betMoney
        
    return cash

main()
