# Write your list_stats function here.
def list_stats(l):
  l.sort()
  if len(l)==1:
    median=l[0]
  elif len(l)%2==0:
    median=(l[int(len(l)/2)]+l[int(len(l)/2) - 1])/2
  else:
    median=l[int((len(l)-1)/2)]
  s=sum(l)
  return (median,s/len(l))



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
  print(m)

  # Run your function with the second example in the question
  m = list_stats([1.5])
  print(m)
