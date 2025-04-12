import random
from rsa import RSA
import helpers


def main():
    security_thingy = RSA(5)

    string1 = ""
    string2 = ""

    for i in range(200):
        letter1 = random.randrange(0, 26)
        letter2 = random.randrange(0, 26)
        string1 += chr(letter1 + 97)
        string2 += chr(letter2 + 97)



    security_thingy.GenerateKeys(string1, string2)
    print(security_thingy.Encrypt("input.txt", "output.txt"))
    security_thingy.Decrypt("output.txt", "decryptoutput.txt")








if __name__ == '__main__':
    main()



