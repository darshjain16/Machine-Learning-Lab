# Reading the dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#to ignore warnings
import warnings
warnings.filterwarnings('ignore')

# Reading Dataset
df = pd.read_csv("C:/Users/Lenovo/Desktop/ML.py/ldataset.csv")
print(df)

# print the first  5 observations of the dataset
print(df.head())
'\n'

# Print the last 5 observations of the dataset
print(df.tail())
'\n'

print(df.info())
'\n'
print(df.nunique())
'\n'

# get no.of null values with respect to each feature
print(df.isnull().sum())
'\n'

# get percentage of null data in each column
print((df.isnull().sum()/(len(df)))*100)
'\n'

# Data Reduction
# Remove City column from df
df = df.drop(['City'], axis = 1)
print("Removing City column from dataset: ")
print(df.info())
'\n'


# Creating Features
from datetime import date
date.today().year
df['car_age']=date.today().year-df['Model Year']
print("Create New Column:")
print(df.head()) 
'\n'

# make unique data
print("Make Unique Data:")
print(df.Model.unique())
print(df.Model.nunique())
'\n'

searchfor = ['G-ClASS','MODEL X','I7','CITY']
print("Search for specific model names:")
df1 = df[df.Model.str.contains('|'.join(searchfor))].head(5)
print(df1)
'\n'

# Getting count and name of unique values for a particular column
print("Replace the model name:")
df["Model"].replace({"G-CLASS": "MERCEDES-BENZ-G-CLASS", "I7": "BMW I7","CITY": "CITY ZX"}, inplace=True)
print(df)
'\n'

# Provide a statistics summary of data belonging to numerical datatype such as int, float
df2=df.describe().T
print(df2)
'\n'

# Provides a statistics summary of all data, include object, category etc
df3 = df.describe(include='all').T
print(df3)
'\n'

# Separating the features based on categorical data and numerical data
cat_cols=df.select_dtypes(include=['object']).columns
num_cols = df.select_dtypes(include=np.number).columns.tolist()
print("Categorical Variables:")
print(cat_cols)
print("Numerical Variables:")
print(num_cols)
'\n'

# Performing univariate analysis on numercial variable
# Print box plot
print('car_age')
print('Skew :', round(df['car_age'].skew(), 2))
plt.figure(figsize = (16, 5))
plt.subplot(1, 2, 1)
'\n'

# Print histogram 
df['car_age'].hist(grid=False)
plt.ylabel('count')
plt.subplot(1, 2, 2)
sns.boxplot(x=df['car_age'])
plt.show()
'\n'

# Performing univariate analysis on categorical variable
# Print bar plot
fig, axes = plt.subplots(figsize = (16, 16))
fig.suptitle('Bar plot for categorical variables in the dataset')
sns.countplot( x = 'Electric Vehicle Type', data = df, color = 'blue', 
              order = df['Electric Vehicle Type'].value_counts().index)
plt.show()