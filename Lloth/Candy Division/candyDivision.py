wow = int(input())
import math

def printDivisors(n) :
    list = []

    for i in range(1, int(math.sqrt(n) + 1)) :

        if (n % i == 0) :

            if (n / i == i) :
                print (i)
            else :
                print (i)
                print(n/i)
                list.append(int(n/i))


    for i in list[::-1] :
        print (i, end=" ")

# Driver method
printDivisors(wow)
