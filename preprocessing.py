import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor 
from sklearn import preprocessing
import seaborn as sns
import sys

if len(sys.argv) < 3:
	sys.exit("Error: incorrect number of arguments supplied. Usage: python data_cleaning.py example.csv")

filepath = sys.argv[1]

# load data from csv
try:
	df = pd.read_csv(filepath)
except:
	sys.exit("Error: csv file not found.")

# drop symbol
df = df.drop('symbol',axis=1)

# drop columns that are missing more than 50% of data
valid_columns = (df.isna().sum()/df.shape[0] < .5).values
df = df.loc[:,valid_columns]

# drop remaining entries with missing values
df = df.dropna()

# encode day month and year as integers
df['date'] = pd.to_datetime(df['date'])
df['day'] =  df['date'].dt.day
df['month'] =  df['date'].dt.month
df['year'] =  df['date'].dt.year
df = df.drop('date',axis=1)

features = df.drop('increasePercent',axis=1).copy()

# drop features with high VIF
def get_max_vif():
	max_vif = 5
	max_feature = None
	for i in range(features.shape[1]):
		vif = variance_inflation_factor(features.values, i) 
		if vif > max_vif:
			max_vif = vif
			max_feature = features.columns[i] 
	return max_feature, max_vif

f, v = get_max_vif()
while f is not None:
	features = features.drop(f, axis=1)
	f, v = get_max_vif()

# normalize features
min_max_scaler = preprocessing.MinMaxScaler()
features = pd.DataFrame(min_max_scaler.fit_transform(features.values),columns=features.columns)

features['increasePercent'] = df['increasePercent']
df = features.copy()

# remove invalid entries
df = df[df['increasePercent'] != 0]

# encode increase percent
if int(sys.argv[2]) == 0: # 1 for >= 10%, 0 otherwise
	df['increasePercent'] = df['increasePercent'] >= 10
else: # increase = 1 for >= 10%, decrease = 1 for <= -10%, both 0 otherwise
	df['increase'] = df['increasePercent'] >= 10
	df['decrease'] = df['increasePercent'] <= -10
	df = df.drop('increasePercent',axis=1)

df.to_csv("data.csv",index=False)
