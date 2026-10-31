import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download required NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

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

# Define lemmatization function
def lemmatize(text):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    return [lemmatizer.lemmatize(word.lower()) for word in tokens]

# Apply lemmatization
df['Lemmatized'] = df['Text'].apply(lemmatize)

# Display result
print("\nDataFrame after Lemmatization:")
print(df[['Text', 'Lemmatized']].to_string(index=False))