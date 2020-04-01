# -*- coding: utf-8 -*-
"""
Created on Mon May  7 23:31:25 2018

@author: lc
"""

def bsearch(l,t):
    left=0
    right=len(l)
    mid=(left+right)//2
    while left<=right:
        if l[mid]==t:
            return mid
        elif l[mid]<t:
            left=mid+1
            mid=(left+right)//2
        else:
            right=mid-1
            mid=(left+right)//2
l = [1, 4, 4,12, 45, 66, 99, 120, 444]      
result=[bsearch(l,i) for i in l]
# =============================================================================
# 以上次品，正品返回第一个等于target的index
# =============================================================================
def bsearch_real(nums,target):
    left=0
    right=len(nums)-1
    mid=(left+right)//2
    while left<=right:
        if nums[mid]>=target:
            right=mid-1
            mid=(left+right)//2
        elif nums[mid]<target:
            left=mid+1
            mid=(left+right)//2
    if nums[left]==target:
        return left
    return -1
l = [4, 4, 4,4,4,12, 45, 66, 99, 120, 444]      
result1=[bsearch_real(l,i) for i in l]



        


