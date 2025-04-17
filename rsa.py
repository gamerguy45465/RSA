import miller
import permutation
import exchange
import helpers


class RSA:
    def __init__(self, keys):
        self.keys = keys
        self.r = 0
        self.C = []
        self.indices = []
        self.divides = 200

    def GenerateKeys(self, text_string1, text_string2):
        p = helpers.RSA_Base26(text_string1)
        q = helpers.RSA_Base26(text_string2)

        if(p < 10**200 or q < 10**200):
            print("Error: Input strings are too short")
            quit()

        p = p % 10**200
        q = q % 10**200

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

        self.r = r

        e = 10**398 + 1

        while(helpers.EuclideanAlgorithm(e, r) != 1):
            e += 1


        print("E: ", e)
        print("R: ", r)


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

    def FileHandler(self, input_text_file, out_text_file, encrypt=True):
        InputFile = open(input_text_file, "rb")
        OutputFile = open(out_text_file, "wb")

        PlainTextBinary = InputFile.read()
        PlainText = PlainTextBinary.decode("utf-8")
        InputFile.close()

        print(PlainText)

        alphabet = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        if(encrypt == True):
            the_number_text = ""
            for i in range(len(PlainText)):
                the_text = ""
                the_number = helpers.textToNumber(PlainText[i])
                print("The Number: ", the_number)
                if(the_number <= 9):
                    the_text += "0" + str(the_number)
                    self.indices.append(i)
                    the_number_text += the_text

                else:
                    the_text += str(the_number)
                    the_number_text += the_text



            print("The Number Text: ", the_number_text)

            #the_number_text = helpers.alphabetToNumber(alphabet, PlainText) #Instead of a list, return 1 base 10 number
            test = str(the_number_text)
            for number in test:
                print(number, ", ")
            new_plain_text = the_number_text

            Blocks = []
            SubBlocks = ""
            isToFour = 0
            for i in range(len(new_plain_text)):

                plainText = new_plain_text[i]
                new_number_text = helpers.fromBase(len(alphabet), plainText)
                SubBlocks += str(plainText)
                isToFour += 1

                if(i == (len(new_plain_text) - 1)):
                    SubBlocks += "04"
                    Blocks.append(SubBlocks)
                    SubBlocks = ""

                if (isToFour >= self.divides):
                    Blocks.append(SubBlocks)
                    SubBlocks = ""
                    isToFour = 0

        else:
            new_plain_text = PlainText
            Blocks = []
            SubBlocks = ""
            for i in range(len(new_plain_text)):
                if (new_plain_text[i] != "$"):
                    SubBlocks += new_plain_text[i]

                else:
                    Blocks.append(SubBlocks)
                    SubBlocks = ""






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

        print("E: ", e)

        print("D: ", d)

        return (Blocks, n, e, d, OutputFile)








    def Encrypt(self, input_text_file, out_text_file):
        (M, n, e, d, OutputFile) = self.FileHandler(input_text_file, out_text_file)

        C = []

        for i in range(len(M)):
            new_M = M[i]
            print("The M: ", M)
            C.append(pow(int(M[i]), int(e), int(n)))

        OutputFile.truncate()

        alphabet = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        for i in range(len(C)):
            New_C = str(C[i])
            Message = New_C + "$"

            OutputFile.write(Message.encode("utf-8"))

        OutputFile.close()

        self.C = C

        return C





    def Decrypt(self, input_text_file, output_text_file):
        (M, n, e, d, OutputFile) = self.FileHandler(input_text_file, output_text_file, False)
        print("MMMM: ", M)
        alphabet = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        #d 937
        #e = 13


        C = []


        for i in range(len(M)):
            new_M = M[i]
            print("new_M", new_M)
            C.append(str(pow(int(new_M), int(d), int(n))))

        OutputFile.truncate()

        j = 0

        print("C: ", C)

        for i in range(len(C)):
            if(len(C[i]) == 3):
                '''if(int(C[i]) % self.indices[j] == 1):
                    stringthing = "0" + C[i]
                    C[i] = stringthing

                else:
                    stringthing = C[i][0:2] + "0" + C[i][2:3]
                    C[i] = stringthing'''

                stringthing = "0" + C[i]
                C[i] = stringthing

                j += 1

        print("C: ", C)


        for i in range(len(C)):
            #C[i] = helpers.toBase(70, C[i])
            new_plain_text = helpers.justaString(alphabet, C[i])
            print(new_plain_text)
            OutputFile.write(str(new_plain_text).encode("utf-8"))


        new_text = "\n Done in " + str(len(C)) + " Blocks of " + str(self.divides) + " characters."
        OutputFile.write(new_text.encode("utf-8"))

        OutputFile.close()

        return C












