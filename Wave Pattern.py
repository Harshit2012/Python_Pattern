#!/usr/bin/env python
# coding: utf-8

# In[1]:


wH = 5
wL = 4

for x in range(1, wH + 1):
    for y in range(1, wL + 1):
        for z in range(1, wH + 1):
            if (x == z or x + z == wH + 1):
                print("*", end="")
            else:
                print("", end="")
        print()

