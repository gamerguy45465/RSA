def alphabetToNumber(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    Number = []

    for letter in message:
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                Number.append(i)


    return Number



def toBase(b, number): #Assuming that the message was already converted to its index equivalent
    result = ""

    for i in range(len(number)):
        base_number = int(number[i]) % b
        result += str(base_number)


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
    the_new_list = alphabetToNumber(the_string)
    the_newer_list = fromBase(26, the_new_list)
    the_newest_sum = SumofArray(the_newer_list)

    return the_newest_sum


def EuclideanAlgorithm(number1, number2):
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


    return bigger




