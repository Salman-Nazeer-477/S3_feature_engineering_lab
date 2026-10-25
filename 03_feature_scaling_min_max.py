import pandas as pd

# Create dataset
data = {
    'height': [150, 160, 170, 180, 190],
    'weight': [50, 65, 75, 85, 100]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display original dataset
print("Original Dataset:")
print(df)

# Min-Max Normalization
df['height'] = (df['height'] - df['height'].min()) / (df['height'].max() - df['height'].min())
df['weight'] = (df['weight'] - df['weight'].min()) / (df['weight'].max() - df['weight'].min())

# Display normalized dataset
print("\nNormalized Dataset:")
print(df)