import numpy as np
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeRegressor

import numpy as np
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeRegressor

# paste your get_features_targets function here
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

# paste your median_diff function here
def median_diff(predicted, actual):
  return np.median(np.absolute(predicted-actual))


# complete this function
def cross_validate_model(model, features, targets, k):
  kf = KFold(n_splits=k, shuffle=True)

  # initialise a list to collect median_diffs for each iteration of the loop below
  med_diffs=[]
  for train_indices, test_indices in kf.split(features):
    train_features, test_features = features[train_indices], features[test_indices]
    train_targets, test_targets = targets[train_indices], targets[test_indices]
    
    # fit the model for the current set
    model.fit(train_features,train_targets)
    # predict using the model
    predictions=model.predict(test_features)
    # calculate the median_diff from predicted values and append to results array
    med_diffs.append(median_diff(predictions, test_targets))
 
  # return the list with your median difference values
  return med_diffs

if __name__ == "__main__":
  data = np.load('./sdss_galaxy_colors.npy')
  features, targets = get_features_targets(data)

  # initialize model with a maximum depth of 19
  dtr = DecisionTreeRegressor(max_depth=19)

  # call your cross validation function
  diffs = cross_validate_model(dtr, features, targets, 10)

  # Print the values
  print('Differences: {}'.format(', '.join(['{:.3f}'.format(val) for val in diffs])))
  print('Mean difference: {:.3f}'.format(np.mean(diffs)))
