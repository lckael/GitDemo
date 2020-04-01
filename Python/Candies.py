`# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 17:12:21 2017

@author: lc
"""

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        tmp={}
        for i in candies:
            tmp[i]=1
        if len(tmp.keys())<=len(candies)/2:
            ret=len(tmp.keys())
        else:
            ret=len(candies)/2
        return ret
                