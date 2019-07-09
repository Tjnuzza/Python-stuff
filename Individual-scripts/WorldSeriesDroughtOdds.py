'''Sports drought chance calculation
What are the random odds of one baseball team
not winning a World Series for 100 years?'''

from random import randrange

def main():
    print('What are the chances the Cubs wouldn\'t win a World Series for 100 years?')
    droughts = 0
    for x in range(10000):
        seriesWinners = []
        for count in range(100):
            seriesWinners.append(randrange(30))#30 teams
        centuryDrought = arrayScan(seriesWinners)
        if centuryDrought:
            droughts += 1
    print('Drought Chance: ', droughts/100, '%')
    #End main

def arrayScan(arr):
    noWins = True
    for s in range(len(arr)):
        if arr[s] == 0:
            noWins = False
            break
    return noWins

main()
