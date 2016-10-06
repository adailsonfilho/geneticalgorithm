from geneticsalgorithm import ga
import numpy as np

#  population
population_size = 30 

population = np.array([ np.random.choice(list(range(8)), size = 8, replace=False) for i in range(population_size)])

#  fitness
def fitness(invididual):

	conflicts = 0

	#conflicts counter
	for li,ci in enumerate(invididual):
		
		for lj,cj in enumerate(invididual):
			
			#not same line
			if li != lj:
				#same main diag
				if (li - ci) == (lj - cj):
					conflicts += 1
				elif (li + ci) == (lj + cj):
					conflicts += 1

	return conflicts

#  crossover_prob

crossover_prob = 1

#  mutation_prob

mutation_prob = 0.5

#  crossover
def crossover(ind1, ind2):

	cut = np.random.randint(1,len(ind1)-4)
	ref = np.zeros(len(ind1)) != 0
	new_ind = np.zeros(len(ind1)) - 1

	i = 0
	i1 = 0
	i2 = 0
	acc = 0

	while i < len(ind1):

		if i < cut or acc == 4:
			if not ref[ind1[i1]]:
				new_ind[i] = ind1[i1]
				ref[ind1[i1]] = True
				i += 1
				i1 += 1
			else:
				i1 += 1
		elif not ref[ind2[i2]] and acc < 4:
			new_ind[i] = ind2[i2]
			ref[ind2[i2]] = True
			i2 +=1
			i +=1 
			acc +=1
		else:
			i2 += 1


	return [new_ind]


#  mutation

def mutation(ind):

	perm = np.random.choice(list(range(8)),size=2,replace= False)

	temp = ind[perm[0]]
	ind[perm[0]] = ind[perm[1]]
	ind[perm[1]] = temp

	return ind


# objective

objective = "minimize"

# max_epochs

max_epochs = 1000

# generational

generational = False

# mutation_extra_individual

mutation_extra_individual = True

# stop_if_reachs

stop_if_reachs = 0

# offspring_size

#45% da population
offsprings = int(population_size * 0.3)

# progenitors_amount

progenitors_amount = 10

# elitist
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
