# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 11:21:36 2017

@author: lc
"""
import math
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret=0
        for i in range((n//2)+1):
            tmp=n-2*i+i
            step=math.factorial(tmp)/(math.factorial(i)*math.factorial(n-2*i))
            ret+=step
        return ret
            
            
            