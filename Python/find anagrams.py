# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:57:29 2017

@author: lc
"""

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """ 
        
########################################################################
#        ret=[]
#        if s=='' or p=='':
#            return ret
#        d1={}
#        l_s=len(s)
#        l_p=len(p)
#        for i in range(l_s-l_p+1):
#            d1[s[i:i+l_p]]=i
#        d2={}
#        for i in p: 
#            if i in d2:
#                d2[i]+=1
#            else:
#                d2[i]=1
#            d3={}
#            for j in i:
#                if j in d3:
#                    d3[j]+=1
#                else:
#                    d3[j]=1
#            if d2==d3:
#                ret+[d1[i]]
#        return ret
########################################################################
#        ret=[]
#        if s=='' or p=='':
#            return ret
#        d1={}
#        for i in range(len(s)):
#            if s[i] in p:
#                d1[s[i]]=i+1
#            else:
#                d1[s[i]]=0
#        for i in p:
#            if i not in s:
#                d1[i]=0
#        tmp=0
#        for i in p:
#            tmp+=d1[i]
#        for i in range(len(s)):
#            tmp1=0
#            for j in s[i:i+len(p)]:
#                tmp1+=d1[j]
#            if tmp1==tmp:
#                ret+=[i]
#        return ret

    
        