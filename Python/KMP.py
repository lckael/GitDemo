# -*- coding: utf-8 -*-
"""
Created on Mon May 14 21:05:15 2018

@author: lc
"""

def cal_next(s):
    length=len(s)
    k=-1
    nex=[0]*length
    nex[0]=-1
    for i in range(length):
        while k>-1 and s[k+1]!=s[i]:
            k=nex[k]
        if s[k+1]==s[i]:
            k+=1
        nex[i]=k
        print(nex[i])
    return nex

def kClosestNumbers(A, target, k):
        # write your code here
        d={}
        for i in A:
            d[i]=abs(i-target)
        l=sorted(d.items(),key=lambda x:(x[1],x[0]))
        ret=[i[0] for i in l]
        return ret[:k]
def myPow(x, n):
        # write your code here
        if x==0:
            return 0
        if n==0:
            return 1
        return x*myPow(x,n-1)

def isPalindrome( s):
        # New method
        if s=="":
            return True
        if len(s)==1:
            return True
        left=0
        right=len(s)-1
        while left<right:
            while right >=0 and not s[right].isalpha() and not s[right].isnumeric():
                right-=1
            while left <len(s) and not s[left].isalpha() and not s[left].isnumeric():
                left+=1
                print(left)
            if s[left].lower()!=s[right].lower():
                return False
        return True