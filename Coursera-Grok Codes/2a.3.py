# Write your function median_FITS here:
import numpy as np
from astropy.io import fits
import time

def median_fits(l):
  start=time.perf_counter()
  data=np.array([])
  for fn in l:
    hdulst=fits.open(fn)
    fil=hdulst[0].data
    data=np.append(data,fil),
  data = np.reshape(data,(len(l),int(np.sqrt(np.size(data)/len(l))),int(np.sqrt(np.size(data)/len(l)))))
  medn=np.median(data,axis=0)
  memory=data.nbytes/1024
  dur=time.perf_counter() - start
  return (medn,dur,memory)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with first example in the question.
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  # Run your function with second example in the question.
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
  print(result[0][100, 100], result[1], result[2])
