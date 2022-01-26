import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf
from scipy.constants import pi,c,G as pi,c,G

data, freq, time = np.loadtxt('GW_data_file.csv',delimiter=',')
ind=np.where(np.logical_and(freq>50,time<0))
freq=freq[ind]
time=time[ind]
data=data[ind]

indexes=np.array([],dtype=int)
for i in range(len(time)-1):
    if data[i]*data[i+1]<=0:
        indexes=np.append(indexes,[i,i+1])

time,freq = time[indexes],freq[indexes]

p_opt,p_cov = cf(lambda x,a,b: np.power(-a*x,b),time,freq)
a,b = p_opt

m=np.power(np.power(5*a,3)/np.power(8*pi,8),1/5)*(c**3)/G
print(m)
plt.scatter(np.log(-1*time),np.log(freq))
plt.plot(np.log(-1*time),(b)*(np.log(a)+np.log(-1*time)),color='green')
plt.xlabel('time')
plt.ylabel('frequency')
plt.title('curve fitting for GW')
plt.show()

