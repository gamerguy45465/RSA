import math

def first_set(N):
    set_one = []
    for i in range(N):
        set_one.append(i)

    return set_one

def manipulate(A):
    permutations = [format(A)]
    i = 0
    while (i < (math.factorial(len(A)) - 1)):
        n = len(A) - 1
        j = n - 1

        while A[j] > A[j + 1]:
            j = j - 1

        k = n

        while A[j] > A[k]:
            k = k - 1

        A[j], A[k] = A[k], A[j]

        r = n

        s = j + 1

        while (r > s):
            A[r], A[s] = A[s], A[r]
            r = r - 1
            s = s + 1
        permutations.append(format(A))

        i += 1

    return permutations

def format(A):
    string = ""
    for element in A:
        string += str(element)


    return string




def generate(set):
    final_result = manipulate(set)
    string = ""
    for e in final_result:
        string += str(e) + " "


    print(string)





def permutations(N):
    set = first_set(N)
    generate(set)



def main():
    print("Welcome to permutation generator")
    N = 15

    while(N > 10):
        N = int(input("Please enter an amount for N"))


    permutations(N)






if __name__ == '__main__':
    main()


