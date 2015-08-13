#!/usr/bin/env python

class Staves:
    """Creates a new Staves object"""
    def __init__(self, inStr):
        self.__string = inStr

    """Finds the longest balanced pair of staves

    This is the master method which is used to call the others.
    It checks all pairs of staves, longest first.
    """  
    def find_longest_balanced_pair(self):
        max_stave_len = len(self.__string) / 2
        for stave_len in xrange(max_stave_len, 0, -1):
            rightmost_stave1_start = len(self.__string) - 2 * stave_len
            for stave1_start in xrange(0, rightmost_stave1_start + 1):
                stave1 = self.__string[stave1_start:stave1_start + stave_len]
                for stave2_start in xrange(stave1_start + stave_len, rightmost_stave1_start + stave_len + 1):
                    stave2 = self.__string[stave2_start:stave2_start + stave_len]
                    if self.__balanced(stave1, stave2):
                        return '%d %d %d' % (stave1_start, stave2_start, stave_len)
        return False

    # Checks whether the pair of staves can be balanced   
    def __balanced(self, stave1, stave2):
        return (self.__layout_is_balanced(stave1, stave2) or
                self.__layout_is_balanced(stave1, stave2[::-1]) or
                self.__layout_is_balanced(stave1[::-1], stave2) or
                self.__layout_is_balanced(stave1[::-1], stave2[::-1]))

    # Checks whether a particular layout of a pair of staves is balanced
    # There are 4 possible layouts per pair: both staves forward, stave 1 forward with stave 2 backward,
    #     stave 1 backward with stave 2 forward, both staves backward
    def __layout_is_balanced(self, stave1, stave2):
        staves = map(int, list(stave1 + stave2))
        regular_sum = sum(staves)    # Sum of masses for each section of staves
        weighted_sum = 0             # Sum of position * mass for each section of staves
        for pos in xrange(0, len(staves)):
            weighted_sum += staves[pos] * (pos + 1)
        center_of_gravity = float(weighted_sum) / regular_sum
        midpoint_position_of_staves = float(len(staves) + 1) / 2
        return center_of_gravity == midpoint_position_of_staves

print Staves(raw_input()).find_longest_balanced_pair()
