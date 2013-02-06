#!/usr/bin/env python

import fileinput

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-01-13"

class SecretDecoder:
    __debug = False

    def __checkIfPossibleLine(self, inOriginal, inLine):
        """
        This method returns true if the inLine is a possible combination compared with
        the inOringinal line words by words and char by char or false if is not a possible combination

        @return bool True if is possible, False if not
        """
        if self.__debug:
            print "Check if possible: %s" % (inLine)

        charDict = {}
        intDict = {}
        # Check char by char all the words
        for wordPos in xrange(0, len(inLine)):
            for charPos in xrange(0, len(inLine[wordPos])):
                # Use a dictionary in order to know if the character was previously setted, and
                # if it was, check if the replacement matches
                if charDict.get(inLine[wordPos][charPos], '') == '':
                    charDict[inLine[wordPos][charPos]] = inOriginal[wordPos][charPos]
                else:
                    if charDict[inLine[wordPos][charPos]] != inOriginal[wordPos][charPos]:
                        if self.__debug:
                            print "No possible"

                        return False

                # Use a dictionary in order to know if the character was previously setted, and
                # if it was, check if the replacement matches
                if intDict.get(inOriginal[wordPos][charPos], '') == '':
                    intDict[inOriginal[wordPos][charPos]] = inLine[wordPos][charPos]
                else:
                    if intDict[inOriginal[wordPos][charPos]] != inLine[wordPos][charPos]:
                        if self.__debug:
                            print "No possible"

                        return False

        if self.__debug:
            print "Possible"

        return True

    def __checkByDepp(self, inOriginalLine, inLine = [], inCurrentWord = 0):
        """
        Recursive search, check all the posible combinations for the given line as a string with
        the necessary format to be printed
        """
        if self.__debug:
            print "Checking: %s - %s" % (inOriginalLine, inLine)

        if self.__checkIfPossibleLine(inOriginalLine, inLine):
            # If the line is possible, and the number of words are the same, we have a
            # line, return it, this will stop the recursivity :)
            if len(inOriginalLine) == len(inLine):
                return "%s = %s" % (' '.join(inOriginalLine), ' '.join(inLine))

            # Check all the words with the same lenght that the number of encrypted characters have
            for word in self.__wordsByLen[len(inOriginalLine[inCurrentWord])]:
                newLine = inLine[:]
                newLine.append(word)
                solution = self.__checkByDepp(inOriginalLine, newLine, inCurrentWord + 1)
                if solution <> False:
                    return solution

        return False

    def resolve(self):
        """
        This method launches the recursive serach of the correct combination and returns as string the text
        decoded if possible, with the necessary format given by the specifications

        @return str The text decoded and formatted
        """
        decrypted = []
        for line in self.__linesEncoded:
            decrypted.append(self.__checkByDepp(line))

        return '\n'.join(decrypted)

    def __init__(self, inInputLines):
        # Will contain the original lines encoded as lists of words
        self.__linesEncoded = []
        # This dictionary will be used to store all the possible words sorted by length in order to
        # do as fast as possible the replacement
        self.__wordsByLen = {}

        readingSecrets = False

        # Parse the input lines and prepare the dictionary of words by length, the lists with the encoded
        # lines, and the list with the possible words to be used
        for line in inInputLines[1:]:
            if line == '//secret':
                readingSecrets = True
            else:
                if readingSecrets:
                    self.__linesEncoded.append(line.split())
                else:
                    if self.__wordsByLen.get(len(line), False) == False:
                        self.__wordsByLen[len(line)] = [line]
                    else:
                        self.__wordsByLen[len(line)].append(line)

        if self.__debug:
            print "Encoded: %s" % (self.__linesEncoded)
            print "Words by len: %s" % (self.__wordsByLen)

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    print SecretDecoder(lines).resolve()
