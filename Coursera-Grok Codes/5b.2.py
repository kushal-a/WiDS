import numpy as np
from sklearn.tree import DecisionTreeRegressor

# copy in your get_features_targets function here
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

# load the data and generate the features and targets
data = np.load('sdss_galaxy_colors.npy')
features, targets = get_features_targets(data)
  
# initialize model
dtr = DecisionTreeRegressor()
# train the model
dtr.fit(features, targets)
# make predictions using the same features
predictions = dtr.predict(features)
# print out the first 4 predicted redshifts
print(predictions[:4])
