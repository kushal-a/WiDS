from itertools import count
import numpy as np
import matplotlib.pyplot as plt
from astropy.stats import sigma_clipped_stats
from astropy.io import fits

def get_background_histogram(array, min_count, max_count):
    """
        array is the numpy array that contains the counts for each pixel
        the bins for the histogram will be np.arange(min_count, max_count, 1)
    """
    flattened_array = array.flatten()
    num_pixels, bin_edges = np.histogram(flattened_array, bins=np.arange(min_count, max_count, 1))
    bins = 0.5*(bin_edges[1:] + bin_edges[:-1])
    return bins, num_pixels

def plot(data,color,text):
    mean,median,std=sigma_clipped_stats(data)
    bins_, num_pixels = get_background_histogram(data,median-5*std,median+5*std)
    plt.figure(figsize=(10,5))
    plt.plot(bins_,num_pixels,color=color)
    plt.xlabel('Counts')
    plt.ylabel('Number of Pixels')
    plt.title(text)
    plt.text(450,500000,"Estimate of Background Count:"+str(np.quantile(num_pixels[int(2*num_pixels.shape[0]/3):],0.5)))
    plt.show()

data=fits.open('Messier3.fits')[0].data
plot(data,'r',"Including Clusters")

data_without_cluster=np.concatenate([data[:1024,:],data[3072:,:],data[:,:1024],data[:,3072:]],axis=None)
plot(data_without_cluster,'g',"Without Clusters")


