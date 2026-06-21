import pandas as pd

# Ye line add karo — saari columns dikhayegi
pd.set_option('display.max_columns', None)

df = pd.read_excel('Dataset for Data Analytics.xlsx')
print(df.describe())
Q1 = df['TotalPrice'].quantile(0.25)
Q3 = df['TotalPrice'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

# Outliers nikalo
outliers = df[(df['TotalPrice'] < lower_limit) | (df['TotalPrice'] > upper_limit)]

print("Total Outliers:", len(outliers))
print(outliers[['OrderID', 'TotalPrice']])
print(outliers[['OrderID', 'Quantity', 'UnitPrice', 'TotalPrice']])

# Sirf number columns ka correlation
correlation = df[['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice']].corr()
print(correlation)

import matplotlib.pyplot as plt
import seaborn as sns

# Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Between Variables')
plt.savefig('correlation_heatmap.png')
plt.show()

print("Chart saved!")