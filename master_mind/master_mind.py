#!/usr/bin/env python

""" I'm sorry but seems that this is not the fastest solution, I used a pre-filter in order
    to don't process all the impossible keys at the moment of create the list of possible keys, and
    a two phases filter for all the possible keys ordered by the score of the guesses, but the
    script is still too complex :'( """

import fileinput

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-12-30"

class MasterMind:
    __guesses = None
    __guessLen = None
    __inHiggerInt = 0
    __possibleKeys = []

    def __checkPossibleKeyWithAllKeys(self, inKey):
        for guess in self.__guesses:
            score = 0
            for pos in xrange(0, len(inKey)):
                if guess[pos] == inKey[pos]:
                    score += 1

                if score > guess[len(guess) - 1]:
                    return False

        return True
                

    def __createPossibleKeys(self, inGuess, inScore, inCurrentScore = 0, inCurrentPos = 0, inCurrentKeys = [0]):
        if inCurrentScore > inScore or inCurrentPos > self.__guessLen:
            return

        if len(inCurrentKeys) > self.__guessLen:
            inCurrentKeys.pop()
            if self.__checkPossibleKeyWithAllKeys(inCurrentKeys):
                self.__possibleKeys.append(inCurrentKeys)
            return

        for value in xrange(0, self.__inHiggerInt):
            inCurrentKeys[inCurrentPos] = value

            keys = inCurrentKeys[:]
            keys.append(0)

            self.__createPossibleKeys(inGuess, inScore, inCurrentScore + (int(inCurrentKeys[inCurrentPos] == inGuess[inCurrentPos])), inCurrentPos + 1, keys)

    def __removeImpossibleGuesses(self, inGuess, inScore):
        # print "Guess: %s - Score: %s" % (inGuess, inScore)
        newPossibleKeys = []

        for possibleKey in self.__possibleKeys:
            currentScore = 0
            for pos in xrange(0, self.__guessLen):
                if inGuess[pos] == possibleKey[pos]:
                    currentScore += 1

                if currentScore > inScore:
                    break

            if currentScore == inScore:
                newPossibleKeys.append(possibleKey)

        self.__possibleKeys = newPossibleKeys

    def resolve(self):
        # Create a set with all the possible keys using the guess with the lowest score...
        self.__guesses = sorted(self.__guesses, key = lambda guess: guess[len(guess) - 1])

        firstGuess = self.__guesses[0]
        self.__createPossibleKeys(firstGuess[:-1], firstGuess[len(firstGuess) - 1])

        # print self.__possibleKeys

        # Remove all the impossible keys, do it to times to ensure that all the
        # guesses are checked against all the guesses
        for times in xrange(0, 2):
            for guess in self.__guesses:
                self.__removeImpossibleGuesses(guess[:-1], guess[len(guess) - 1])

        # If we have at least one possible key, return the string "yes"
        if len(self.__possibleKeys) > 0:
            return 'Yes'

        return 'No'

    def __init__(self, inHiggerInt, inGuessLen, inGuesses):
        # print "HiggerGuess: %s GuessLen: %s " % (inHiggerInt, inGuessLen)

        self.__inHiggerInt = inHiggerInt
        self.__guesses = inGuesses
        self.__guessLen = inGuessLen

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    currentLine = 1

    for problemLine in xrange(0, int(lines[0])):
        problemInfo = map(int, lines[currentLine].split())
        guesses = []
        for guess in xrange(0, problemInfo[2]):
            currentLine += 1
            guesses.append(map(int, lines[currentLine].split()))

        print MasterMind(problemInfo[0], problemInfo[1], guesses).resolve()
        currentLine += 1
