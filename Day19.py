#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_cosine_similarity(text1, text2):
    # Create a TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()

    # Transform texts into TF-IDF vectors
    tfidf_matrix = vectorizer.fit_transform([text1, text2])

    # Compute cosine similarity
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

    return similarity[0][0]

# Example usage
text1 = "Machine learning is fascinating."
text2 = "Artificial intelligence and machine learning are related."

similarity_score = calculate_cosine_similarity(text1, text2)
print(f"Cosine Similarity: {similarity_score:.4f}")

