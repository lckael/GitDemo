# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 23:41:16 2017

@author: lc
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret=[]
        d1={}
        for i in range(len(nums)):
            d1[i]=nums[i] 
        for i in d1:
            if target-d1[i] in nums:
               ret+=[i]
        if len(ret)!=2:
            for i in ret:
                if d1[i]==target/2:
                    ret.remove(i)
        return ret
                
            