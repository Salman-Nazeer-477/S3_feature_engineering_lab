import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary containing the data
data_dict = {
    'Age': [22, 25, 47, 52, 46, 56, 59, 60, 62, 61, 18, 28, 27],
    'Income': [50000, 55000, 65000, 70000, 75000, 80000, 60000, 70000, 73000, 55000, 40000, 45000, 50000],
    'Spending Habits': [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000, 3200, 3500, 3500, 4000]
}

# Create a DataFrame
df = pd.DataFrame(data_dict)

# Display the first five rows
print(df.head())

# Display information about the DataFrame
df.info()

# Display statistical summary
print(df.describe())

# Histogram of Age
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], kde=True)
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Histogram of Income
plt.figure(figsize=(10, 6))
sns.histplot(df['Income'], kde=True)
plt.title('Histogram of Income')
plt.xlabel('Income')
plt.ylabel('Frequency')
plt.show()

# Histogram of Spending Habits
plt.figure(figsize=(10, 6))
sns.histplot(df['Spending Habits'], kde=True)
plt.title('Histogram of Spending Habits')
plt.xlabel('Spending Habits')
plt.ylabel('Frequency')
plt.show()

# Boxplot of Age
plt.figure(figsize=(10, 6))
sns.boxplot(x='Age', data=df)
plt.title('Boxplot of Age')
plt.show()

# Boxplot of Income
plt.figure(figsize=(10, 6))
sns.boxplot(x='Income', data=df)
plt.title('Boxplot of Income')
plt.show()

# Boxplot of Spending Habits
plt.figure(figsize=(10, 6))
sns.boxplot(x='Spending Habits', data=df)
plt.title('Boxplot of Spending Habits')
plt.show()