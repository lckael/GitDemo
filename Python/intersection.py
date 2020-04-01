# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 21:59:52 2017

@author: lc
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1={}
        dict2={}
        ret=[]
        for i in nums1:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        for i in nums2:
            if i not in dict2:
                dict2[i]=1
            else:
                dict2[i]+=1
        for j in dict1:
            if j in dict2:
                ret+=[j]
        return ret
        