import permutation as pm
import math as md
'''
Consider the problem of several students planning a holiday gift exchange. Everyone will give one gift to a randomly 
selected student in the group. In great anticipation, all participating students place their names in a hat, then shake it up. 
One by one, each student pulls out the name of the person he/she is assigned to. All is well until everyone hears the blood curdling cry of, 
"Jeepers, I've got my own name!"

What is the probability (0 to 1) that all goes well and no-one selects their own name if there are N students, where N ranges from 2 through 10? 

Sometimes it's very difficult to solve a problem mathematically, and writing a computer simulation is much easier. 
Solve this problem by writing a program that uses your Permutation Generator to count how many are Wins, and divides this by Total. 
Do this in a loop for ALL numbers from 2 through 10.

Based on that data, where do you think that this probability goes as N approaches infinity? Does it go to zero, one, 
or some specific number? If some specific number, identify that number in a google search and tell me what it is.

Example output for N being 2 and 3:

2.  1 of 2 permutations are wins. Probability is 0.50
3.  2 of 6 permutations are wins. Percent is 0.333333333333336

etc.

Submit:
Pass off in person, and submit your code.
'''

def Matches(permutation):
    isTrue = False

    for i in range(len(permutation)):
        if(int(permutation[i]) == i):
            isTrue = True
            break

    return isTrue


def Probability(E, N):
    return (1 - E/N)

def main():
    i = 2

    while(i <= 10):
        set = pm.permutations(i)

        wins = 0

        for j in range(len(set)):
            match = Matches(set[j])
            if(match):
                wins += 1

        if(wins == 0):
            wins = 1


        print(wins, "of", m.factorial(i), "permutations are wins. Probability is", Probability(wins, m.factorial(i)))



        i += 1




if __name__ == '__main__':
    main()

