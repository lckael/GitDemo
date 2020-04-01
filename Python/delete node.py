# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 23:55:12 2017

@author: lc
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val)

class linkedlist(object):
    def __init__(self, r): 
        self.root=ListNode(r)
    def add(self,d):
        curr=self.root
        new=ListNode(d)
        new.next=curr
        self.root=new
    def printlist(self):
        p=self.root
        while p:
            print(p.val)
            p=p.next
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next       
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
            
a=linkedlist(5)
a.add(3)
a.add(2)
a.add(4)
a.printlist()
b=a.root
a.root=a.reverseList(b)
a.printlist()



        
        

        
    

