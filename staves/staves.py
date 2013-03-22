#!/usr/bin/env python

import itertools

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-03-21"

class Staves:
    __debug = False

    def __checkWighted(self, inStr1, inStr2):
        stavesInt = map(int, list(inStr1 + inStr2))

        regularSum = sum(stavesInt)

        weigthedSum = 0
        for pos in xrange(0, len(stavesInt)):
            weigthedSum += stavesInt[pos] * (pos + 1)

        return (float(weigthedSum) / regularSum) == (float(len(stavesInt) + 1) / 2)

    def __checkPossible(self, inStr1, inStr2):
        return len(self.__string.replace(inStr1, '').replace(inStr2, '')) == (len(self.__string) - len(inStr1) - len(inStr2))

    def resolve(self):
        stavesByLen = {}

        for count in xrange(0, len(self.__string)):
            for subStrLen in xrange(0, len(self.__string) - count):
                stave = self.__string[count:count + subStrLen + 1]
                if len(stave) in stavesByLen:
                    stavesByLen[len(stave)].append(stave)
                else:
                    stavesByLen[len(stave)] = [stave]

        if self.__debug:
            print stavesByLen

        for length in sorted(stavesByLen.keys(), reverse = True):
            for combination in itertools.combinations(stavesByLen[length], 2):
                if self.__checkPossible(combination[0], combination[1]):
                    if (
                        (self.__checkWighted(combination[0], combination[1])) or
                        (self.__checkWighted(combination[0][::-1], combination[1])) or
                        (self.__checkWighted(combination[0], combination[1][::-1])) or
                        (self.__checkWighted(combination[0][::-1], combination[1][::-1]))):

                        return "%d %d %d" % (
                            self.__string.find(combination[0]),
                            self.__string.find(combination[1]),
                            len(combination[0]))

        return False

    def __init__(self, inStr):
        self.__string = inStr

print Staves(raw_input()).resolve()
