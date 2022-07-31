import math
import random

def getGCD(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return (math.gcd(a%b, b))
    if a < b:
        return (math.gcd(a, b%a))


#Test code
if 0 == 0:
    print(getGCD(10, 15)) #5
    print(getGCD(24, 12)) #12

def isCoprime(a, b):
  return math.gcd(a, b) == 1

def calculateProbability(end, steps):
    count = 0
    for i in range(0, steps):
            # get two random integers, from 1 to $end
        number_0 = random.randint(1, end)
        number_1 = random.randint(1, end)
            
            # increment the counter if both integers are coprimes,
            # coprimes: greatest common divisor is 1. gcd(nu0, nu1) == 1
        if math.gcd(number_0, number_1) == 1:
            count += 1
            
    return float(count)/steps	

print(calculateProbability(1000000, 1000)) #0,608 0,604 0,594 0,604 0,617


