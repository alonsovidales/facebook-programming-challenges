#!/usr/bin/env python

import fileinput

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-03-22"

class Game:
    __debug = False
    __number = None

    def __removeMaxPossible(self, inNumber):
        """
        This method removes the maximun number satisfying the n-2^k constraint

        @return int The number after remove the max number as an integer
        @return bool False if is not possible to remove any number
        """
        # Get the number in binary and remove the "0b" prefix
        binNumber = bin(inNumber)[2:]
        # The first zero will determinate the first max number than can be removed keeping the same number of '1'
        # and complaining with the n-2^k constraint
        firstZeroPos = binNumber.find('0')

        # If we don't have zeros, we can remove anithing keeping the same number of '1' :'(
        if firstZeroPos == -1:
            return False

        if self.__debug:
            print "N: %d" % (inNumber)
            print "To Remove: 1%s" % ('0' * (len(binNumber) - firstZeroPos - 1))
            print inNumber - int("1%s" % ('0' * (len(binNumber) - firstZeroPos - 1)), 2)
            print bin(inNumber - int("1%s" % ('0' * (len(binNumber) - firstZeroPos - 1)), 2))[2:]

        return inNumber - int("1%s" % ('0' * (len(binNumber) - firstZeroPos - 1)), 2)

    def resolve(self):
        """
        @return str The player who will win the game
        """
        firstWin = False
        # Substract numbers until have a number that can't be reduced (withouth any zero on it)
        n = self.__removeMaxPossible(self.__number)
        while n != False:
            firstWin = not firstWin
            n = self.__removeMaxPossible(n)

        if firstWin:
            return "First Player"

        return "Second Player"

    def __init__(self, inNumber):
        self.__number = inNumber

        if self.__debug:
            print "Number: %s" % (bin(inNumber)[2:])

if __name__ == "__main__":
    lines = map(int, [line.replace('\n', '') for line in fileinput.input()])

    for number in lines[1:]:
        print Game(number).resolve()
