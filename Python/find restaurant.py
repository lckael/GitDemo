# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 09:56:36 2017

@author: lc
"""

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict1={}
        dict2={}
        ret={}
        for i in range(len(list1)):
            dict1[list1[i]]=i
        for i in range(len(list2)):
            dict2[list2[i]]=i
        for i in dict1:
            if i in dict2:
                ret[i]=dict1[i]+dict2[i]
        return [i for i in ret if ret[i]==min(ret.values())]
                
        
      