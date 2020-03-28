from enum import Enum
import os
import pickle
import PIL.Image
import numpy as np

import sklean.linear_model
from sklearn.model_selection import train_test_split
from sklearn import metrics
# Regression API for this project


class RegressionModels (Enum):
    


# parameters:
# - dimensions
# - findOffset (bool): if true regressor will find offset instead of true value
# - Regression Model
# Will find the lasso regressor for the given data and parameters
def findRegressor (start_photos, start_ages, target_photo, target_age, dimensions, findOffset):
    
    