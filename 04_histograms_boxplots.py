import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create dataset dictionary
data_dict = {
    'Age': [22, 25, 47, 52, 46, 56, 59, 60, 62, 61, 18, 28, 27],
    'Income': [50000, 55000, 65000, 70000, 75000, 80000, 60000, 70000, 73000, 55000, 40000, 45000, 50000],
    'Spending Habits': [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000, 3200, 3500, 3500, 4000]
}

# Create DataFrame
df = pd.DataFrame(data_dict)

# Display head, info, and describe
print(df.head())
df.info()
print(df.describe())

# Histograms
for col in ['Age', 'Income', 'Spending Habits']:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[col], kde=True)
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()

# Boxplots
for col in ['Age', 'Income', 'Spending Habits']:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=col, data=df)
    plt.title(f'Boxplot of {col}')
    plt.show()