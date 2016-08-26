import numpy as np


a = np.array([0,2,3,1,7,6,4,5])
b = np.array([5,7,0,3,4,6,1,2])

print(a)
print(b)

#  crossover
def crossover(ind1, ind2):


	cut = np.random.randint(1,len(ind1)-4)
	print('cut:',cut)
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

print(crossover(a,b))