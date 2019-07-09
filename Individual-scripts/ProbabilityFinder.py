'''
Monster rare drop probability determiner
'''

from random import randrange
total = 0
drop = 0

for i in range(10000):#Ten thousand iterations
    found = False
    for j in range(100):#Amount of monsters you killed
        drop = randrange(100)#Probability of drop = 1/X
        if drop == 0:
            found = True
            break
    if found:
        total += 1
    #End for

print(total/10000)
#End
