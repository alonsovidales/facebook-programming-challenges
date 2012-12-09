#!/usr/bin/env python

"""
The test case is not corret!!!!!!
Usign the given input:
//dict
hello
there
yello
bob
tom
mabel
says
hi
secret
the
is
to
smile
//secret
45161 01223
x2x 3453 6k
x8z yz67zx 5y x4 y352z

According to the verification system, the output should to be:
there yello
bob says hi
tom secret is to smile

as you can see on the third line we have:
x8z -> tom
and
x4 -> to
The "o" of Tom is an 8 and the "o" of to is an 4

I wasted two hours trying to solve this problem :'(
"""

import fileinput, itertools, collections

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-12-09"

class SecretDecoder:
    __wordsByLen = {}
    __originLinesEnc = []
    __linesEncoded = []

    def __checkIfPossible(self, inLines):
        for linePos in xrange(0, len(inLines)):
            charDict = {}
            for wordPos in xrange(0, len(inLines[linePos])):
                for char in xrange(0, len(self.__originLinesEnc[linePos][wordPos])):
                    if charDict.get(inLines[linePos][wordPos][char], '') == '':
                        charDict[inLines[linePos][wordPos][char]] = self.__originLinesEnc[linePos][wordPos][char]
                    else:
                        if charDict[inLines[linePos][wordPos][char]] != self.__originLinesEnc[linePos][wordPos][char]:
                            return False

        return True

    def __checkByDepp(self, inLines, inCurrentLine = 0, inCurrentWord = 0):
        if self.__checkIfPossible(inLines):
            if len(inLines) == len(self.__originLinesEnc) and len(inLines[len(inLines) - 1]) == len(self.__originLinesEnc[len(inLines) - 1]):
                for line in inLines:
                    print " ".join(line)
                exit()

            for possibleWord in self.__wordsByLen[len(self.__originLinesEnc[inCurrentLine][inCurrentWord])]:
                try:
                    inLines[inCurrentLine][inCurrentWord] = possibleWord
                except:
                    try:
                        inLines[inCurrentLine].insert(inCurrentWord, possibleWord)
                    except:
                        inLines.append([possibleWord])

                if len(self.__originLinesEnc[inCurrentLine]) == (inCurrentWord + 1):
                    self.__checkByDepp(inLines, inCurrentLine + 1, 0)
                else:
                    self.__checkByDepp(inLines, inCurrentLine, inCurrentWord + 1)

    def resolve(self):
        self.__checkByDepp([])

        return ""

    def __init__(self, inInputLines):
        readingSecrets = False
        for line in inInputLines[1:]:
            if line == '//secret':
                readingSecrets = True
            else:
                if readingSecrets:
                    self.__linesEncoded.append(line.split())
                    self.__originLinesEnc.append(line.split())
                else:
                    if self.__wordsByLen.get(len(line), False) == False:
                        self.__wordsByLen[len(line)] = [line]
                    else:
                        self.__wordsByLen[len(line)].append(line)

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    print SecretDecoder(lines).resolve()
