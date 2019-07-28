'''Advanced FizzBuzz problems
By Tjnuzza

We've all seen this problem a million times
But there are many different ways to solve it
Let's look at a few of them'''

# First let's do the obvious way
def ClassicFizzBuzz(num):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)
    #End ClassicFizzBuzz
'''This will work but it has a few problems
If we decide that Buzz should fire on multiples of 7, then we need to change two values
Not a big deal here, but could be a headache in real code
So let's define them as variables'''

def VariableFizzBuzz(num):
    fizz = 3
    buzz = 5
    if num % fizz == 0 and num % buzz == 0:
        print("FizzBuzz")
    elif num % buzz == 0:
        print("Buzz")
    elif num % fizz == 0:
        print("Fizz")
    else:
        print(num)
    #End VariableFizzBuzz

'''Now our values need to be defined only once
But what if we want to add another condition
Like "Fuzz" for numbers divisible by 7?
Then instead of having four possible outputs, we have eight
So what can we do? Let's concatenate strings'''

def ConcatenateFizzBuzz(num):
    message = ""
    if num % 3 == 0:
        message += "Fizz"
    if num % 5 == 0:
        message += "Buzz"
    if message == "":
        message += str(num)
    print(message)
    #End ConcatenateFizzBuzz

'''This allows us to add another condition if we so desire
And it should work as long as that final condition is always last, but it still looks a little repetitive
One last one: Let's define our values in a dictionary, then we can loop through it to get our values'''

def ArrayFizzBuzz(num):
    Values = {
        3 : "Fizz",
        5 : "Buzz"
    }
    # By the way, this is how you declare a dictionary in Python
    # Keys on left, values on right
    # Probably not a coincidence that it looks like JSON
    message = ""
    for (x, y) in Values.items():
        if num % x == 0:
            message += y
    if message == "":
        message += str(num)
    print(message)
    #End ArrayFizzBuzz

# This last one let's us add a single key-value pair to create more conditions
# It's a bit complicated to whiteboard, but it's the best way to handle it in the time I care to spend on it
