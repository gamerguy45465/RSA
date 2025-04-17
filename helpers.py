import math
import sys

def alphabetToNumber(alphabet, message):
    Number = 0

    for letter in message:
        pos = alphabet.find(letter)

        if(pos != -1):
            Number = Number * len(alphabet) + pos



    return Number


def alphabettest(alphabet, message):
    C = ""
    print("Message: ", message)
    for i in range(len(message) - 2):
        print("I: ", i)
        print("Messages[i]: ", message[i])
        k = str(message[i])
        print("K", k)
        j = int(k)
        C += alphabet[j]

    print(C)


def justaNumber(alphabet, number):
    S = ""
    text = numberToAlphabet(alphabet, int(number))

    for i in range(len(text)):
        pos = alphabet.find(text[i])
        S += str(pos)


    return S


def justaString(alphabet, number):
    S = ""
    string_number = str(number)


    print("String_Number: ", string_number)



    for i in range(0, len(string_number) - 1, 2):
        letter = string_number[i] + string_number[i + 1]
        if(int(letter) < 70):
            S += alphabet[int(letter)]




    return S






def numberToAlphabet(alphabet, number):

    '''Message = ""

    for individual in number:
        for i in range(len(alphabet)):
            if individual == alphabet[i]:
                Message += str(alphabet[i])


    return Message '''

    l = len(alphabet)
    s = alphabet[number % l]
    value = number // l
    while value > 0:
        s += alphabet[value % l]
        value = value // l


    s = s[len(s)-1::-1]
    return s




def toBase(b, number): #Assuming that the message was already converted to its index equivalent
    '''result = ""

    for i in range(len(number)):
        base_number = int(number[i]) % b
        result += str(base_number)


    return result'''

    result = ""

    q = int(number)
    k = 0

    while q != 0:
        result += str(q % b)
        q = q // b
        k = k + 1

    return result


def fromBase(b, number):
    result = ""
    for i in range(len(number) - 1, 0, -1):
        result += str(b * int(number[i])**i)

    return result




def SumofArray(arr):
    the_sum = 0

    for i in range(len(arr)):
        the_sum += arr[i]


    return the_sum

def textToNumber(text):
    number = ""
    alphabet = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for letter in text:
        pos = alphabet.find(letter)
        number += str(pos)

    return int(number)



def RSA_Base26(the_string):
    the_new_list = textToNumber(the_string)

    return the_new_list


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

    #print(remainders)
    #print(equations)


    if(remainders[len(remainders) - 1] == 1):
        return remainders[len(remainders) - 1]


    else:

        return remainders[len(remainders) - 2]







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



print(toBase(70, "81"))





