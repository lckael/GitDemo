# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 22:53:12 2017

@author: lc
"""
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        d1={}
        for i in range(2,n):
            
