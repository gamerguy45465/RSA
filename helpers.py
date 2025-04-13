import math

def alphabetToNumber(message, alphabet):
    Number = []

    for letter in message:
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                Number.append(i)


    return Number


def numberToAlphabet(number, alphabet):
    Message = ""

    for individual in number:
        for i in range(len(alphabet)):
            if individual == alphabet[i]:
                Message += str(alphabet[i])


    return Message



def toBase(b, number): #Assuming that the message was already converted to its index equivalent
    result = []

    for i in range(len(number)):
        base_number = int(number[i]) % b
        result.append(base_number)


    return result


def fromBase(b, number):
    result = []
    for i in range(len(number) - 1, 0, -1):
        result.append(int(number[i])**i)

    return result




def SumofArray(arr):
    the_sum = 0

    for i in range(len(arr)):
        the_sum += arr[i]


    return the_sum


def RSA_Base26(the_string):
    the_new_list = alphabetToNumber(the_string, "abcdefghijklmnopqrstuvwxyz")
    the_newer_list = fromBase(26, the_new_list)
    the_newest_sum = SumofArray(the_newer_list)

    return the_newest_sum


'''def EuclideanAlgorithm(number1, number2):
    bigger = 0
    smaller = 0
    if(number1 > number2):
        bigger = number1
        smaller = number2

    else:
        bigger = number2
        smaller = number1


    while(smaller != 1 and smaller != 0):
        if(smaller != 0):
            q = bigger // smaller
            r = bigger % smaller
            bigger = q
            smaller = r
            isTrue = bigger > smaller


    return bigger'''


def EuclideanAlgorithm(number1, number2):
    equations = []
    dividends = []
    divisors = []
    quotients = []
    remainders = []

    quotient = math.inf
    remainder = math.inf

    while(remainder != 1 and remainder != 0):

        quotient = number2 // number1
        remainder = number2 % number1
        equation = str(number2) + " = " + str(number1) + " * " + str(quotient) + " + " + str(remainder)
        dividends.append(number2)
        divisors.append(number1)
        quotients.append(quotient)
        remainders.append(remainder)
        equations.append(equation)
        number2 = number1

        number1 = remainder


    return remainders[len(remainders) - 1]







def inverse(a, n):
    t = 0
    r = n 
    newt = 1
    newr = a
    
    while newr != 0:
        quotient = r // newr
        (t, newt) = (newt, t - quotient * newt)
        (r, newr) = (newr, r - quotient * newr)
        
    
    if r > 1:
        return "a i not invertible"
    
    if t < 0:
        t = t + n
        
    return t





