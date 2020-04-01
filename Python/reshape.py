# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 02:10:10 2017

@author: lc
"""

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c!=len(nums)*len(nums[0]):
            return nums
        tmp=[]
        ret=[[[] for x in range(c)] for y in range(r)]
        for i in nums:
            tmp+=i
        tmp.reverse()
        for i in range(r):
            for j in range(c):
                ret[i][j]=tmp.pop()
        return ret
    
a=Solution()
a.matrixReshape([[1,2],[3,4]],1,4)
