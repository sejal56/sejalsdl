
# coding: utf-8

# In[1]:


A={1,2,3,4}
B={4,5,6,7}
print(A==B)


# In[2]:


A={'a','b','c'}
B={'a','b','c'}
print(A==B)


# In[3]:


A={'a','b','c','d','e'}
B={'c','d'}
A.issubset(B)


# In[4]:


B.issubset(A)


# In[5]:


A={'a','b','c','d','e'}
B={'c','d'}
A.issuperset(B)


# In[6]:


A>B


# In[7]:


A={'a','b','c','d','e'}
A.pop()
'c'


# In[8]:


A={'a','b','c','d','e'}
A.pop()


# In[9]:


A


# In[10]:


A={'a','b','c','d','e'}
A.push()


# In[11]:


'a'


# In[12]:


A


# In[13]:


A={1,2,3,4}
B={3,4,5,6,7}
print(A)


# In[14]:


print(B)


# In[15]:


print("Union", A|B)


# In[16]:


print("difference",A-B)


# In[17]:


print("intersection",A^B)

