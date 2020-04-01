# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 11:55:22 2017

@author: lc
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret=[]
        for i in range(num+1):
            ret+=[len(bin(i).replace('0b','').replace('0',''))]
        return ret