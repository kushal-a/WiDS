# Write your calc_stats function here.
import numpy as np
def calc_stats(f):
  data = np.loadtxt(f, delimiter=',')
  me=np.sum(data)/np.size(data)
  m=np.sort(data,None)
  if np.size(data)%2==0:
    med=(m[int(np.size(data)/2)]+m[int(np.size(data)/2) - 1])/2
  else:
    med=m[int((np.size(data)-1)/2)]
  me=np.round(me, decimals=1)
  med=np.round(med, decimals=1)
  return (me,med)



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calc_stats` function with examples:
  mean = calc_stats('data.csv')
  print(mean)
