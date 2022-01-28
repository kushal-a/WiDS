# Write your mean_fits function here:
from astropy.io import fits
def mean_fits(l):
  hlst=fits.open(l[0])
  d=hlst[0].data
  l.remove(l[0])
  for n in l:
     hlst=fits.open(n)
     a=hlst[0].data
     d+=a
  return d/(len(l)+1)



if __name__ == '__main__':
  
  # Test your function with examples from the question
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(data[100, 100])

  # You can also plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()
