import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download required NLTK resources
nltk.download('punkt')

# Create dataset
data = {
    'Text': [
        'The children are playing in the playground',
        'They are running very fast and enjoying the games',
        'The games are fun and exciting for all kids'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Define stemming function
def stem(text):
    stemmer = PorterStemmer()
    tokens = word_tokenize(text)
    return [stemmer.stem(word) for word in tokens]

# Apply stemming
df['Stemmed'] = df['Text'].apply(stem)

# Display result
print("\nDataFrame after Stemming:")
print(df.to_string(index=False))