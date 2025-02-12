from algebra import Field

class Rational(Field):
    
    def __init__(self,num,denom):
        self.num = num
        self.denom = denom
    
    def __str__(self):
        return '('+str(self.num)+'/'+str(self.denom)+')'
    
    def id():
        return Rational(1,1)
    
    def zero():
        return Rational(0,1)
    
    def __mul__(a,b):
        if isinstance(b,int):
            return Rational(a.num*b, a.denom)
        else:
            return Rational(a.num*b.num, a.denom*b.denom)
    
    def __add__(a,b):
        cnum = a.num*b.denom + b.num*a.denom
        cdenom = a.denom*b.denom
        return Rational(cnum, cdenom)
    
    def __neg__(a):
        return Rational(-a.num, a.denom)
    
    def inv(a):
        return Rational(a.denom, a.num)