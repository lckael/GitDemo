# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:41:55 2017

@author: lc
"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict1={}
        dict2={}
        for i in s:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        for i in t:
            if i not in dict2:
                dict2[i]=1
            else:
                dict2[i]+=1
        if len(dict1)!=len(dict2):
            return (set(dict1)^set(dict2)).pop()
        else:
            for j in dict1:
                if dict1[j]!=dict2[j]:
                    return j
            
        