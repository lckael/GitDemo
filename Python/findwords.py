# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 20:31:46 2017

@author: lc
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
#####################Solution 1#####################################################
#        ret=[]
#        str1='qwertyuiop'
#        str2='asdfghjkl'
#        str3='zxcvbnm'
#        dict1={}
#        dict2={}
#        dict3={}
#        for i in str1:
#            dict1[i]=1
#        for i in str2:
#            dict2[i]=1
#        for i in str3:
#            dict3[i]=1
#        for word in words:
#            flag=0
#            if word[0].lower() in dict1:
#                for i in word[1:]:
#                    if i.lower() not in dict1:
#                        flag=1
#                        break
#            elif word[0].lower() in dict2: 
#                for i in word[1:]:
#                    if i.lower() not in dict2:
#                        flag=1
#                        break
#            else:
#                for i in word[1:]:
#                    if i.lower() not in dict3:
#                        flag=1
#                        break
#            if flag==0:
#                ret+=[word]
#        return ret
#####################Solution 2#####################################################
        set1=set('qwertyuiop')
        set2=set('asdfghjkl')
        set3=set('zxcvbnm')
        ret=[]
        for word in words:
            if set(word.lower())&set1==set(word.lower()):
                ret+=[word]
            elif set(word.lower())&set2==set(word.lower()):
                ret+=[word]
            elif set(word.lower())&set3==set(word.lower()):
                ret+=[word]
        return ret
                 
         
                
                    
        
                
        