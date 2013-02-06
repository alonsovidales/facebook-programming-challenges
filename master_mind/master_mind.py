#!/usr/bin/env python

import fileinput, itertools

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-12-30"

class MasterMind:
    __debug = False

    def __checkIfPossibleByPairs(self):
        """ If the score is bigger than the half of the guess len in two of the guesses, they
        should to share at least the score - (guess lengh / 2) elements """
        prevGuess = self.__guesses[0]
        for guess in reversed(self.__guesses):
            if guess[len(guess) - 1] < (self.__guessLen / 2):
                return True

            sharedElems = 0
            for pos in xrange(0, self.__guessLen):
                if guess[pos] == prevGuess[pos]:
                    sharedElems += 1

            if self.__debug:
                print "Shared: %s - Len: %s - Score: %s" % (sharedElems, (self.__guessLen / 2), guess[len(guess) - 1])

            if sharedElems < (guess[len(guess) - 1] - (self.__guessLen / 2)):
                return False

        return True

    def __createPossibleKeys(self, inGuesses):
        possibles = {}
        notPossibles = {}
        keyMembers = {}

        for pos in xrange(0, self.__guessLen):
            possibles[pos] = set()
            notPossibles[pos] = set()

        for guess in inGuesses:
            if self.__debug:
                print "Guess: %s" % (guess)
            remainScore = guess[len(guess) - 1]

            totalNotPos = 0
            for pos in xrange(0, self.__guessLen):
                if guess[pos] in notPossibles[pos]:
                    totalNotPos += 1

            # If the total lenght of the guess minus the not possible number are
            # equal to the score, all the remain numbers are parts of the key
            if (self.__guessLen - totalNotPos) == remainScore:
                for pos in xrange(0, self.__guessLen):
                    if guess[pos] not in notPossibles[pos]:
                        keyMembers[pos] = guess[pos]
            else:
                # All the numbers that we can asset in the key, will decrease the score,
                # and all the number that are not in the key will increase the score, but will
                # nos be considerer in a future
                for pos, value in keyMembers.items():
                    if guess[pos] == value:
                        remainScore -= 1
                    else:
                        remainScore += 1

                if remainScore == 0:
                    for pos in xrange(0, self.__guessLen):
                        notPossibles[pos].add(guess[pos])
                        possibles[pos].discard(guess[pos])
                        if self.__debug:
                            print "Discarted: %s" % (guess[pos])
                else:
                    for pos in xrange(0, self.__guessLen):
                        if (self.__guessLen - pos) == remainScore:
                            if pos not in keyMembers:
                                keyMembers[pos] = guess[pos]
                            remainScore -= 1
                        else:
                            if guess[pos] not in notPossibles[pos]:
                                remainScore -= 1
                                possibles[pos].add(guess[pos])

            if self.__debug:
                print "Key members: %s" % (keyMembers)
                print "Not Possibles: %s" % (notPossibles)
                print "Possibles: %s" % (possibles)

        mainKeys = []
        if len(possibles) > 0:
            for pos in xrange(0, self.__guessLen):
                if pos in keyMembers:
                    mainKeys.append([keyMembers[pos]])
                else:
                    if len(possibles[pos]) == 0:
                        keys = []
                        for count in xrange(1, self.__inHiggerInt + 1):
                            if count not in notPossibles[pos]:
                                keys.append(count)
                        mainKeys.append(keys)
                    else:
                        mainKeys.append(list(possibles[pos]))

        if self.__debug:
            print "Main keys: %s" % (mainKeys)

        possibleKeyValues = []
        for pos in xrange(0, self.__guessLen):
            if pos in keyMembers:
                possibleKeyValues.append([keyMembers[pos]])
            else:
                keys = []
                for count in xrange(1, self.__inHiggerInt + 1):
                    if count not in notPossibles[pos]:
                        keys.append(count)

                possibleKeyValues.append(keys)
                        

        if self.__debug:
            print "Possible keys: %s" % (possibleKeyValues)

        return mainKeys, possibleKeyValues

    def __checkIfPossibleWithGuesses(self, inKey):
        if self.__debug:
            print "Checking:"
            print inKey

        for guess in self.__guesses:
            score = 0
            for pos in xrange(0, self.__guessLen):
                if inKey[pos] == guess[pos]:
                    score += 1

            if score < guess[len(guess) - 1]:
                return False

        return True

    def resolve(self):
        # Create a set with all the possible keys using the guess with the lowest score...
        self.__guesses = sorted(self.__guesses, key = lambda guess: guess[len(guess) - 1])

        # First of all check if is possible comparing the matches between the keys, is
        # the fastest method that can define if is not possible
        if not self.__checkIfPossibleByPairs():
            return "No"

        # Get the posible keys, mainKeys will be the keys with most posibilities to match
        # because of they include all the numbersincluded into the different guesses, and
        # possibleKeys the rest of posible keys with the numbers that can't be discarted
        mainKeys, possibleKeys = self.__createPossibleKeys(self.__guesses)

        # Check the keys with most posibilities
        for key in itertools.product(*mainKeys):
            if self.__checkIfPossibleWithGuesses(key):
                return "Yes"

        # Check the rest, this is the brute force  method :'(
        for key in itertools.product(*possibleKeys):
            if self.__checkIfPossibleWithGuesses(key):
                return "Yes"

        # No key matches, no hope left :'(
        return "No"

    def __init__(self, inHiggerInt, inGuessLen, inGuesses):
        if self.__debug:
            print "HiggerGuess: %s GuessLen: %s " % (inHiggerInt, inGuessLen)

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
