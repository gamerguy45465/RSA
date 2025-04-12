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

        if(p % 2 == 0):
            p += 1

        if(q % 2 == 0):
            q += 1

        while(not miller.MonteCarlo(p)):
            p += 2

        while(not miller.MonteCarlo(q)):
            q += 2


        n = p * q

        r = (p - 1) * (q - 1)

        e = 10**398 + 1

        while(helpers.EuclideanAlgorithm(e, r) != 1):
            e += 1


        d = helpers.inverse(e, r)

        publicFile = open("public.txt", "w")

        publicFile.truncate()

        publicFile.write(str(n) + "\n")
        publicFile.write(str(e) + "\n")

        publicFile.close()


        privateFile = open("private.txt", "w")

        privateFile.truncate()

        privateFile.write(str(n) + "\n")
        privateFile.write(str(d) + "\n")

        privateFile.close()



    def FileHandler(self, input_text_file, out_text_file):
        InputFile = open(input_text_file, "rb")
        OutputFile = open(out_text_file, "w")

        PlainTextBinary = InputFile.read()
        PlainText = PlainTextBinary.decode("utf-8")
        InputFile.close()

        alphabet = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        new_plain_text = helpers.alphabetToNumber(PlainText, alphabet)

        new_plain_text_list = helpers.fromBase(70, new_plain_text)

        M = helpers.SumofArray(new_plain_text_list)

        # Public: n e
        # Private: n d

        publicFile = open("public.txt", "r")
        privateFile = open("private.txt", "r")

        Public = []
        Private = []

        for i in range(2):
            Public.append(publicFile.readline())
            Private.append(privateFile.readline())

        publicFile.close()
        privateFile.close()

        n = Public[0]
        e = Public[1]
        d = Private[1]

        return (M, n, e, d, OutputFile)








    def Encrypt(self, input_text_file, out_text_file):
        (M, n, e, d, OutputFile) = self.FileHandler(input_text_file, out_text_file)

        C = pow(M, int(e), int(n))

        OutputFile.truncate()
        OutputFile.write(str(C) + "\n")

        return C





    def Decrypt(self, input_text_file, output_text_file):
        (M, n, e, d, OutputFile) = self.FileHandler(input_text_file, output_text_file)


        return "Hello World"









