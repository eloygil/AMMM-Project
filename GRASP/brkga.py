
from problem import Problem
from solution import Solution
from individual import Individual
import time, sys, random, os

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

# get number of individuals and number of genes per chromosome
#problem.numGenes = decoder.getNumGenes()
#problem.numIndividuals = int(round(decoder.getNumIndividuals()))

# pre-compute number of elite, crossover and mutants in the population
problem.numElites = int(round(problem.pElites * problem.numIndividuals))
problem.numMutants = int(round(problem.pMutants * problem.numIndividuals))
problem.numCrossOvers = problem.numIndividuals - problem.numElites - problem.numMutants

#if(problem.numElites <= 0):
#    raise Exception('pElites(%s) results in an invalid numElites(%s).' % (problem.pElites, problem.numElites))

#if(problem.numMutants <= 0):
#    raise Exception('pMutants(%s) results in an invalid numMutants(%s).' % (problem.pMutants, problem.numMutants))

#if(problem.numCrossOvers <= 0):
#    raise Exception('pElites(%s) and pMutants(%s) results in an invalid numCrossOvers(%s).' % (problem.pElites, problem.pMutants, problem.numCrossOvers))

population = initializeIndividuals(problem)
startTime = time.time()
print sys.argv
generation = 0
while time.time() - startTime < float(sys.argv[2]):
    generation += 1
    
    # decode the individuals using the decoder
    #it_elapsedDecodingTime, it_decodedIndividuals = self.decodeIndividuals(population, decoder)
    #total_elapsedDecodingTime += it_elapsedDecodingTime
    #total_decodedIndividuals += it_decodedIndividuals
    
    # sort them by their fitness
    sortIndividuals(population)
    #print generation, map(str,population)
    
    # update statistics
    bestIndividual = population[0]
    newBestFitness = bestIndividual.getFitness()
    if(newBestFitness < bestFitness):
        bestSolution = bestIndividual.solution
        bestFitness = newBestFitness
        print "BF: ", bestFitness
    print bestIndividual.solution
    
    # evolve the population
    population = evolveIndividuals(population, problem)

'''
avg_decodingTimePerIndividual = 0.0
if(total_decodedIndividuals != 0):
    avg_decodingTimePerIndividual = 1000.0 * total_elapsedDecodingTime / float(total_decodedIndividuals)

print ''
print 'BRKGA Individual Decoder Performance:'
print '  Num. Individuals Decoded', total_decodedIndividuals
print '  Total Decoding Time     ', total_elapsedDecodingTime, 's'
print '  Avg. Time / Individual  ', avg_decodingTimePerIndividual, 'ms'
'''
print bestSolution, generation

#instance_19.dat -> NT: 5 Q: 7507 75

