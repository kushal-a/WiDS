# Write your median_bins and median_approx functions here.
import numpy as np
def median_bins(values,B):
  mean=np.mean(values)
  sd=np.std(values)
  ignore=int(np.sum(np.where(values<mean-sd,1,0)))
  width=2*sd/B
  hist=np.array([],dtype=int)
  for i in range(B):
    lowerBound=mean-sd+i*width
    hist=np.append(hist,np.sum(np.where(np.logical_and(values>=lowerBound,values<lowerBound+width),1,0)))
  return (mean,sd,ignore,hist)
def median_approx(values,B):
  mean,sd,ignore,hist=median_bins(values,B)
  total=np.size(values)
  width=2*sd/B
  runningSum=ignore
  i=0
  while runningSum<=(total)/2:
    if i==B:
      break
    runningSum+=hist[i]
    i+=1
  return (mean-sd+((i-0.5)*width))


# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your functions with the first example in the question.
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))

  # Run your functions with the second example in the question.
  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
