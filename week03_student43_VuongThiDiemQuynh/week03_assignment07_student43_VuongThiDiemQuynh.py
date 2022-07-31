'''
    Problem 3: 
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
'''

def isPrime(n):
    for i in range(2,n):
        if (n % i == 0):
            return False
    return True
        

def getLargestPrimeFactor(n):
    listPrimeFactors = []
    for i in range(1,n):
        if (n % i == 0) & isPrime(i):
            listPrimeFactors.append(i)
    return listPrimeFactors[-1]

    
print(getLargestPrimeFactor(6008)) #751