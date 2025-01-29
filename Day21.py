#!/usr/bin/env python
# coding: utf-8

# In[1]:


from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    text = input("Enter text for sentiment analysis: ")
    sentiment = analyze_sentiment(text)
    print(f"The sentiment of the text is: {sentiment}")

