# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 17:06:08 2017

@author: lc
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret=[]
        d1={}
        for i in nums:
            d1[i]=1
        for i in range(1,len(nums)+1):
            if i not in d1:
                ret+=[i]
        return ret