'''Prime Number sieves
There are many ways to find prime numbers
We will print all prime numbers 2 thru 100'''

from math import sqrt

# Here's a very simple way to do it
def TrialDivision():
    IsPrime = True
    for i in range(2, 101):
        j = 2
        while(IsPrime and j < i):
            if(i % j == 0):
                IsPrime = False
            #End if
            j += 1
        #End while
        if(IsPrime):
            print(i)
        IsPrime = True
        #End IF
    #End for
#End TrialDivision
#This method works, but it is inefficient because we are testing every possible combination
