# -*- coding: utf-8 -*-
'''
GRASP Solver by Eloy Gil
eloy.gil@est.fib.upc.edu
'''

# argv[1]: path to instance (ex. '../InstanceGen/instance_6.dat')
# argv[2]: time (in seconds) to work

from problem import Problem
from solution import Solution
import time, sys, random, os

alpha = 0.4

def fileCheck(inst_path):
    if os.path.isfile(inst_path):
        print 'Using instance ' + inst_path.split('/')[-1]
    else:
        print 'File ' + inst_path + " not found. Aborting."
        exit()

def construct(alpha, problem):
    solution = Solution(problem)
    CL = solution.candidateList()
    while len(CL) > 0:
        CL = sorted(CL, key=lambda candidate: candidate[2])
        minCandidate = CL[0][2]
        maxCandidate = CL[-1][2]
        threshold = minCandidate + alpha * (maxCandidate - minCandidate)
        RCL = [x for x in CL if x[2] <= threshold]
        theChosenOne = random.choice(RCL)
        solution.assign(theChosenOne)
        CL = solution.candidateList()
        #print CL, minCandidate, maxCandidate, threshold, RCL
    #print "Solution: ", solution.assignments
    return solution

def local(solution):
    #print "*" * 100
    bestNeighbour = solution
    H = solution.getNeighbours()
    while len(H) > 0:
        #bestNeighbour = min(H, key=lambda s: s.quality())

        quality = float('infinity')
        #print H
        for n in H:
            if n.quality() < quality:
                quality = n.quality()
                bestNeighbour = n

        #print bestNeighbour
        H = bestNeighbour.getNeighbours()
    return bestNeighbour


# Checks that the path to the file exists
fileCheck(sys.argv[1])

# Loads the instance
problem = Problem()
problem.load(sys.argv[1])

# Initialize time
startTime = time.time()

# Initialize final solution
finalSolution = Solution(problem)
finalSolution.setWorstCase()

# Initialize solution

print "Initial solution:", finalSolution.routes, "with quality:", finalSolution.quality()

while time.time() - startTime < float(sys.argv[2]):
    CURSOR_UP_ONE = '\033[F'
    ERASE_LINE = '\033[K'
    print(CURSOR_UP_ONE + ERASE_LINE)
    print round(((time.time() - startTime) * 100) / float(sys.argv[2]), 2), '%'
    solution = construct(alpha, problem)
    solution = local(solution)
    if solution.quality() < finalSolution.quality():
        finalSolution = solution
print "Instance executed for ", sys.argv[2], "seconds."
print "Final solution: ", finalSolution

#problem  = Problem()
#solution = Solution(problem)
#print(solution.quality())