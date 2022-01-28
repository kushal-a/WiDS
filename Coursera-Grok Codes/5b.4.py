import numpy as np
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

# write a function that splits the data into training and testing subsets
# trains the model and returns the prediction accuracy with median_diff
def validate_model(model, features, targets):
  # split the data into training and testing features and predictions
    split = features.shape[0]//2
    train_features = features[:split]
    test_features = features[split:]
    train_targets = targets[:split]
    test_targets = targets[split:]
    # train the model
    model.fit(train_features, train_targets)
    # make predictions using the same features
    predictions = model.predict(test_features)
    # get the predicted_redshifts
    # use median_diff function to calculate the accuracy
    return median_diff(test_targets, predictions)


if __name__ == "__main__":
  data = np.load('sdss_galaxy_colors.npy')
  features, targets = get_features_targets(data)

  # initialize model
  dtr = DecisionTreeRegressor()

  # validate the model and print the med_diff
  diff = validate_model(dtr, features, targets)
  print('Median difference: {:f}'.format(diff))
