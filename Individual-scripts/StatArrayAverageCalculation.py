'''
Dnd ability score array average calculation
For all six ability rolls, using 4d6, drop lowest, arrange to taste method
By Tom
'''

from random import randint

def main():
    rollSums = [0, 0, 0, 0, 0, 0]#Placeholder values
    
    for countArrays in range(10000):
        statArray = []#Empty list for rolls
        
        for abScrRolls in range(6):
            fourD6 = []
            for k in range(4):#Roll four dice
                fourD6.append(randint(1,6))
                
            abilityScore = ScoreProcess(fourD6)
            statArray.append(abilityScore)
            #End for
        #End for
        selSort(statArray)
        
        for k in range(6):
            rollSums[k] += statArray[k]
            
    rollAverage = []
    for x in range(6):
        placeAverage = (rollSums[x]/10000)
        placeAverage = round(placeAverage, 2)
        rollAverage.append(placeAverage)
    #End for
    print(rollAverage)
    #input('Press any key to close...')
    #This is a 'press any key to continue' command
    #End main

def ScoreProcess(arr):#Drop lowest die, add the rest, return the sum
    LowRoll = 0
    
    for i in range(1,4):#Find lowest die
        if arr[i] < arr[LowRoll]:
            LowRoll = i
    RollTotal = 0
    
    for i in range(4):#Take sum of three best dice
        RollTotal += arr[i]
    AbScr = RollTotal-arr[LowRoll]
    return AbScr

def selSort(arr):#Selection Sort
    for i in range(len(arr)):
        highIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[highIndex]:
                highIndex = j
        arr[i], arr[highIndex] = arr[highIndex], arr[i]
        #end selSort
        
    
main()
