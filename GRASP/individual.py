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
        ind.chromosomes = [[round(random.random(),2) for e in range(0,problem.nPoints)] for e in range(0,problem.nPoints)]
        return ind

    def createCrossover(vip,pleb):
        problem = ind1.problem
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
                if(pInheritance < pInheritanceElite):
                    gene = vipGene
                else:
                    gene = plebGene

                ind.chromosomes[numChromosome][numGene] = copy.deepcopy(gene)
                

        
        # instantiate the new Individual with chromosome and an undefined fitness
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
            best = min(CL, key=lambda c: c[2] * self.chromosomes[c[0]][c[1]])
            self.solution.assign(best)
            CL = self.solution.candidateList()

        self.fitness = self.solution.quality()

    def getFitness(self):
        if self.solution == None: self.decode()
        return self.fitness


from problem import Problem

problem = Problem()
problem.load(sys.argv[1])

ind1 = Individual.createMutant(problem)
#ind1.chromosomes = [[1.0] * problem.nPoints] * problem.nPoints
print ind1.chromosomes
print

ind2 = Individual.createMutant(problem)
#ind2.chromosomes = [[0.0] * problem.nPoints] * problem.nPoints
print ind2.chromosomes
print

cross = Individual.createCrossover(ind1,ind2)
print cross.chromosomes