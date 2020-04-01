# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 23:31:18 2017

@author: lc
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        s=0
        for i in nums:
            if i==0:
                s+=1
        for i in range(s):
            nums.remove(0)
            nums.append(0)
            
                  