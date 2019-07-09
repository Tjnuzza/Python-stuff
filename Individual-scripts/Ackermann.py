'''Tom Nuzzarello
Ackermann function experiment
This is a non-primitive recursive mathematical function
Like in C++, this function exceeds max recursion very easily'''

def main():
    print('Ackermann function')
    m = int(input('Enter M: '))
    n = int(input('Enter N: '))
    result = ack(m,n)
    print(result)
    #End main

def ack(m,n):
    if (m == 0):
        return n + 1
    elif (n == 0):
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))
    #End ackermann

main()
