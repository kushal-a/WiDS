# Write your find_closest function here
import numpy as np
def hms2dec(h,m,s):
  out=15*dms2dec(h,m,s)
  if out<0:
    out=360-out
  return out
def dms2dec(d,m,s):
  if d<0:
    m=-m
    s=-s
  return d+m/60+s/3600
def import_bss():
    cat = np.loadtxt('bss.dat', usecols=range(1, 7))
    output=[]
    for i in range(np.shape(cat)[0]):
      output.append((i+1,hms2dec(cat[i,0],cat[i,1],cat[i,2]),dms2dec(cat[i,3],cat[i,4],cat[i,5])))
    return output
def find_closest(cat,r,d):
  distances=np.array([])
  for entry in cat:
    distances=np.append(distances,angular_dist(r,d,entry[1],entry[2]))
  min_=np.min(distances)
  ind=np.where(distances==min_)[0][0]
  obj_id=cat[ind][0]
  return obj_id,min_
  
def angular_dist(r1,d1,r2,d2):
  r1=np.radians(r1)
  d1=np.radians(d1)
  r2=np.radians(r2)
  d2=np.radians(d2)
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  a = np.sin(np.abs(d1 - d2)/2)**2
  d=2*np.arcsin(np.sqrt(a + b))
  return np.degrees(d)



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  cat = import_bss()
  
  # First example from the question
  print(find_closest(cat, 175.3, -32.5))

  # Second example in the question
  print(find_closest(cat, 32.2, 40.7))
