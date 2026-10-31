import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

# Create dataset
data = {
    'x1': [1, 2, 3, 4, 5],
    'x2': [5, 4, 3, 2, 1]
}
df = pd.DataFrame(data)

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Generate polynomial features
poly = PolynomialFeatures(degree=2, include_bias=False)
poly_features = poly.fit_transform(df[['x1', 'x2']])

poly_df = pd.DataFrame(
    poly_features,
    columns=poly.get_feature_names_out(['x1', 'x2'])
)

print("\nDataFrame with Polynomial Features:")
print(poly_df)

# Create interaction feature
df['x1_x2_interaction'] = df['x1'] * df['x2']

# Combine polynomial and interaction features
final_df = pd.concat([poly_df, df[['x1_x2_interaction']]], axis=1)

print("\nFinal DataFrame with Polynomial and Interaction Features:")
print(final_df)