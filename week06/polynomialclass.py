'''This module implements functionalities for manipulating polynomials using standard mathematical operators such as + and * '''

import copy
import numpy as np

class Polynomial(object):
    '''Polynomials on R'''
    
    def __init__(self, coeffs):
        '''Creates a Polynomial defined by the list of coefficients'''
        if not(isinstance(coeffs, list)):
            raise Exception('A list of coefficients is required for defining a polynomial')
        elif (len(coeffs)==0):
            raise Exception('An empty list cannot be used for defining a polynomial')
        self.coeffs = copy.deepcopy(coeffs);  # make sure that we copy the coefficients so that we don't accidentally change input
    
    def __str__(self):
        '''Returns a string representation of a Polynomial'''
        deg = len(self.coeffs)-1
        s = ''
        for j in range(deg,-1,-1):
                s += ' + (' + str(self.coeffs[j]) +') * x^'+str(j)
        return s
  
    def __repr__(self):
        '''Returns a string representation of a LinearFunction'''
        return str(self);
    
    def __add__(self, q):
        '''Returns the sum of two Polynomials, self(x) and q(x)'''
        if (isinstance(q, (int, float))):
            rc = copy.deepcopy(self.coeffs)
            rc[0] += q
        else:
            p = self
            np = len(p.coeffs)
            nq = len(q.coeffs)
            pc = p.coeffs + [0] * max(0, nq-np)
            qc = q.coeffs + [0] * max(0, np-nq)
            rc = [0]*max(np, nq)
            for j in range(max(np, nq)):
                rc[j] = pc[j] + qc[j]
        return Polynomial(rc)

    def __mul__(self, q):
        '''Multiply the Polynomial by a scalar'''
        if isinstance(q, (int, float)):
            rc = [0]*len(self.coeffs)
            for j in range(len(self.coeffs)):
                rc[j] = self.coeffs[j]*q
        else:
            # Multiply two polynomials p(x)=self(x), q(x)
            p = self
            deg_p = len(p.coeffs)-1
            deg_q = len(q.coeffs)-1
            deg_r = deg_p+deg_q
            
            rc = [0]*(deg_r+1)
            for j in range(0,deg_r+1):
                for k in range(0,j+1):
                    if (k <= deg_p) and (j-k <= deg_q):
                        rc[j] += p.coeffs[k] * q.coeffs[j-k]
        return Polynomial(rc)    
    
    def __neg__(self):
        '''Returns the negative of a Polynomial'''
        c = [0]*len(self.coeffs)
        for j in range(len(self.coeffs)):
            c[j] = -self.coeffs[j]
        return Polynomial(c)
    
    def __sub__(self, q):
        '''Returns the subtraction of the Polynomial q(x) from self(x)'''
        return self + (-q)
    
    def __truediv__(self, c):
        '''Divide the Polynomial by a scalar'''
        if isinstance(c, (int, float)):
            rc = [0]*len(self.coeffs)
            for j in range(len(self.coeffs)):
                rc[j] = self.coeffs[j]/c
        else:
            raise Exception('Can only divide by a scalar (int or float)')
        return Polynomial(rc)

    
    def evaluate(self, x):
        '''Evaluate polynomial using Horner's rule'''
        p = self
        deg = len(p.coeffs)-1
        q = p.coeffs[-1]
        for k in range(deg-1,-1,-1):
            q = p.coeffs[k] + x*q
        return q
    
    def __matmul__(self, x):
        '''Overload the operator @ for evaluation of the polynomial'''
        return self.evaluate(x)


    def __rmul__(self, c):
        '''Multiply a scalar by the Polynomial (from right)'''
        return self * c # we can simply reuse __mul__ (just put c on right)
    
    def __radd__(self, c):
        '''Add a Polynomial to a scalar (from right)'''
        return self + c # we can simply reuse __add__ (just put c on right)