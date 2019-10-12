#On 2d6 and 2d8 Indra rolled 4 1s
#What are the odds?

from random import randrange

def main():
    count = 0
    for i in range(10000):
        count += BadRoll()
    print(str(count) + " out of 10,000")

def BadRoll():
    arr = [0, 0, 0, 0]
    arr[0] = randrange(6) + 1
    arr[1] = randrange(6) + 1
    arr[2] = randrange(8) + 1
    arr[3] = randrange(8) + 1
    if arr == [1, 1, 1, 1]:
        return 1
    else:
        return 0

main()
