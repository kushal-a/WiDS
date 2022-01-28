# Write your query function here
import numpy as np
def query(csv):
    file = np.loadtxt(csv,delimiter=",")
    selected_cols=file[:,[0,2]]
    satisfying_rows=selected_cols[np.where(selected_cols[:,1]>1)]
    sort_indices=np.argsort(satisfying_rows[:,1])
    return satisfying_rows[sort_indices,:]

# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv')
