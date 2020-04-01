# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:59:57 2017

@author: lc
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp={}
        for i in nums:
            if i in tmp:
                tmp[i]+=1
            else:
                tmp[i]=1
        return [i for i in tmp if tmp[i]==1][0]
    
    