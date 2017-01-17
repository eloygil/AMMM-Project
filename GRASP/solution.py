# -*- coding: utf-8 -*-
'''
GRASP Solver by Eloy Gil
eloy.gil@est.fib.upc.edu
'''

class Solution(object):
    def __init__(self, problem):
        self.problem = problem
        self.assignments = [[5, 2, 1], [4, 3, 0]]  # probablemente será una lista de listas (cada asignación de cada camión)
        #self.lastArrival = float('-infinity')
        self.assignments = []
        self.feasible = True

    def isFeasible(self):
        problem = self.problem
        for route in self.assignments:
            lastPoint = problem.sourcePoint
            currentTime = 0
            for point in route:
                destTime = currentTime + problem.dist[lastPoint][point]
                print destTime, problem.window[point][1]
                if destTime > problem.window[point][1]: return False
                currentTime = max(destTime, problem.window[point][0]) + problem.task[point]
                lastPoint = point
            currentTime += problem.dist[lastPoint][problem.sourcePoint]
            if currentTime > problem.workTime:
                return False
        return True

    def _routeTime(self,route,includeReturn=True):
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
        for route in self.assignments:
            rTime = self._routeTime(route)
            if (maxTime < rTime):
                maxTime = rTime
        return maxTime

    def quality(self):
        nTrucks = len(self.assignments)
        maxTime = self.lastTruckTime()
        return nTrucks * self.problem.bigM + maxTime

    def candidateList(self):
        candidates = []
        unassignedPoints = range(0,self.problem.nPoints)
        wTime = self.problem.workTime
        for existingRoute in self.assignments:
            for point in existingRoute:
                unassignedPoints.remove(point)
        for unassignedPoint in unassignedPoints:
            for i in range(0, len(self.assignments)):
                self.assignments[i].append(unassignedPoint)
                print self.assignments
                if self.isFeasible():
                    rTime = self._routeTime(self.assignments[i],False)
                    candidates.append((unassignedPoint,i,rTime))
                self.assignments[i].remove(unassignedPoint)
            self.assignments.append([unassignedPoint])
            if self.isFeasible():
                rTime = self._routeTime(self.assignments[-1],False)
                candidates.append((unassignedPoint,-1,wTime + rTime))
            self.assignments.remove([unassignedPoint])
        return candidates

    def assign(self, candidate):
        if candidate[1] == -1:
            self.assignments.append([candidate[0]])
        else:
            self.assignments[candidate[1]].append(candidate[0])