#!/usr/bin/env python
# coding: utf-8

# In[4]:


import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Input sentence
sentence = "NLP is amazing and fun to learn."

# Process the sentence
doc = nlp(sentence)

# Print the POS tagging
print("Token\tPOS Tag")
print("----------------")
for token in doc:
    print(f"{token.text}\t{token.pos_}")


# In[ ]:




