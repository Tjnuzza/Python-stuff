'''Tom Nuzzarello
Fast stat array roller
Method: 4d6 drop lowest, 6 times, arrange to taste'''

from random import randint

def main():
    rolls = int(input('Enter Rolls: '))
    
    for countArrays in range(rolls):
        statArray = []
        for abScrRolls in range(6):
            DieRolls = []
            for k in range(4):
                DieRolls.append(randint(1,6))
                #End for
            abilityScore = ScoreProcess(DieRolls)
            statArray.append(abilityScore)
            #End for
        SelSort(statArray)
        
        print(statArray)
        #End for
    #End main

def ScoreProcess(arr):#Drop lowest die, add the rest, return the sum
    LowRoll = 0
    for i in range(1,4):#Remember to add 1 to the endpoint or it will skip the last element
        if arr[i] < arr[LowRoll]:
            LowRoll = i
    RollTotal = 0
    for i in range(4):
        RollTotal += arr[i]
    AbScr = RollTotal-arr[LowRoll]
    return AbScr

def SelSort(statArray):
    for i in range(len(statArray)):
        highIndex = i
        for j in range(i+1, len(statArray)):
            if statArray[j] > statArray[highIndex]:
                highIndex = j
                    
        temp = statArray[i]
        statArray[i] = statArray[highIndex]
        statArray[highIndex] = temp
    return statArray

main()
