import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
df = sns.load_dataset('iris')

# Display the dataset
print(df)

# Remove the categorical column
df_numeric = df.drop(columns=['species'])
print(df_numeric)

# Calculate the correlation matrix
correlation_matrix = df_numeric.corr()
print(correlation_matrix)

# Visualize the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap='coolwarm',
    vmin=-1,
    vmax=1,
    fmt='.2f',
    linewidths=0.5
)
plt.title('Correlation Matrix Heatmap of Iris Dataset')
plt.show()