# Import the running_stats function
from helper import running_stats
import numpy as np
from astropy.io import fits
# Write your median_bins_fits and median_approx_fits here:
def median_bins_fits(filenames,B):
  for i in range(len(filenames)):
    d=fits.open(filenames[i])[0].data
    if i==0:
      data=d
      continue
    data=np.append(data,d)
  l=d.shape[0]
  data=np.reshape(data,(l,l,len(filenames)))
  mean,sd=running_stats(filenames)
  ignore=np.zeros_like(data[:,:,0])
  for i in range(l):
    for j in range(l):
      ignore[i,j]=np.sum(np.where(data[i,j,:]>mean[i,j]-sd[i,j],1,0))
  width=2*sd/B
  hist=np.zeros((l,l,B),dtype=int)
  for i in range(B):
    lowerBound=mean-sd+i*width
    for j in range(l):
      for k in range(l):
        hist[j,k,i]=np.sum(np.where(np.logical_and(data[j,k]>=lowerBound[j,k],data[j,k]<lowerBound[j,k]+width[j,k]),1,0))
  return (mean,sd,ignore,hist)

def median_approx_fits(filenames,B):
  mean,sd,ignore,hist=median_bins_fits(filenames,B)
  total=len(filenames)
  width=2*sd/B
  runningSum=ignore
  iters=np.zeros_like(mean)
  for i in range(np.shape(mean)[0]):
    for j in range(np.shape(mean)[0]):
      count=0
      while runningSum[i,j]<=(total)/2:
        if count==B:
          break
        runningSum[i,j]+=hist[i,j,count]
        count+=1
      iters[i,j]=count
  return (mean-sd+((iters-0.5)*width))



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with examples from the question.
  mean, std, left_bin, bins = median_bins_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
  median = median_approx_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
