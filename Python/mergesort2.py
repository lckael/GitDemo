# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 21:30:34 2018

@author: lc
"""

def mergeSort(l):
    if len(l)>1:
        ret=[]
        start=0
        end=len(l)-1
        mid=start+(end-start)//2
        left=mergeSort(l[:mid+1])
        right=mergeSort(l[mid+1:])
        i=0
        j=0
        while i<len(left) and j+1<len(right):
            if left[i]<right[j]:
                ret+=left[i]
                i+=1
            else:
                ret+=right[j]
                j+=1
        if i<len(left):
            ret.append(left[i:])
        elif j<len(right):
            ret.append(right[j:])
        return ret
    return l
    
    
    