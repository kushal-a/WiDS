import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf
from scipy.constants import pi,c,G as pi,c,G
from astropy.io import fits
from astropy.stats import sigma_clipped_stats

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

p_opt,p_cov = cf(lambda x,a,b: np.sign(-1*a*x)*np.float_power(np.abs(a*x),b),time,freq)
a,b = p_opt

m=np.power(np.power(5*a,3)/np.power(8*pi,8),1/5)*(c**3)/G
print("M="+str(m))
plt.scatter(np.log(-1*time),np.log(freq))
plt.plot(np.log(-1*time),(b)*(np.log(a)+np.log(-1*time)),color='green')
plt.xlabel('time')
plt.ylabel('frequency')
plt.title('curve fitting for GW')
plt.show()


data=fits.open('Messier3.fits')[0].data
def get_background_histogram(array, min_count, max_count):
    """
        array is the numpy array that contains the counts for each pixel
        the bins for the histogram will be np.arange(min_count, max_count, 1)
    """
    flattened_array = array.flatten()
    num_pixels, bin_edges = np.histogram(flattened_array, bins=np.arange(min_count, max_count, 1))
    bins = 0.5*(bin_edges[1:] + bin_edges[:-1])
    return bins, num_pixels
    
mean,median,std=sigma_clipped_stats(data)

bins_, num_pixels = get_background_histogram(data,median-5*std,median+5*std)
bins_=bins_/mean
plt.plot(bins_,num_pixels)
def gaussian(x,mu,sigma,a):
    return a*np.exp(-0.5*(np.float_power((x-mu)/sigma,2)))

p_opt,p_cov=cf(gaussian,bins_,num_pixels,(1,10**(-2),400000))
mu,sigma,a=p_opt
num, bin_ed = np.histogram(data.flatten(), bins=np.arange(median-5*std, median+5*std, 1))
bin_nor=bin_ed/mean
plt.scatter(bins_,num_pixels,label="Data")
plt.plot(bins_,gaussian(bins_,mu,sigma,a),color='r',label="Gaussian Fit")
plt.xlabel("$x/\mu$")
plt.ylabel("Count")
plt.legend()
plt.show()
