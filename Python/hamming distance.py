# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 21:18:51 2017

@author: lc
"""

class Solution(object):
    def hammingDistance(self, x, y):
        lim=int(bin(2**31).replace('0b',''))
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        arr1=int(bin(x).replace('0b',''))
        arr2=int(bin(y).replace('0b',''))
        arr1_new=lim+arr1
        arr2_new=lim+arr2
        tmp=arr1_new+arr2_new
        count=0
        for i in str(tmp):
            if i=='1':
                count+=1
        return count
       

        