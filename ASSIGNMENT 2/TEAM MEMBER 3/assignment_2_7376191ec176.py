# -*- coding: utf-8 -*-
"""ASSIGNMENT_2_7376191EC176.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U0grYwEYD7dgF_CmyGNuegN1fh5GPMMP

UPLOADING A FILE
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from google.colab import files
files.upload()

"""DISPLAY THE DATASET"""

df = pd.read_csv("/content/Churn_Modelling.csv")
df.head()

"""MULTI-VARIATE ANALYSIS"""

sns.pairplot(df)

plot_x = np.random.randint(low=1, high=10, size=25)

plt.plot(plot_x, color = 'blue', linewidth=3, linestyle='-.')
plt.show()

"""BI-VARIANT ANALYSIS"""

sns.set_style('whitegrid')
ax= sns.boxplot(x='CreditScore',y='Balance',data=df)
ax = sns.stripplot(x="CreditScore", y="Balance",data=df)

sns.heatmap(df.corr(), annot = True, cmap='viridis')

data = pd.read_csv("Churn_Modelling.csv")

df = pd.DataFrame(data)
df.mean()

bool_series = pd.isnull(df["Age"])
df[bool_series]

df.notnull()

df[(df['Age'] > 39) | (df['Age'] < 42)]

new_df = df[(df['Tenure'] < 8) & (df['Tenure'] > 1)]
new_df

x = df.iloc[ : , :-1].values
x

y= df.iloc[ : , 4].values
y