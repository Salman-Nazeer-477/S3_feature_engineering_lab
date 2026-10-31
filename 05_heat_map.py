import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
df = sns.load_dataset('iris')

# Display the dataset
print(df.head())

# Remove the categorical column
df_numeric = df.drop(columns=['species'])

# Calculate correlation matrix
correlation_matrix = df_numeric.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Visualize heatmap
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