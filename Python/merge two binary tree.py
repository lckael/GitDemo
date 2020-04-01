# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:46:47 2017

@author: lc
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        ret=TreeNode((t1.val if t1 else 0)+(t2.val if t2 else 0))
        ret.left=self.mergeTrees(t1 and t1.left,t2 and t2.left)
        ret.right=self.mergeTrees(t1 and t1.right,t2 and t2.right)
        return ret
    
    def maxDepth(self,root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        else:
            return 1+max(self.maxDepth(root.left ),self.maxDepth(root.right ))
    def invert(self,root):
        if not root:
            return
        if not root.left and not root.right:
            return 
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        x=root
        tmp=x.left
        x.left=x.right
        x.right=tmp
        
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.invert(root)
        return root
            
        
    
            
a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
d=TreeNode(4)
e=TreeNode(5)
f=TreeNode(6)   
a.left=b
a.right=c
d.left=e
d.right=f
x=Solution()
print(x.invertTree(a))

            