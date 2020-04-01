# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 16:43:40 2017

@author: lc
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left==None and root.right==None:
            return 1
        else:
            return max(1+self.diameterOfBinaryTree(root.left),1+self.diameterOfBinaryTree(root.right))

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

if n==None:
    print('f')

x=Solution()
print(x.diameterOfBinaryTree(a))


        