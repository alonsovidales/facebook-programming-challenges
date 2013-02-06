#!/usr/bin/env python

""" I didn't test this solution against the Facebook validator, I was interrupted when I was doing it :'( """

import fileinput, math

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-12-09"

class ReversePolishNotation:
    __debug = False

    def __calcMaxNumOfOps(self):
        replace = 0
        stackLength = 0
        for count in xrange(0, len(self.__input)):
            if self.__input[count] == 'x':
                stackLength += 1
            else:
                # We have an operator, and nothing to work with
                # We can, remove the operator or replace it in order to
                # avoid problems with future operators, we replace it,
                # this is only to get an aproximation of the max num of ops
                if stackLength <= 1:
                    stackLength += 1
                    replace += 1
                else:
                    stackLength -= 1

        self.__maxNumOfOps = int(replace + math.floor((stackLength - 1) / 2) + ((stackLength - 1) % 2))

    def __isValid(self, operation):
        stackLength = 0
        for count in xrange(0, len(operation)):
            if operation[count] != '-':
                if operation[count] == 'x':
                    stackLength += 1
                else:
                    if stackLength < 1:
                        return False
                    else:
                        stackLength -= 1

        return stackLength == 1

    def __resolveByDeep(self, operation, currentPos = 0, currentOps = 0):
        # Check if the current operation is valid, in this case, we can set
        # the max numbre of ops to the current number of ops
        if self.__isValid(operation):
            if self.__debug:
                print "Valid: %s - %s" % (currentOps, operation)
            self.__maxNumOfOps = currentOps

        # Check if this is not a valid way, or the number os current ops are
        # bigger than another best option
        if currentOps >= self.__maxNumOfOps or currentPos >= len(operation):
            if self.__debug:
                print operation
                print "returning -1 Operation: %s Max Operations: %s ..." % (currentOps, self.__maxNumOfOps)
            return -1

        self.__resolveByDeep(operation, currentPos + 1, currentOps)

        # Try adding an x
        newOperation = operation[:]
        newOperation.insert(currentPos, 'x')
        self.__resolveByDeep(newOperation, currentPos + 2, currentOps + 1)

        # Try adding an *
        newOperation = operation[:]
        newOperation.insert(currentPos, '*')
        self.__resolveByDeep(newOperation, currentPos + 2, currentOps + 1)

        # Try Removing the char (replace by -)
        newOperation = operation[:]
        newOperation[currentPos] = '-'
        self.__resolveByDeep(newOperation, currentPos + 1, currentOps + 1)

        # Try replacing the character by the opposite
        newOperation = operation[:]
        if newOperation[currentPos] == '*':
            newOperation[currentPos] = 'x'
        else:
            newOperation[currentPos] = '*'
        self.__resolveByDeep(newOperation, currentPos + 1, currentOps + 1)

    def resolve(self):
        self.__calcMaxNumOfOps()
        self.__resolveByDeep(self.__input)
        return self.__maxNumOfOps

    def __init__(self, inProblem):
        self.__input = list(inProblem)
        self.__maxNumOfOps = None

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    for problem in xrange(1, int(lines[0]) + 1):
        print ReversePolishNotation(lines[problem]).resolve()
