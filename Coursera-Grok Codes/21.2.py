import numpy as np
import statistics
import time

def time_stat(func, size, ntrials):
  # the time to generate the random array should not be included
  
  dur=0
  # modify this function to time func with ntrials times using a new random array each time
  for i in range(ntrials):
    data = np.random.rand(size)
    start=time.perf_counter()
    func(data)
    dur+=time.perf_counter() - start
  # return the average run time
  return dur/ntrials

if __name__ == '__main__':
  print('{:.6f}s for statistics.mean'.format(time_stat(statistics.mean, 10**5, 10)))
  print('{:.6f}s for np.mean'.format(time_stat(np.mean, 10**5, 1000)))
