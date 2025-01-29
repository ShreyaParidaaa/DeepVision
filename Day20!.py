#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    # Process the text
    doc = nlp(text)

    # Print named entities and their labels
    print("Entities and their types:")
    for ent in doc.ents:
        print(f"{ent.text}: {ent.label_}")

# Example usage
text = "Apple was founded by Steve Jobs in Cupertino, California."
perform_ner(text)


# In[ ]:




