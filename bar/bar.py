#!/usr/bin/env python

import fileinput

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-12-09"

class GroupObjects:
    __debug = False

    def __checkIfPossible(self, inNumber, inGroupPos):
        """
        Returns true if the given number on the given group can be positioned on
        the self.__position position.
        This method compares the number against all the groups O(n - 1) where n is
        the number of groups

        @param inNumber int The number to be compared
        @param inGroupPos int The position of the group who contains the number
        """

        maxPos = 0
        minPos = 0

        for groupPos in xrange(0, len(self.__groups)):
            if inGroupPos <> groupPos:
                if self.__debug:
                    print "Group: %s Number: %s Comparing Group: %s Comp Num: %s" % (
                        inGroupPos,
                        inNumber,
                        groupPos,
                        self.__groups[groupPos][0])

                # Check if the compared group contain a number smaller than the current
                # number, then we can use it to increase the possible position
                if self.__groups[groupPos][0] <= inNumber:
                    minPos += 1
                    if self.__debug:
                        print "Inc Pos"

                # Check if the bigger number of the current group is smaller than the
                # current one, then the player will play always a number who will move
                # the current number one position
                if self.__groups[groupPos][len(self.__groups[groupPos]) - 1] < inNumber:
                    maxPos += 1

        # Check if the number can be included into the numbers on the whised position
        if minPos >= (self.__position - 1) and maxPos <= (self.__position - 1):
            if self.__debug:
                print "Found: %s" % (inNumber)
            return True

        return False

    def resolve(self):
        """
        @return int the number of all the numbers that can fit on the given position
        """
        possibleSolutions = set()

        # Check all the numbers against all the groups in order to determinate all the
        # possible positions for the number number, each number will be compared against
        # the biggest and smallest numbers of each group, then O(n * m) where n is the
        # number of numbers, and m the number of groups
        for groupPos in xrange(0, len(self.__groups)):
            for number in self.__groups[groupPos]:
                if number not in possibleSolutions:
                    if self.__checkIfPossible(number, groupPos):
                        possibleSolutions.add(number)
                        if self.__debug:
                            print "Comparing: %s" % (number)
                    

        if self.__debug:
            print "Solutions: %s" % (sorted(possibleSolutions))

        return len(possibleSolutions)

    def __init__(self, inPosition, inPositions):
        # Get all the groups, ans sort the numbers for each group, removing the first one,
        # that is the number of numbers
        self.__groups = [sorted(map(int, numbers.split()[1:])) for numbers in inPositions]
        self.__position = inPosition

        if self.__debug:
            print "Position: %s Groups: %s" % (self.__position, self.__groups) 

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    currentLine = 1
    for problem in xrange(0, int(lines[0])):
        problemInfo = map(int, lines[currentLine].split())
        print GroupObjects(
            problemInfo[1],
            lines[currentLine + 1:currentLine + 1 + problemInfo[0]]).resolve()

        currentLine += problemInfo[0] + 1
