import numpy as np
from matplotlib import pyplot as plt

# Complete the following to make the plot
if __name__ == "__main__":
    data = np.load('sdss_galaxy_colors.npy')
    # Get a colour map
    cmap = plt.get_cmap('YlOrRd')
    
    # Define our colour indexes u-g and r-i

    # Make a redshift array

    # Create the plot with plt.scatter and plt.colorbar
    plt.scatter(data['u']-data['g'],data['r']-data['i'],s=1,linewidths=0,c=data['redshift'])
    c=plt.colorbar()
    # Define your axis labels and plot title
    plt.xlabel('Color index u-g')
    plt.ylabel('Color index r-i')
    plt.title('Redshift (colour) u-g versus r-i')
    c.set_label('Redshift')
    plt.xlim([-0.5,2.5])
    plt.ylim([-0.5,1])
    # Set any axis limits
    
    plt.show()
