#!/usr/bin/env python

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-03-21"

class UniqueSubstrings:
    def resolve(self):
        # Will contain all the possible substrings
        substrings = set()

        # Get all the possible substrings from the main string
        for count in xrange(0, len(self.string)):
            for subStrLen in xrange(0, len(self.string) - count):
                substrings.add(self.string[count:count + subStrLen + 1])

        return len(substrings)

    def __init__(self, inStr):
        self.string = inStr

print UniqueSubstrings(raw_input()).resolve()
