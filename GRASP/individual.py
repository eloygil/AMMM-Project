# -*- coding: utf-8 -*-
'''
GRASP Solver by Eloy Gil
eloy.gil@est.fib.upc.edu
'''

from solution import Solution
import copy, sys, random

class Individual(object):

    @staticmethod
    def createMutant(problem):
        ind = Individual(problem)
        ind.chromosomes = [[random.random() for e in range(0,problem.nPoints)] for e in range(0,problem.nPoints)]
        return ind

    @staticmethod
    def createCrossOver(vip,pleb):
        problem = vip.problem
        numGenes = problem.nPoints
        numChromosomes = problem.nPoints
        pInheritanceElite = problem.pInheritanceElite
        ind = Individual(problem)
        for numChromosome in range(0, numChromosomes):
            for numGene in range(0, numGenes):
                # pick genes from parents
                vipGene = vip.chromosomes[numChromosome][numGene]
                plebGene = pleb.chromosomes[numChromosome][numGene]
                # pick the gene from elite or non-elite
                # pInheritanceElite: probability of picking the gene from the elite parent
                pInheritance = random.uniform(0.0, 1.0);
                if pInheritance < pInheritanceElite:
                    gene = vipGene
                else:
                    gene = plebGene
                ind.chromosomes[numChromosome][numGene] = gene
        return ind

    def __init__(self, problem):
        self.problem = problem
        self.chromosomes = []
        for i in xrange(0,problem.nPoints):
            self.chromosomes.append([1.0] * problem.nPoints)
        self.solution = None
        self.fitness = float('infinity')

    def decode(self):
        problem = self.problem
        self.solution = Solution(problem)
        
        CL = self.solution.candidateList()
        while len(CL) > 0:
            nextTruck = len(self.solution.routes)
            for c in CL: 
                c = (c[0], c[1], c[2] if c[2] >= 0 else nextTruck)
            best = min(CL, key=lambda c: c[2] * self.chromosomes[c[0]][c[1]])
            self.solution.assign(best)
            CL = self.solution.candidateList()

        self.fitness = self.solution.quality()

    def getFitness(self):
        if self.solution == None: self.decode()
        return self.fitness

    def __str__(self):
        return str(self.solution)