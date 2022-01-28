# Write your query function here
import numpy as np

def query(csv):
    out = np.loadtxt(csv,delimiter=",")
    return out[np.where(out[:,2]>1)][:,[0,2]]



# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv')
