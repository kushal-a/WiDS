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

# Complete the following function
def accuracy_by_treedepth(features, targets, depths):
  # split the data into testing and training sets
  split = int(features.shape[0]*0.5)
  train_features = features[:split]
  test_features = features[split:]
  train_targets = targets[:split]
  test_targets = targets[split:]
  # initialise arrays or lists to store the accuracies for the below loop
  accuracies_train=[]
  accuracies_test=[]
  # loop through depths
  for depth in depths:
    # initialize model with the maximum depth. 
    dtr = DecisionTreeRegressor(max_depth=depth)
    # train the model using the training set
    dtr.fit(train_features , train_targets)
    # get the predictions for the training set and calculate their median_diff
    predictions_test=dtr.predict(test_features)
    predictions_train=dtr.predict(train_features)
    # get the predictions for the testing set and calculate their median_diff
    accuracies_train.append(median_diff(predictions_train, train_targets))
    accuracies_test.append(median_diff(predictions_test, test_targets))
  # return the accuracies for the training and testing sets
  return accuracies_train,accuracies_test

if __name__ == "__main__":
  data = np.load('sdss_galaxy_colors.npy')
  features, targets = get_features_targets(data)

  # Generate several depths to test
  tree_depths = [i for i in range(1, 36, 2)]

  # Call the function
  train_med_diffs, test_med_diffs = accuracy_by_treedepth(features, targets, tree_depths)
  print("Depth with lowest median difference : {}".format(tree_depths[test_med_diffs.index(min(test_med_diffs))]))
    
  # Plot the results
  train_plot = plt.plot(tree_depths, train_med_diffs, label='Training set')
  test_plot = plt.plot(tree_depths, test_med_diffs, label='Validation set')
  plt.xlabel("Maximum Tree Depth")
  plt.ylabel("Median of Differences")
  plt.legend()
  plt.show()
