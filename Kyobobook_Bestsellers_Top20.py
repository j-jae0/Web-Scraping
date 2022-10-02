#!/usr/bin/env python
# coding: utf-8

# # Requests로 베스트셀러 데이터 수집하기

# ## 라이브러리 로드

# In[1]:


from IPython.display import Image
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import requests


# ## 베스트셀러 페이지 url 가져오기

# In[2]:


Image("images/kyobobook_bestseller.png")


# ## Requests를 통한 HTTP 요청

# In[3]:


url = "http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf"


# In[4]:


response = requests.post(url, headers={"user-agent": "Mozilla/5.0"})
response


# ## BeautifulSoup으로 태그 찾기

# In[5]:


html = bs(response.text)


# In[6]:


title_tags = html.select(".title > a > strong")


# In[7]:


title_tags


# In[8]:


price_tags = html.select(".detail > .price > strong")


# In[9]:


price_tags


# ## 불필요한 태그 제거하기
# 

# In[10]:


title_tags[0].contents[0]


# In[11]:


price_tags[0].contents


# In[12]:


best_dict = {}

for i in range(len(title_tags)):
    best_dict[i+1] = [title_tags[i].contents[0], price_tags[i].contents[0]] 


# In[13]:


# key : 순위, values : 책제목, 가격
best_dict


# ## DataFrame으로 반환

# In[14]:


df = pd.DataFrame(best_dict,)
df


# In[15]:


# 행 열 전환, top20 범위 제한
df = df.transpose()


# In[16]:


type(df)


# In[17]:


df.columns


# In[18]:


df.columns = ['도서', '가격']


# In[19]:


top_20 = df[:20]


# In[20]:


top_20

