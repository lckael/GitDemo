# -*- coding: utf-8 -*-
"""
Created on Fri May 25 18:19:20 2018

@author: lc
"""
# =============================================================================
# Partition till fisrt part has k elements
# =============================================================================

def threeSum(numbers):
        # write your code here
        ret=[]
        numbers=sorted(numbers)
        for i in range(0,len(numbers)-2):
            start=i+1
            end=len(numbers)-1
            while start<end:
                if numbers[start]+numbers[end]>-numbers[i]:
                    end-=1
                elif numbers[start]+numbers[end]<-numbers[i]:
                    start+=1
                else:
                    if numbers[start]!=numbers[start-1]:
                        ret+=[[numbers[i],numbers[start],numbers[end]]]
                    end-=1
                    start+=1
        return ret
    
s=[-1,0,1]
threeSum(s)
    

            