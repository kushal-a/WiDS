# Write your import_bss function here.
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

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Output of the import_bss and import_super functions
  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)
