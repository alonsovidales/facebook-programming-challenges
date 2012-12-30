#!/usr/bin/env python

import fileinput

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-12-09"

class BarProblem:
    __numbersByPlayes = []
    __position = None
    __possibleNumbers = set()

    def __recursiveSearch(self, inPlayers, inCombination = []):
        if len(self.__numbersByPlayes) == len(inCombination):
            print sorted(inCombination)
            numberToAdd = sorted(inCombination)[self.__position - 1]
            self.__possibleNumbers.add(numberToAdd)

            for player in self.__numbersByPlayes:
                player.discard(numberToAdd)
        else:
            for playerPos in xrange(0, len(inPlayers)):
                try:
                    for number in inPlayers[playerPos]:
                        auxComb = inCombination[:]
                        auxComb.append(number)
                        self.__recursiveSearch(inPlayers[playerPos + 1:], auxComb)
                except:
                    print "MODIF"
                    self.__recursiveSearch(inPlayers[playerPos:], auxComb)

    def resolve(self):
        self.__recursiveSearch(self.__numbersByPlayes)
        return len(self.__possibleNumbers)

    def __init__(self, inPosition, inPlayerNumbers):
        self.__numbersByPlayes = []
        totalNums = set()
        for player in inPlayerNumbers:
            totalNums = totalNums | set(map(int, player.split()[1:]))
            self.__numbersByPlayes.append(set(map(int, player.split()[1:])))

        self.__position = inPosition
        print self.__position
        print self.__numbersByPlayes

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    linePos = 1
    while linePos < len(lines):
        problemInfo = map(int, lines[linePos].split())
        linesOnProblem = problemInfo[0]
        print BarProblem(problemInfo[1], lines[linePos + 1:linesOnProblem + linePos + 1]).resolve()
        linePos += linesOnProblem + 1
