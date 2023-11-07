#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# . Write a program to check if the given number is palindrome or not.
num = int(input("Enter the number"))
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

