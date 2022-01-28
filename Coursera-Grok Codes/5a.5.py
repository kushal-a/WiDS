# Write your query function here
import numpy as np
def query(csv1,csv2):
    file1 = np.loadtxt(csv1,delimiter=",")
    file2 = np.loadtxt(csv2,delimiter=",",usecols=[0,5])
    satisfying_rows1=file1[np.where(file1[:,2]>1)]
    satisfying_rows1_=np.array([])
    for i,(kid,_,radius) in enumerate(satisfying_rows1):
        if i!=0:
            ind=np.where(file2[:,0]==kid)
            satisfying_rows2=np.vstack((satisfying_rows2,file2[ind]))
        else:
            ind=np.where(file2[:,0]==kid)
            satisfying_rows2=file2[ind]
        for __ in range(np.shape(ind)[1]):
            satisfying_rows1_=np.append(satisfying_rows1_,radius)
        
    out=satisfying_rows2[:,1]/satisfying_rows1_
    out=np.sort(out)
    out=out[:, np.newaxis]
    return out



# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv', 'planets.csv')
