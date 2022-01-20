import numpy as np
beehive_data = np.loadtxt('Beehive_data.csv', delimiter=',')
distances =10*10**((beehive_data[:,0]-4.83)/5+beehive_data[:,1]/2) # since we take unit distance as 10 parsec
meanDistance=sum(distances*beehive_data[:,2])/sum(beehive_data[:,2])
print (meanDistance)