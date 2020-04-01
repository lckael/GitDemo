# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 23:59:17 2017

@author: lc
"""

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    
    def convertBST1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        else:
            a=root.val
            b=0 if not root.left else root.left.val
            c=0 if not root.right else root.right.val
            root.val+=c
            if root.left:
                root.left.val+=root.val
            if root.left.right:
                root.left.right.val+=root.val
            self.convertBST1(root.left)
            self.convertBST1(root.right)

            
    def convertBST(self, root):
            self.convertBST1(root)
            return root
            
a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
d=TreeNode(4)
e=TreeNode(5)
f=TreeNode(6) 
a.left=b
a.right=c
b.left=d
b.right=e
c.left=f

x=Solution()
