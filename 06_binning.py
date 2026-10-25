import pandas as pd

# Create the dataset
data = {'Age': [5, 12, 25, 37, 45, 60, 72, 85, 90, 100]}
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Equal-width binning
bins = [0, 20, 40, 60, 80, 100]
labels = ['0-20', '21-40', '41-60', '61-80', '81-100']
df['Age Group'] = pd.cut(
    df['Age'],
    bins=bins,
    labels=labels,
    include_lowest=True
)
print("\nDataFrame with Binned Age Groups:")
print(df)

# Equal-frequency binning
df['Age Group (Equal Frequency)'] = pd.qcut(
    df['Age'],
    q=5,
    labels=['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
)
print("\nDataFrame with Equal Frequency Binned Age Groups:")
print(df)