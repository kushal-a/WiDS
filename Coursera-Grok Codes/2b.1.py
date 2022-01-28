# Write your hms2dec and dms2dec functions here
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



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The first example from the question
  print(hms2dec(23, 12, 6))

  # The second example from the question
  print(dms2dec(22, 57, 18))

  # The third example from the question
  print(dms2dec(-66, 5, 5.1))
