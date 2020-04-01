# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 17:33:10 2017

@author: lc
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def q_traverse(self):
        if self.val:print(self.val)  
        if self.left:self.left.q_traverse() 
        if self.right:self.right.q_traverse()
    
    def z_traverse(self):
        if self.left:self.left.z_traverse() 
        if self.val:print(self.val)
        if self.right:self.right.z_traverse()
        
    def h_traverse(self):
        if self.left:self.left.h_traverse() 
        if self.right:self.right.h_traverse()
        if self.val:print(self.val)
        
a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
d=TreeNode(4)
e=TreeNode(5)
f=TreeNode(6)
g=TreeNode(7)
h=TreeNode(8)
i=TreeNode(9)
j=TreeNode(10)
k=TreeNode(11)
l=TreeNode(12)
m=TreeNode(13)
n=TreeNode(14)
a.left=b
a.right=c
c.left=e
c.right=f
b.left=g
b.right=h


a.q_traverse()
a.z_traverse()
a.h_traverse()
