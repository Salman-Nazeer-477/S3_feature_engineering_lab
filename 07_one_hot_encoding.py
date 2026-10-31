import pandas as pd

# Create dataset
data = {
    'category': ['Good', 'Better', 'Best', 'Good', 'Better'],
    'gender': ['Male', 'Female', 'Male', 'Female', 'Male']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Perform One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=['category', 'gender'])

# Display encoded DataFrame
print("\nDataFrame after One-Hot Encoding:")
print(df_encoded)