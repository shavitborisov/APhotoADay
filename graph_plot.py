#!/usr/bin/python3.6

# Pass data in csv file with two coloumns - Age, MSE

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

csv_file = sys.argv[1]

data = pd.read_csv(csv_file).set_index('Age')
data_plot = data.plot(title = "Total Sales by Month", legend = None)