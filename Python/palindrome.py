# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 22:27:58 2017

@author: lc
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1={}
        ret=0
        v=0
        for i in s:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for i in dict1:
            if dict1[i]%2!=0:
                v=1
            ret+=dict1[i]//2
        if v==1:
            return 2*ret+1
        else:
            return 2*ret
        