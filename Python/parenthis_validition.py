# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 01:55:50 2017

@author: lc
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2!=0:
            return False
        d1={')':'(',']':'[','}':'{'}
        tmp=[]
        if s[0] not in d1.values():
            return False
        for  i in s:
            if i in d1.values():
                tmp+=[i]
            else:
                if tmp.pop()!=d1[i]:
                    return False
        if tmp!=[]:
            return False
        else:
            return True
            
        
        
        
            
            