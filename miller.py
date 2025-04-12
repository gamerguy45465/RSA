import random as rd

'''Implement (in Python) a function that takes an integer as input and returns True or False as output,
indicating whether or not the integer is prime. Use the Monte Carlo probabalistic algorithm discussed in section 7.2,
so that it will finish in reasonable time given several hundred digit test numbers. We will use this piece of code later
when we implement RSA encription.


Hint: Replace the Python command:
remainder = b ** e % n
with the equivalent but far faster:
remainder = pow(b,e,n)

Test your code really good. I suggest comparing your prime testing function versus the standard prime testing function for
all integers from 3 through 1 million. Then test your function on 200 digit primes by comparing your results to those found on
Prime Generator Web PageLinks to an external site. or https://bigprimes.org/Links to an external site. . Also test it on big composite
numbers. You could make a big composite number by multiplying 2 100 digit primes together.

Reminder: Do not go find code on the web that does this. This is a programming class, so implement your own solutions!

Submit:
Pass off in person, and submit your code.'''


def MonteCarlo(x):
    if(x <= 20):
        if not isPrimeStandard(x):
            return False

    else:
        for i in range(20):
            if not MillersTest(x):
                return False



    return True




def isPrimeStandard(n): #This is a greedy algorithm
    if n == 2: #If it is equal to 2, then it is prime
        return True

    if n % 2 == 0: #Check if it is even, but not equal to 2
        return False

    factors = [] # Declaring Array to hold feasible solutions

    for i in range(1, n + 1):
        value = n/i # Select
        if str(value).endswith(".0"): #checking Feasibility
            factors.append(int(value)) #If Feasable, append it to our results


    if(factors[0] == n and factors[1] == 1): #If minimized, Return True
        return True

    return False #Otherwise return false


def MillersTest(n):
    b = rd.randrange(2, n)
    nm1 = n - 1
    s = 0
    while (nm1 % 2 == 0):
        nm1 //= 2
        s += 1

    T = nm1

    if pow(b, T, n) == 1:
        return True


    for j in range(0, s):
        if pow(b, T, n) == (n - 1):
            return True
        T *= 2

    return False








def main():
    for i in range(3, 105):
        value = MonteCarlo(i)
        if value:
            print(i)




    





if __name__ == "__main__":
    main()