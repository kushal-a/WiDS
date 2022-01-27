import numpy as np
galaxies_data = np.loadtxt('galaxies.csv', delimiter=',')
distances=(300000/70)*galaxies_data[:,3]
def distanceToGalaxy(s):
    #s is the serial number of the galaxy
    return distances[s-1]
def noOfGalaxiesInInterval(d1,d2):
    #let interval be d1 to d2
    return np.sum(np.where(np.logical_and(distances>=d1,distances<=d2),1,0))
def distBtwTwoGalaxies(s1,s2):
    #s1 and s2 be the serial nos of the 2 galaxies
    d1,d2=distances[s1-1],distances[s2-1]
    costheta=np.sin(galaxies_data[s1-1,2])*np.sin(galaxies_data[s2-1,2])+np.cos(galaxies_data[s1-1,2])*np.cos(galaxies_data[s2-1,2])*np.cos(galaxies_data[s1-1,1]-galaxies_data[s2-1,1])
    distSqr=d1**2 + d2**2 - 2*d1*d2*costheta
    return np.sqrt(distSqr)

print(distanceToGalaxy(1000))
print(noOfGalaxiesInInterval(200,210))
print(distBtwTwoGalaxies(1000,2000)) #something wrong here