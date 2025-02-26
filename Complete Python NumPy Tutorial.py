#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 23:00:11 2023

@author: morningstar
"""

import numpy as np
import re


import pandas_datareader


x = np.array(1,2,2)
print(x)


# Complete Python NumPy Tutorial 
# (Creating Arrays, Indexing, Math, Statistics, Reshaping)


# THE BASICS:
    
#a=np.array([1,2,3],dtype="int32")
#b= np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])

#print(b)

#print(a)

# Get Dimension
#print(b.ndim)

#Get Shape 
#print(a.shape)

# Get Type 
#print(a.dtype)

# Get Size
#print(a.itemsize)
#print(b.itemsize)

# Get Total Size
#print(a.size*a.itemsize) #or you can print(a.nbytes)




# ACCESSING/CHANGING SPECIFIC ELEMNTS, ROWS, COLUMNS AND ETC:


#a= np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
#print(a)

# Get Specific Elemnt [r, c]. r: represent row-index
# -and c: represent column_index
#print(a[1,4])
 
# Get A Specific Row
#print(a[1,:])

# Get A Specific Column
#print(a[:,3])

# Geting A Little More Fancy [startindex:endindex:stepsize]
#print(a[0,1:6:3])
#a[1,5]=20
#print(a)

#a[:,3]=[1,34]

#print(a) 

# 3-D EXAMPLE:

#b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
#print(b)

# Get A Specific Elemnt (work outside in)
#print(b [0,1,0])

# Replace

#b[:,1,:]=[[6,6],[5,1]]
#print(b)


# INITIALIZING DIFFRENT TYPES OF ARRAYS:

# Initiaze All Zeros In Array/Matrix
#a= np.zeros(5)
#print(a)
#b=np.zeros((4,12))
#print(b)


# All 1s Matrix

#c=np.ones((4,3,2),dtype="int32")

#print(c,c.dtype)

# Any other Number
#d=np.full((2,3), 32,dtype="int16")
#print(d,d.dtype)

# Any Ohter Number (full_like)

#d= np.full_like(a, 34)#/np.full(a.shape,34)
#print(d)

# Random Decimal Numbers

#b=np.random.rand(4, 2,3)
#print(b)
#a= np.random.random_sample(a.shape)
#print(a)


# Random Integer Values
#c=np.random.randint(-4,7,size=(3,2))
                    
#print(c)
# The Indenity Matrix

#b=np.identity(6)
# print(b)

# Repeat An Array

#f= np.array([[2,3,4]])
#f= np.repeat(f, 4,axis=0)
#print(f)

#output=np.ones([5,5])
# print(output)

#z=np.zeros([3,3])
#z[1,1:2]=9
#output[1:4,1:4]=z

#print(output)


# COPYING ARRAYS:
    

#a= np.array([[3,4,5],[4,5,7]])
#b=a.copy()
#b[1,[0]]=43
#print(a)
#print(b)



# MATHEMATICS:
    
#a= np.array([1,2,3,4])


#a=a*4
#a=a/2
#a=-2
#a=+2
#b=np.array([1,0,1,0])
#a=a+b
#a=pow(a, 3)

#print(a)

# Take The Sin

#a=np.cos(a)
#print(a)


# LINEAR ALGEBRA:
    
#a= np.ones((2,3))
#b=np.full((3,2), 2)
#print(b)
#a=np.matmul(a,b)
#print(a)

# Find The Determinant
#c= np.identity(3)
#c= np.linalg.det(c)
#print(c)


# STATISTICS:

#stats= np.array([[1,2,3],[4,5,6]])
#stats_1=np.min(stats,axis=1)
#print(stats_1)
    
#stats_2=np.max(stats,axis=1)
#print(stats_2)
 
#stats=np.sum(stats)
#print(stats) 


# REORGANIZING ARRYAS:
    
#before =np.array([[1,2,3,4],[5,6,7,8]])
#print(before)

#before_after= np.reshape(before, (8,1))
#print(before_after)

# Vertically Stacking Vectors

#v1=np.array([1,2,3,4])

#v2=np.array([5,6,7,8])
#v1v2=np.vstack([v1,v2])

#print(v1v2)

# Horizontal Staking Vectors

#h1=np.array([2,4])
#h2=np.array([2,2])

#h1h2=np.hstack((h1,h2))
#print(h1h2)



# MISCELLANEOUS:
    # LOAD DATA FROM FILE:
    
#df=np.genfromtxt("data.txt",delimiter=",")
#print(df)

#df2=df.astype("int32")
 
#print(df2.dtype)

# BOOLEAN MASKING AND ADVANCED INDEXING:
#df_50=df[df>50]
#print(df_50)


# You Can Index With A List In Numpy-module

#a=np.array([1,2,3,4,5,6,7,8,9])

#a= a[[1,3,8]]
#print(a)

#b=np.any(df>50,axis=0)

#c=np.any(df>50,axis=0)
#print(b)
#print(c)

#d= ((df>50)&(df<100))
#print(d)






# Comprehensive Python Beautiful Soup Web Scraping Tutorial! 
# -(find/find_all, css select, scrape table)



















    