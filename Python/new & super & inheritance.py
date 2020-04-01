# -*- coding: utf-8 -*-
"""
Created on Mon May  7 19:20:57 2018

@author: lc
"""

class person:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        
    def prop(self):
        return (self.name * self.gender)
    
class student(person):
    def __init__(self,name,gender,course):
        super().__init__(name,gender)
        self.course=course
    
    def prop(self):
        return super().prop()
        
a=person(4,5)
a.prop()

b=student(6,7,8)
b.prop()    