import random
from rsa import RSA
import helpers

def generate_key():
    string1 = ""
    for i in range(200):
        letter1 = random.randrange(0, 26)
        string1 += chr(letter1 + 97)

    return string1


def main():

    security_thingy = RSA(5)

    new_input = input("Do you want new keys?")

    if new_input == "yes":

        string1 = generate_key()
        string2 = generate_key()
        print(string1)
        print(string2)
        return

    else:
        string1 = "hcqmbzppsbchobqpvrckniwzxwzfnmykxflstyudaujgciukhjqmepflggpmtdlqpfxztfmkzjzwbglyxondwzqatqwitkcexpmmktlztlfwxhupvgjldrlplhfkjhlywwpwzsykjjlkcqtnitdavrlebbqhtqlyfoxjgrxzkbojiclbmtcrtllefwokolfvvtanmofm"
        string2 = "csrliiqjnkwrgfihaibbwwqftjlwowjtgzhawsvonksbdbglgbrlxcplfwuhjvzbhvlfdlqkzbgnzgjzexwcktokdjpqwydynzoxfjbdyxxgtxahvwyvmaivndrmqylfsdsfdxmdyrrasixfddfalnvbiqvenqwpkrbcoheahxdjnnegmkhorrztigxurzxtcezhosws"









    security_thingy.GenerateKeys(string1, string2)
    security_thingy.Encrypt("input.txt", "output.txt")
    security_thingy.Decrypt("output.txt", "decryptoutput.txt")








if __name__ == '__main__':
    main()



