import numpy as np

def get_features_targets(data):
  # complete this function
      u=data['u']
      g=data['g']
      r=data['r']
      i=data['i']
      z=data['z']
      inputs=np.zeros((data.shape[0],4))
      inputs[:,0]=u-g
      inputs[:,1]=g-r
      inputs[:,2]=r-i
      inputs[:,3]=i-z
      return inputs,data['redshift']


if __name__ == "__main__":
  # load the data
  data = np.load('sdss_galaxy_colors.npy')
    
  # call our function 
  features, targets = get_features_targets(data)
    
  # print the shape of the returned arrays
  print(features[:2])
  print(targets[:2])
