# -*- coding: utf-8 -*-
'''
GRASP Solver by Eloy Gil
eloy.gil@est.fib.upc.edu
'''

import copy

class Solution(object):
    def __init__(self, problem):
        self.problem = problem
        self.routes = []

    def isFeasible(self):
        problem = self.problem
        for route in self.routes:
            lastPoint = problem.sourcePoint
            currentTime = 0
            for point in route:
                destTime = currentTime + problem.dist[lastPoint][point]
                if destTime > problem.window[point][1]: return False
                currentTime = max(destTime, problem.window[point][0]) + problem.task[point]
                lastPoint = point
            currentTime += problem.dist[lastPoint][problem.sourcePoint]
            if currentTime > problem.workTime:
                return False
        return True

    def _routeTime(self, route, includeReturn=True):
        problem = self.problem
        lastPoint = problem.sourcePoint
        currentTime = 0
        for point in route:
            currentTime = max(currentTime + problem.dist[lastPoint][point], problem.window[point][0]) + problem.task[point]
            lastPoint = point
        if includeReturn: currentTime += problem.dist[lastPoint][problem.sourcePoint]
        return currentTime

    def lastTruckTime(self):
        problem = self.problem
        maxTime = 0
        for route in self.routes:
            rTime = self._routeTime(route)
            if (maxTime < rTime):
                maxTime = rTime
        return maxTime

    def quality(self):
        nTrucks = len(self.routes)
        maxTime = self.lastTruckTime()
        return nTrucks * self.problem.bigM + maxTime

    def candidateList(self):
        candidates = []
        unassignedPoints = range(0,self.problem.nPoints)
        wTime = self.problem.workTime
        for existingRoute in self.routes:
            for point in existingRoute:
                unassignedPoints.remove(point)
        for unassignedPoint in unassignedPoints:
            for i in range(0, len(self.routes)):
                self.routes[i].append(unassignedPoint)
                if self.isFeasible():
                    rTime = self._routeTime(self.routes[i], False)
                    candidates.append((unassignedPoint,i,rTime))
                self.routes[i].remove(unassignedPoint)
            self.routes.append([unassignedPoint])
            if self.isFeasible():
                rTime = self._routeTime(self.routes[-1], False)
                candidates.append((unassignedPoint,-1,wTime + rTime))
            self.routes.remove([unassignedPoint])
        return candidates

    def assign(self, candidate):
        if candidate[1] == -1:
            self.routes.append([candidate[0]])
        else:
            self.routes[candidate[1]].append(candidate[0])

    def setWorstCase(self):
        for point in range(0, self.problem.nPoints):
            self.routes.append([point])

    def getNeighbours(self):
        neighbours = []
        prevScore = self.quality()
        newSolution = copy.deepcopy(self)

        for i in range(0, len(newSolution.routes)):
            for point in newSolution.routes[i]:
                if len(newSolution.routes[i]) == 1:
                    del newSolution.routes[i]
                else:
                    newSolution.routes[i].remove(point)

                for j in range(0, len(newSolution.routes)):
                    #if i == j: continue
                    for k in range(0, len(newSolution.routes[j]) + 1):
                        newSolution.routes[j].insert(k,point)
                        if newSolution.isFeasible() and prevScore > newSolution.quality():
                            neighbours.append(copy.deepcopy(newSolution))
                        newSolution.routes[j].remove(point)
                newSolution = copy.deepcopy(self)
        return neighbours

    def __str__(self):
        return str(self.routes) + " trucks: " + str(len(self.routes)) + " quality: " + str(self.quality())