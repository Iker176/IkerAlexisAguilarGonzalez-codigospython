#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=float(input("Valor a:" ))
b=float(input("Valor b:" ))
c=float(input("Valor c:" ))
if a!=0:
    x1=(-b+(((b*2)-(4*a*c))*0.5))/(2*a)
    x2=(-b-(((b*2)-(4*a*c))*0.5))/(2*a)
    print("el valor de x1 es:" )
    print(x1)
    print("el valor de x2 es:" )
    print(x2)

