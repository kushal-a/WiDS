# Write your crossmatch function here.
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
def import_super():
    cat = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
    output=[]
    for i in range(np.shape(cat)[0]):
      output.append((i+1,cat[i,0],cat[i,1]))
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

def crossmatch(bss_cat, super_cat, max_dist):
  matches=[]
  non_matches=[]
  for i in range(np.shape(bss_cat)[0]):
      obj_id,dist=find_closest(super_cat,bss_cat[i][1],bss_cat[i][2])
      if dist<max_dist:
          matches.append((bss_cat[i][0],obj_id,dist))
      else:
        non_matches.append(bss_cat[i][0])
  return matches,non_matches



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()

  # First example in the question
  max_dist = 40/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

  # Second example in the question
  max_dist = 5/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))
