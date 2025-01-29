#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

def extract_email_addresses(text):
    # Define a regular expression pattern for matching email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    # Use re.findall() to extract all matches of the email pattern
    email_addresses = re.findall(email_pattern, text)

    return email_addresses

# Test the function with the provided input
text = 'Contact us at support@example.com and sales@example.org.'
emails = extract_email_addresses(text)

# Print the extracted email addresses
print(emails)

