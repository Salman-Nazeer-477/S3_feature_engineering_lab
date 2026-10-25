import pandas as pd

# Create dataset
data = {
    'name': ['John', 'Anna', 'Nino', 'Invalid Name 123', 'Charlie', ''],
    'gender': ['Male', 'Female', 'Male', 'Unknown', 'Male', 'Female'],
    'age': [23, 25, -1, 30, 22, 180]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display original DataFrame
print("Original DataFrame with invalid data entries:")
print(df)

# Remove rows with invalid names
df = df[df['name'].apply(lambda x: isinstance(x, str) and x.isalpha())]

# Keep only valid genders
df = df[df['gender'].isin(['Male', 'Female'])]

# Keep only valid ages (0 to 120)
df = df[(df['age'] >= 0) & (df['age'] <= 120)]

# Display cleaned DataFrame
print("\nCleaned DataFrame after removing invalid entries:")
print(df)