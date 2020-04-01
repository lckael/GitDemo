# -*- coding: utf-8 -*-
"""
Created on Sat May  5 17:08:05 2018

@author: lc
"""

class stack:
    def __init__(self):
        self.values=[]
    
    def __repr__(self):
        ret=''
        for i in range(self.size()):
            ret+=str(self.values[i])+' '
        return ret
        
    def is_empty(self):
        return self.values==[]
    
    def peek(self):
        return self.values[-1]
    
    def size(self):
        return len(self.values)
    
    def push(self,data):
        self.values.append(data)
        
    def pop(self):
        return self.values.pop()

def superstack(operations):
    stack=[]
    length=0
    for i in operations:
        op=i.split(' ')[0]
        if op=='push':
            stack.append(int(i.split(' ')[1]))
            length+=1
            print(i.split(' ')[1])
        elif op=='pop':
            length-=1
            if length==0:
                stack.pop()
                print('EMPTY')
            else:
                stack.pop()
                print(stack[-1])
        else:
            e=int(i.split(' ')[1])
            add=int(i.split(' ')[2])
            for j in range(e):
                stack[j]+=add
            print(stack[-1])



    
    
    
#test:
x=stack()
x.push(2)
x.push(3)
x.push(4)
x.push(5)

operations =[];
operations.append('push 4');
operations.append('pop');
operations.append('push 3');
operations.append('push 5');
operations.append('push 2');
operations.append('inc 3 1')
operations.append('pop');
operations.append('push 1');
operations.append('inc 2 2');
operations.append('push 4');
operations.append('pop');
operations.append('pop');
superstack(operations)
    