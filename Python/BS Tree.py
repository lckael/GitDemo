# -*- coding: utf-8 -*-
"""
Created on Sun May  6 13:18:33 2018

@author: lc
"""

# =============================================================================
# Type 1
# =============================================================================
class BSTree:
    class Node:
        def __init__(self,data=None):
            self.data=data
            self.left= None
            self.right= None
            
    def __init__(self):
        self.root=None
        
    def _insert(self,root,data):
        if not root:
            root=self.Node(data)
        else:
            if data>root.data:
                root.right=self._insert(root.right,data)
            elif data<root.data:
                root.left=self._insert(root.left,data)
            else:
                print('Data exists')
        return root
    
    def insert(self,data):
        self.root=self._insert(self.root,data)

    def _minimum(self,root):
        if root:
            if not root.left:
                return root
            else:
                return self._minimum(root.left)
            
    def minimum(self):
        return self._minimum(self.root).data
        
    def _maximum(self,root):
        if root:
            if not root.right:
                return root
            else:
                return self._maximum(root.right)
            
    def maximum(self):
        return self._maximum(self.root).data    
        
    def _pretraverse(self,root):
        if root.left !=None:
            self._pretraverse(root.left)
        if root:
            print (root.data)
        if root.right !=None:
            self._pretraverse(root.right)
            
    def pretraverse(self):
        self._pretraverse(self.root)
    
    def _delete(self,root,data):
        if not root:
            print('Not found')
        elif data<root.data:
            self._delete(root.left,data)
        elif data>root.data:
            self._delete(root.right,data)
        elif root.right and root.left:
            right_min = self._minimum(root.right)
            
            root.data=right_min.data
            root.right=self._delete(root.right,right_min.data)
        elif root.right:
            root=root.right
        elif root.left:
            root=root.left
        else:
            root=None
            print('hahah')
        return root

    def delete(self,data):
        self.root=self._delete(self.root,data)
        
        
    
        
        
        
#test 1
x=BSTree()
x.insert(7)
x.insert(3)
x.insert(5)
x.insert(9)
x.insert(18)
x.insert(1)
x.insert(8)
x.delete(18)
x.pretraverse()
#test 2
   

        













