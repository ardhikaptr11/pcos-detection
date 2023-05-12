# Import all necessary dependencies
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import *
from keras.losses import *
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load and read the dataset
file_url = 'https://raw.githubusercontent.com/ardhikaptr11/pcos-detection/main/Dataset/PCOS%20Dataset.csv'
read_file = pd.read_csv(file_url)

# Dropping feature with NaN values
data = read_file.drop(['Unnamed: 44'], axis=1)
print(data.head(10))  # Print first 10 rows in the dataset


