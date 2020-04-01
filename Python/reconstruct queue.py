# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 11:21:53 2017

@author: lc
"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ret=[]
        for i in sorted(people,key=lambda x:(-x[0],x[1])):
            ret.insert(i[1],i)
        return ret
            
a=Solution()
b=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(a.reconstructQueue(b)) 
            
        
        