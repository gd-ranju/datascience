import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the data
data = pd.read_csv('data.csv')
data.head(10)
data.describe()