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
        print CL, minCandidate, maxCandidate, threshold, RCL
    print "Solution: ", solution.assignments

fileCheck(sys.argv[1])
startTime = time.time()
problem = Problem()
problem.load(sys.argv[1])
#solution = Solution(problem)
#construct(0.4, problem)
#print solution.isFeasible()
print
while time.time() - startTime < float(sys.argv[2]):
    test = 1
    # test
print "pos oc. Done."

#problem  = Problem()
#solution = Solution(problem)
#print(solution.quality())