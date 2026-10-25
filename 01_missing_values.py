import pandas as pd

# Create dataset
data = {
    'age': [23, 25, None, 28, 22, None],
    'height': [5.5, 5.8, 5.6, None, 5.9, 5.7],
    'weight': [70, 80, None, 60, 65, None],
    'grade': ['A', 'B', 'C', 'A', None, 'B']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display original DataFrame
print("Original DataFrame with missing values:")
print(df)

# Display columns containing missing values
print("\nColumns with missing values:")
print(df.isnull().sum())

# Fill missing values
df['age'].fillna(df['age'].mean(), inplace=True)
df['height'].fillna(df['height'].median(), inplace=True)
df['weight'].fillna(df['weight'].mean(), inplace=True)
df['grade'].fillna(df['grade'].mode()[0], inplace=True)

# Display DataFrame after handling missing values
print("\nDataFrame after handling missing values:")
print(df)