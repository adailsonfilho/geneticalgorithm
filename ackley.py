from geneticsalgorithm import ga
import numpy as np
import math
import ipdb

#  - fitness: a function that will be run for calculate the fitness of each individual

def fitness(individual):

	def ackley(x):

		firstSum = 0.0
		secondSum = 0.0

		for c in x:
			firstSum += c**2.0
			secondSum += math.cos(2.0*math.pi*c)
		n = float(len(x))
		return -20.0*math.exp(-0.2*math.sqrt(firstSum/n)) - math.exp(secondSum/n) + 20 + math.e

	return 1/(ackley(individual)+1)


#  - population: numpy arrays with the initial population
lim_inf = -15
lim_sup = 15

dimension = 10

population_size = 30
population = np.array([ [np.random.uniform(lim_inf, lim_sup) for i in range(dimension)] for i in range(population_size) ])


#  - crossover_prob: a double between 0 and 1 that determines a probability of ocorring a crossover
crossover_prob = 1


#  - mutation_prob: a double between 0 and 1 that determines a probability of ocorring a mutation
mutation_prob = 0.1


#  - crossover: a function that perform a crossover between two individuals (that must be specified by the developer) and it is called when raffled based on the "crossover_prob" argument, it returns a list of new children for the two given parents
def crossover(ind1, ind2):

	cut = np.random.randint(1,len(ind1)-1)
	
	offspring = []
	offspring.append(np.concatenate((ind1[:cut],ind2[cut:])))
	offspring.append(np.concatenate((ind2[:cut],ind1[cut:])))

	return offspring

#  - mutation: a function that perform a mutation on a single individual and it is called when raffled based on the "mutation_prob" argument

def mutation(ind):

	times = np.random.randint(1, int(0.5*len(ind)))

	for t in range(times):
		perm = np.random.choice(range(len(ind)), size = 2, replace = False)

		temp = ind[perm[0]]
		ind[perm[0]] = ind[perm[1]]
		ind[perm[1]] = temp

	return ind


#  - objective: "minimize" is the defalt value. The options are: "maximize" or "minimize", for the obvious reasons
objective = 'maximize'

#  - max_epochs maximum number of interactions
max_epochs = 1000

#  - generational: True if the progenitors always die, and False if they can still live and the generation die
generational = False

#  - mutation_extra_individual: True or False, defines if a mutation of a individual is considered a new individual or replace de individual
mutation_extra_individual = True

#  - stop_if_reachs: fitness good enough for stopping, if not set, will only stop when achieve the "max_epochs" epochs
stop_if_reachs = 1

#  - offsprings: number of offsprings
offsprings = int(population_size * 0.5)

# - progenitors_amount: amount of individuals considered in the wheel selection
progenitors_amount = population_size

#  - elitist: True or False, defines if only the best one survives
elitist = False

ga(population = population,
	fitness = fitness,
	crossover_prob = crossover_prob,
	mutation_prob = mutation_prob,
	crossover = crossover,
	mutation = mutation,
	objective = objective,
	max_epochs = max_epochs,
	generational = generational,
	mutation_extra_individual = mutation_extra_individual,
	stop_if_reachs = stop_if_reachs,
	offsprings = offsprings,
	progenitors_amount = progenitors_amount,
	elitist = elitist)