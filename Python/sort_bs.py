# -*- coding: utf-8 -*-
"""
Created on Wed May  2 19:28:04 2018

@author: lc
"""

def customSort(arr):
    d={}
    ret=[]
    for i in arr[1:]:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    key=[j for j in d.keys()]
    value=[k for k in d.values()]
    tmp=sorted([[key[l],value[l]] for l in range(len(key))],key= lambda x:(x[1],x[0]))
    for i in tmp:
        ret+=[i[0]]*i[1]
    return ret
    
#test
a=[5,3,1,2,2,4]
customSort(a)
