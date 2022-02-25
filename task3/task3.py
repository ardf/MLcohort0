"""
Task:
AIM: To create a neural network model of the highest accuracy, with the least number of
parameters, and the least number of layers.
1. Download the dataset from the link here
2. Create all the pre-processing steps similar to the one from the above notebooks
3. Create a Neural network model using Keras and train the model on the training dataset
4. Test the model on the test dataset
5. Push the code on Github, showing the model architecture, number of parameters
and test accuracy on the Readme.md file.
"""
import numpy as np
import pandas as pd

data = pd.read_csv('train_labels.csv')
print(data.head())


