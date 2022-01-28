# Write your crossmatch function here.
import numpy as np
import time
from astropy.coordinates import SkyCoord
from astropy import units as u

def angular_dist(r1,d1,r2,d2):
    b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
    a = np.sin(np.abs(d1 - d2)/2)**2
    return 2*np.arcsin(np.sqrt(a + b))

def crossmatch(cat1,cat2,radius):
    start = time.perf_counter()
    sky_cat1 = SkyCoord(cat1*u.degree, frame='icrs')
    sky_cat2 = SkyCoord(cat2*u.degree, frame='icrs')
    closest_ids, closest_dists, closest_dists3d = sky_cat1.match_to_catalog_sky(sky_cat2)
    closest_dists=closest_dists.value
    matches=[]
    non_matches=[]
    for i,dist in enumerate(closest_dists):
        if dist<radius:
            matches.append((i,closest_ids[i],dist))
        else:
            non_matches.append(i)
    dur = time.perf_counter() - start
    return matches,non_matches,dur



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The example in the question
  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  # Test your function on random inputs
  np.random.seed(0)
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)
