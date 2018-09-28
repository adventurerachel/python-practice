
# coding: utf-8

# In[2]:


import requests
r = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')


# In[3]:


print(r.text[0:500])


# In[11]:


from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('span', attrs={'class':'short-desc'})
len(results)


# In[13]:


##isolate to first result
first_result  = results[0]
first_result


# In[17]:


#find date
first_result.find('strong').text[0:-1]+', 2017'


# In[21]:


#find lie
first_result.contents[1][1:-2]


# In[24]:


#find explanation
first_result.find('a').text[1:-1]


# In[26]:


#find link

first_result.find('a')['href']


# In[30]:


records = []
for result in results:
    date = result.find('strong').text[0:-1]+', 2017'
    lie = result.contents[1][1:-2]
    explanation = result.find('a').text[1:-1]
    link = result.find('a')['href']
    
    records.append((date, lie, explanation, link))
    
len(records)

records[0]

