# -*- coding: utf-8 -*-
'''
GRASP Solver by Eloy Gil
eloy.gil@est.fib.upc.edu
'''

from problem import Problem
from solution import Solution
import time, sys, random

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
        print CL, minCandidate, maxCandidate, threshold, RCL
    print "Solution: ", solution.assignments

startTime = time.time()
problem  = Problem()
solution = Solution(problem)
construct(0.4, problem)
#print solution.isFeasible()
print
while time.time() - startTime < float(sys.argv[1]):
    test = 1
    # test
print "pos oc. Done."

#problem  = Problem()
#solution = Solution(problem)
#print(solution.quality())