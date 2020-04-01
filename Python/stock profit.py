# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 01:15:07 2017

@author: lc
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        else:
            min=prices[0]
            max=prices[0]
            maxprofit=0
            for i in prices[1:]:
                tmpprofit=max-min
                if maxprofit<tmpprofit:
                    maxprofit=tmpprofit
                if i<min:
                    min=i
                    max=i
                elif i>min:
                    max=i
            tmpprofit=max-min
            if maxprofit<tmpprofit:
                maxprofit=tmpprofit
            return maxprofit

a=Solution()
b=[7,3,5,1,6,4]
print(a.maxProfit(b))
###########################################################################
#        if prices==sorted(prices,reverse=True):
#            return 0
#        diff=[]
#        for i in range(len(prices)-1):
#            if prices[i]<max(prices[i+1:]):
#                diff+=[max(prices[i+1:])-prices[i]]
#        return max(diff)
###########################################################################
#        if len(prices)<2:
#            return 0
#        else:
#            min_tmp=prices[0]
#            max_tmp=max(prices[1:])
#            diff=max(max_tmp-min_tmp,0)
#            for i in range(len(prices)):
#                if prices[i]<min_tmp and i!=len(prices)-1:
#                    if diff<max(prices[i+1:])-prices[i]:
#                        min_tmp=prices[i]
#                        max_tmp=max(prices[i+1:])
#                        diff=max_tmp-min_tmp
#            return diff

                