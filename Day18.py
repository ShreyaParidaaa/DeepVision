#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

# Ensure required NLTK resources are downloaded
nltk.download('punkt')

# Function to load and tokenize text
def get_most_common_words(file_path, num_words=10):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Tokenize the text
        tokens = word_tokenize(text.lower())

        # Count word frequencies
        word_counts = Counter(tokens)

        # Get the most common words
        common_words = word_counts.most_common(num_words)

        return common_words
    except Exception as e:
        print(f"Error: {e}")
        return []

# Example usage
file_path = "sample.txt"  # Change this to your actual file path
common_words = get_most_common_words(file_path)

# Display results
print("Most Common Words:")
for word, count in common_words:
    print(f"{word}: {count}")


# In[ ]:




