'''
Calculating what an average D&D ability score would be
using 4d6 drop lowest method
By Tom
'''

from random import randint

def main():
    AvgTotal = 0
    for count in range(10000):#Roll 4d6, place in array
        AbilityRoll = []
        for i in range(4):
            AbilityRoll.append(randint(1,6))
        AbilityScore = ScoreProcess(AbilityRoll)
        AvgTotal += AbilityScore
        #End For
    AvgScore = AvgTotal/10000
    AvgScore = round(AvgScore, 2)
    print('Average Score: ', AvgScore)
    #End main
    
def ScoreProcess(arr):#Drop lowest die, add the rest, return the sum
    LowRoll = 0
    for i in range(4):
        if arr[i] < arr[LowRoll]:
            LowRoll = i
    RollTotal = 0
    for i in range(4):
        RollTotal += arr[i]
    AbScr = RollTotal-arr[LowRoll]
    return AbScr

main()
