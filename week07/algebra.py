'''The definitions of abstract classes Ring and Field from Lecture 18b have been provided here for the purpose of Tickable 14'''
from abc import ABC, abstractmethod

class Ring(ABC):
    '''Ring (A, +, ., zero, id)'''
    
    @abstractmethod
    def __mul__(a,b):
        ...
    
    @abstractmethod
    def __add__(a,b):
        ...
        
    @abstractmethod
    def __neg__(a,b):    
        ...
    
    # Even if we do not know how to add or how to negate,
    # we can already define subtraction in terms of these operators.
    def __sub__(a,b):
        return a+(-b)  # Note that a+(-b) is equivalent to a.__add__(b.__neg__())
    
    # The multiplicative identity "1" is written as "id" since 1 is reserved for the integer 
    @abstractmethod
    def id():
        ...
    
    # The additive identity "0" is written as "zero" since 0 is reserved for the integer 
    @abstractmethod
    def zero():
        ...
    
    @abstractmethod
    def __str__(self):
        ...
    
    # __repr__() replicates the (as yet unspecified) implementation of __str__()
    def __repr__(self):
        return str(self)
    
    # Even if id() and __mul__() are not defined yet, we can define power in terms of these
    def __pow__(a, n):
        if (n==0):
            return a.__class__.id()
        else:
            return a * (a**(n-1))
        

class Field(Ring):
    '''Field (A, +, ., zero, id)'''
    
    @abstractmethod
    def inv(a):
        ...
        
    # Even if inv() is not defined yet, and __mul__() is inherited but not defined, we can still define a/b = a * (b.inv())
    def __truediv__(a,b):
        return a*(b.inv())