"""
Cows & Bulls

Created on Thu Jan 12 22:39:31 2017

@author: Martin Smira
"""

import random

# Options
secretNumLen = 4
secretNumMaxNum = 10


introMsg = "Hi Engeto!\n\
I've generated a random {} digit number (ranging from 0 to {}) for you.\n\
Let's play a bulls and cows game.\n"\
.format(str(secretNumLen), str(secretNumMaxNum))

print(introMsg)

secretNum = random.sample(range(secretNumMaxNum), secretNumLen)

round = 0
while True:

    repeatEntry = False

    while True:
        guessInput = input("{}nter a {}-digit number:  ".format(
                           "Re-e" if repeatEntry else "E", secretNumLen))

        guess = list(map(int, guessInput))
        guessLen = len(guess)
        guessUniqueLen = len(set(guess))

        if guessLen != secretNumLen:
            print("Error: You entered a wrong number of digits!")
            repeatEntry = True
        elif guessUniqueLen != secretNumLen:
            print("Error: Use each digit only once!")
            repeatEntry = True
        else:
            repeatEntry = False
            break

    round += 1

    bull = [False] * secretNumLen
    cow = [False] * secretNumLen
    for i in range(secretNumLen):
        bull[i] = secretNum[i] == guess[i]
        cow[i] = secretNum[i] in guess

    nBulls = sum(bull)
    nCows = sum(cow) - sum(bull)

    if nBulls == secretNumLen:

        if round < 4:
            verbalRating = "just lucky"
        elif round < 7:
            verbalRating = "amazing"
        elif round < 9:
            verbalRating = "pretty good"
        elif round < 11:
            verbalRating = "allright"
        elif round < 13:
            verbalRating = "so baad"
        elif round >= 13:
            verbalRating = "... You just suck at this"

        print("Correct, you've guessed the right number in {} guesses!"
              .format(round))
        print("That's {}".format(verbalRating))

        break

    else:
        bull_s = "s" if nBulls != 1 else ""
        cow_s = "s" if nCows != 1 else ""

        print("You hit {} bull{}, {} cow{}"
              .format(nBulls, bull_s, nCows, cow_s))
