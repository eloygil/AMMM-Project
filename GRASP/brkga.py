
from problem import Problem
from solution import Solution
from individual import Individual
import time, sys, random, os

verbose = False

def initializeIndividuals(problem):
        # create a population with numIndividuals individuals created at random
        population = []
        
        individual = Individual(problem)
        population.append(individual)
        
        for numIndividual in xrange(1, problem.numIndividuals):
            individual = Individual.createMutant(problem)
            population.append(individual)

        return population

def sortIndividuals(population):
    # sort individuals in a population by their fitness in ascending order
    population.sort(key=lambda individual: individual.getFitness())

def evolveIndividuals(population, problem):
    numElites = problem.numElites
    
    # get elites and non-elites from current population
    elites = population[0:numElites]            # elites: sublist from 0 to (numElites-1)
    nonElites = population[numElites:]          # nonElites: sublist from numElites to the end

    newPopulation = []
    
    # direct copy the numElites elite individuals to the new population
    newPopulation[0:numElites] = elites
    
    # create numCrossOvers individuals by crossing randomly selected parents
    for numCrossOver in xrange(0, problem.numCrossOvers):
        elite = random.choice(elites)           # pick an elite individual at random
        nonElite = random.choice(nonElites)     # pick a non-elite individual at random
        
        # crossover them parents (elite and non-elite) to produce a new individual
        # pick each gene from elite or non-elite with a specific inheritance probability 
        individual = Individual.createCrossOver(elite, nonElite)
        newPopulation.append(individual)
    
    # create numMutants individuals are created at random
    for numMutant in xrange(0, problem.numMutants):
        individual = Individual.createMutant(problem)
        newPopulation.append(individual)
    
    return newPopulation

problem = Problem()
problem.load(sys.argv[1])

bestSolution = Solution(problem)
bestSolution.setWorstCase()
bestFitness = bestSolution.quality()

# pre-compute number of elite, crossover and mutants in the population
problem.numElites = int(round(problem.pElites * problem.numIndividuals))
problem.numMutants = int(round(problem.pMutants * problem.numIndividuals))
problem.numCrossOvers = problem.numIndividuals - problem.numElites - problem.numMutants

population = initializeIndividuals(problem)
startTime = time.time()
print sys.argv
generation = 0
while time.time() - startTime < float(sys.argv[2]):
    generation += 1
    
    # sort them by their fitness
    sortIndividuals(population)
    
    # update statistics
    bestIndividual = population[0]
    newBestFitness = bestIndividual.getFitness()
    if newBestFitness < bestFitness:
        bestSolution = bestIndividual.solution
        bestFitness = newBestFitness
        if verbose: print "BF: ", bestFitness
    if verbose: print bestIndividual.solution
    
    # evolve the population
    population = evolveIndividuals(population, problem)

print bestSolution, generation

