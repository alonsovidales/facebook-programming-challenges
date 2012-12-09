#!/usr/bin/env python

import fileinput, itertools, collections

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2012-12-09"

class GroupObjects:
    __positions = None
    __problemInfo = None

    def __calcDistances(self, inPositions):
        """ Will return the smallest distance between all the objects on the group,
        and a distionary with the distances as key, and the pair of items as values """
        distances = {}
        totalDist = 0
        for positions in itertools.combinations(inPositions, 2):
            dist = abs(positions[1] - positions[0])
            totalDist += dist
            if distances.get(dist, '') != '':
                distances[dist].append((positions[1], positions[0]))
            else:
                distances[dist] = [((positions[1], positions[0]))]

        return (totalDist, distances)

    def resolve(self):
        distancesTotal = 0
        while len(self.__positions) > self.__problemInfo['groups']:
            # Get the total distance and the doctionary to know which is the better item to be removed
            totalDistance, distDict = self.__calcDistances(self.__positions)
            minDistance = sorted(distDict.keys())[0]
            distancesTotal += minDistance
            minDistItemsPairs = distDict[minDistance]

            # Check each pair in order to know the best fit, the best one will be the pair of items
            # to be removed that will give the smallest distance between all the objects on the group
            for itemPair in minDistItemsPairs:
                auxPos = self.__positions.copy()
                auxPos.remove(itemPair[0])
                removeFirstDist, distances = self.__calcDistances(auxPos)

                auxPos = self.__positions.copy()
                auxPos.remove(itemPair[1])
                removeSecDist, distances = self.__calcDistances(auxPos)

                # Check wich is the element that can be removed obtainin a set of elements with the
                # smallest distance possible, and remove this item
                if removeFirstDist > removeSecDist:
                    self.__positions.remove(itemPair[1])
                else:
                    self.__positions.remove(itemPair[0])

        return distancesTotal

    def __init__(self, inProblemInfo, inPositions):
        problemInfo = map(int, inProblemInfo.split())
        self.__problemInfo = {
            "objects": problemInfo[0],
            "groups": problemInfo[1]}
        self.__positions = set(map(int, inPositions.split()))
        #print "Problem: %s Positions: %s" % (self.__problemInfo, self.__positions) 

if __name__ == "__main__":
    lines = [line.replace('\n', '') for line in fileinput.input()]

    for problem in xrange(0, int(lines[0])):
        print GroupObjects(lines[(problem * 2) + 1], lines[(problem * 2) + 2]).resolve()
