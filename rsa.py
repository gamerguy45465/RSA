import miller
import permutation
import exchange
import helpers


class RSA:
    def __init__(self, keys):
        self.keys = keys

    def GenerateKeys(self, text_string1, text_string2):
        p = helpers.RSA_Base26(text_string1)
        q = helpers.RSA_Base26(text_string2)

        if(p < 10**200 or q < 10**200):
            print("Error: Input strings are too short")
            quit()

        modp = p % 10**200
        modq = q % 10**200

        if(p % 2 == 1):
            p += 1

        if(q % 2 == 1):
            q += 1

        while(not miller.MillersTest(p)):
            p += 2

        while(not miller.MillersTest(q)):
            q += 2


        n = p * q

        r = (p - 1) * (q - 1)







    def Encrypt(self, input_text_file, out_text_file):
        return "Hello World"



    def Decrypt(self, input_text_file, output_text_file):
        return "Hello World"



