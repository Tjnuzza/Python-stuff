'''Death save calculation
What are the odds of making your death saves in 5e DnD?'''

from random import randint

survival = 0

for i in range(10000):
    successes = 0
    failures = 0
    
    while successes < 3 and failures < 3:
        roll = randint(1,20)
        if roll == 20:
            successes = 3
        elif roll == 1:
            failures += 2
        elif roll >= 10:
            successes += 1
        else:
            failures += 1
    #End while
    if successes == 3:
        survival += 1
#End for

print(survival / 10000)
