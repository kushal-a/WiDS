import numpy as np
from astropy.io import fits
from astropy.stats import sigma_clipped_stats
import matplotlib.pyplot as plt

def get_background_histogram(array, min_count, max_count):
    """
        array is the numpy array that contains the counts for each pixel
        the bins for the histogram will be np.arange(min_count, max_count, 1)
    """
    flattened_array = array.flatten()
    num_pixels, bin_edges = np.histogram(flattened_array, bins=np.arange(min_count, max_count, 1))
    bins = 0.5*(bin_edges[1:] + bin_edges[:-1])
    return bins, num_pixels


# curpath = os.path.abspath('.')                  
# biasFolder = os.path.join(curpath, 'bias') 
# biasList = glob.glob(os.path.join(biasFolder,'*fits'))
# numBiasFiles = len(biasList)
# biasImages = np.zeros((4108, 4096, numBiasFiles))

# for i in range(numBiasFiles):
#         biasImages[:,:,i] = fits.open(biasList[i])[0].data

# masterBias = np.median(biasImages, axis=2)

# Flat = fits.open('Flat.fits')[1].data

# masterFlat = Flat - masterBias

# masterFlat = masterFlat/np.median(masterFlat)

# rawHDU = fits.open('Messier3_raw.fits')[0]
# rawData = rawHDU.data

# rawHeader = rawHDU.header

# procData = (rawData - masterBias) / masterFlat

# procHDU = fits.PrimaryHDU(procData)
# procHDU.header = rawHeader

# procHDU.writeto('Messier3.proc.fits', overwrite=True)

procData=fits.open("Messier3.proc.fits")[0].data

def plot(Data,txt,type):
    mean,median,std=sigma_clipped_stats(Data)
    bins_, num_pixels = get_background_histogram(Data,median-5*std,median+5*std)

    plt.figure(figsize=(10,5))
    if type=="h":
        plt.plot(bins_,num_pixels)
        plt.xlabel('Counts')
        plt.ylabel('Number of Pixels')
    else:
        plt.imshow(Data)
        plt.colorbar()
    plt.title(txt)
    plt.show()
plot(procData,"Processed Data","h")

transData=fits.open("Messier3_transient.proc.fits")[0].data

newData=transData-procData
plot(newData,"New Data","i")
new_mean,new_median,new_std=sigma_clipped_stats(newData)


ind = np.where(newData>new_median+5*new_std)
refined_data=np.zeros_like(newData)
refined_data[ind]=newData[ind]
plot(refined_data,"Final Image","i")