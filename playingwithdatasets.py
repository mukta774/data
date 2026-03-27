import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns 
from sklearn.preprocessing import StandardScaler  
df = pd.read_csv(r'D:\data_science\bodyfat - bodyfat.csv')

print(df.head())
print("\nShape : ",df.shape)
print("\n",df.describe())
print("\nInfo :",df.info())

correlation = df.corr()
print("Correlation between each bodypart and the overall bodyfat : " ,correlation['BodyFat'].sort_values(ascending=False))

print("\nNull values in the dataset:", df.isnull().sum().sum())
print("\nDuplicate values in the dataset:", df.duplicated().sum())

y = df['BodyFat']
X = df.drop(columns=['BodyFat'])

scaler = StandardScaler()
y_scaled = scaler.fit_transform(y.values.reshape(-1, 1))
X_scaled = scaler.fit_transform(X.values.reshape(-1, X.shape[1]))

plt.figure(figsize=(10, 6))
plt.scatter(X.iloc[:, 0], y , alpha=0.5)
plt.title(f'Body Fat Percentage vs {X.columns[1]} (Standardized)')
plt.xlabel(X.columns[0])
plt.ylabel('Body Fat Percentage (Standardized)')
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(X.iloc[:, 1], y , alpha=0.5)
plt.title(f'Body Fat Percentage vs {X.columns[2]} (Standardized)')
plt.xlabel(X.columns[1])    
plt.ylabel('Body Fat Percentage (Standardized)')
plt.grid()
plt.show()
 
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
