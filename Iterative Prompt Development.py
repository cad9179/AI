#!/usr/bin/env python
# coding: utf-8

# In[34]:


import openai
import os

openai.api_key = "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"


# In[35]:


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


# In[24]:


from IPython.display import display, HTML
display(HTML(response))


# In[36]:


fact_sheet_chair = """
OVERVIEW
- Part of a beautiful family of mid-century inspired office furniture, 
including filing cabinets, desks, bookcases, meeting tables, and more.
- Several options of shell color and base finishes.
- Available with plastic back and front upholstery (SWC-100) 
or full upholstery (SWC-110) in 10 fabric and 6 leather options.
- Base finish options are: stainless steel, matte black, 
gloss white, or chrome.
- Chair is available with or without armrests.
- Suitable for home or business settings.
- Qualified for contract use.

CONSTRUCTION
- 5-wheel plastic coated aluminum base.
- Pneumatic chair adjust for easy raise/lower action.

DIMENSIONS
- WIDTH 53 CM | 20.87”
- DEPTH 51 CM | 20.08”
- HEIGHT 80 CM | 31.50”
- SEAT HEIGHT 44 CM | 17.32”
- SEAT DEPTH 41 CM | 16.14”

OPTIONS
- Soft or hard-floor caster options.
- Two choices of seat foam densities: 
 medium (1.8 lb/ft3) or high (2.8 lb/ft3)
- Armless or 8 position PU armrests 

MATERIALS
SHELL BASE GLIDER
- Cast Aluminum with modified nylon PA6/PA66 coating.
- Shell thickness: 10 mm.
SEAT
- HD36 foam

COUNTRY OF ORIGIN
- Italy
"""


# In[37]:


prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

Technical specifications: ```{fact_sheet_chair}```
"""
response = get_completion(prompt)
print(response)


# In[38]:


len(response)


# In[39]:


prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

The description is intended for furniture retailers, 
so should be technical in nature and focus on the 
materials the product is constructed from.

Use at most 50 words.

Technical specifications: ```{fact_sheet_chair}```
"""
response = get_completion(prompt)
print(response)


# In[ ]:





# In[40]:


prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

The description is intended for furniture retailers, 
so should be technical in nature and focus on the 
materials the product is constructed from.

At the end of the description, include every 7-character 
Product ID in the technical specification.

Use at most 50 words.

Technical specifications: ```{fact_sheet_chair}```
"""
response = get_completion(prompt)
print(response)


# In[42]:


prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

The description is intended for furniture retailers, 
so should be technical in nature and focus on the 
materials the product is constructed from.

At the end of the description, include every 7-character 
Product ID in the technical specification.

After the description, include a table that gives the 
product's dimensions. The table should have two columns.
In the first column include the name of the dimension. 
In the second column include the measurements in inches only.

Give the table the title 'Product Dimensions'.

Format everything as HTML that can be used in a website. 
Place the description in a <div> element.

Technical specifications: ```{fact_sheet_chair}```
"""

response = get_completion(prompt)
print(response)


# In[44]:


prompt = f"""
I received your email through Indeed. Thank you for contacting me.\
As per your email, I just applied for the position mentioned above. Please find my resume attached.
"""
prompt = f"""
Rewrite in a professional manner as if applying for a job.
```{prompt}```
"""
response = get_completion(prompt)
print(response)



# In[46]:


prompt = f"""
Write a professinal cover letter to apply for Lead data engineer position with the mom Project company
"""
prompt = f"""
Rewrite in a professional manner as if applying for a job. Less than 600 characters
```{prompt}```
"""
response = get_completion(prompt)
print(response)


# In[51]:


prompt = f"""
I haven't received the call from Holly. Here is my resume, for your consideration. 
"""
prompt = f"""
Rewrite in a professional manner as if applying for a job. Using 2 lines at the most
```{prompt}```
"""
response = get_completion(prompt)
print(response)


# In[54]:


prompt = f"""
Write an article about scammers in LinkedIn
"""
prompt = f"""
Compose a piece on the topic of fraudulent individuals on the professional networking platform, LinkedIn. At least 600 characters
```{prompt}```
"""
response = get_completion(prompt)
print(response)


# In[58]:


prompt = f"""
get me miles
"""
prompt = f"""
how many hours by car is Jacksonvile, FL from Pompano beach, FL
```{prompt}```
"""
response = get_completion(prompt)
print(response)


# In[59]:


prompt = f"""
Venezuela
"""
prompt = f"""
Tell me about Venezuela in Spanish
```{prompt}```
"""
response = get_completion(prompt)
print(response)


# In[60]:


prompt = f"""
Tell me about Mexico in Spanish
"""
prompt = f"""

```{prompt}```
"""
response = get_completion(prompt)
print(response)


# In[61]:


prompt = f"""
Tell me about Chine in Madarin
"""
prompt = f"""

```{prompt}```
"""
response = get_completion(prompt)
print(response)

