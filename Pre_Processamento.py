#!/usr/bin/env python
# coding: utf-8

# In[11]:


import csv
import re
import nltk
import string
import sys
import unicodedata


# In[20]:


new_file = csv.reader(open('your_file', 'r',encoding='utf8'))


# In[21]:


resultado = open('new_result', 'w')


# In[22]:


list_docs = []


# In[23]:


def remove_hashtags(text):
	words = text.split()

	for i in words:
		if i.startswith('#'):
			words.remove(i)

	text = ' '.join(words)
	return text


# In[24]:


def remove_url(text):
	clean_text = re.match('(.*?)http.*?\s?(.*?)', text)
	if clean_text:
		return clean_text.group(1)
	else:
		return text


# In[25]:


def remove_stopwords(text):
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    
    a = []
    
    words = text.split()
    for t in words:
        new_token = regex.sub(u'',t)
        if not new_token == u'':
            a.append(new_token)
            
    stopwords = nltk.corpus.stopwords.words('portuguese')
    content = [w for w in a if w.lower().strip() not in stopwords]
    
    clean_text = []
    for word in content:
        
        nfkd = unicodedata.normalize('NFKD', word)
        palavras_sem_acento = u''.join([c for c in nfkd if not unicodedata.combining(c)])
        
        q = re.sub('[^a-zA-Z0-9 \\\]', ' ',palavras_sem_acento)
        
        clean_text.append(q.lower().strip())
        
    tokens = [t for t in clean_text if len(t)>2 and not t.isdigit()]
    ct = ' '.join(tokens)
   

    return ct


# In[26]:


for row in new_file:
    doc_word = remove_stopwords(row[0])
    doc_word = remove_hashtags(doc_word)
    doc_word = remove_url(doc_word)

    print(doc_word)
    resultado.write(doc_word + '\n')


# In[27]:



resultado.close()


# In[ ]:





# In[ ]:




