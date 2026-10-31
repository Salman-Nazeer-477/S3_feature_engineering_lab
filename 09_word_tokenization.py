import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download('punkt')

# Create dataset
data = {
    'Text': [
        'The children are playing in the playground.',
        'They are running very fast and enjoying the games.',
        'The games are fun and exciting for all the kids!'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Define tokenization function
def tokenize(text):
    return word_tokenize(text)

# Apply tokenization
df['Tokenized'] = df['Text'].apply(tokenize)

# Display tokenized DataFrame
print("\nDataFrame after Tokenization:")
print(df[['Text', 'Tokenized']].to_string(index=False))