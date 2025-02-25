'''Algebra of rational polynomials

This module contains functions for adding and multiplying rational polynomials.
'''

import rational
import numpy as np

def add(p,q):
    '''add two polynomials p(x), q(x) with rational coefficients '''
    deg_p = len(p)-1
    assert deg_p >= 0
    deg_q = len(q)-1
    assert deg_q >= 0
    deg_r = max(deg_p,deg_q)
    r = []
    for j in range(deg_r+1):
        r.append([0,1])
    for j in range(deg_p+1):
        r[j] = rational.add(r[j],p[j])
    for j in range(deg_q+1):
        r[j] = rational.add(r[j],q[j])
    return _simplify(r)

def mul(p,q):
    '''multiply two polynomials p(x), q(x) with rational coefficients'''
    deg_p = len(p)-1
    assert deg_p >= 0
    deg_q = len(q)-1
    assert deg_q >= 0
    deg_r = deg_p+deg_q
    r = []
    for j in range(deg_r+1):
        r.append([0,1])
    for j in range(0,deg_r+1):
        for k in range(0,j+1):
            if (k <= deg_p) and (j-k <= deg_q):
                r[j] = rational.add(r[j],rational.mul(p[k],q[j-k]))
    return _simplify(r)

def to_str(p):
    '''Convert to string representation'''
    deg = len(p)-1
    assert deg>=0
    s = ''
    if deg==0:
        s = rational.to_str(p[0])
    else:
        for j in range(deg+1):
            if not(p[j][0] == 0):
                s += ' + ('+rational.to_str(p[j])+') * x^'+str(j)
    return s

def _simplify(p):
    '''Chop off leading terms'''
    if (len(p)>1) and (p[-1][0] == 0):
        return _simplify(p[:-1])
    else:
        return p

def evaluate(p,x):
    '''Evaluate polynomial for a given rational number x using Horner's rule'''
    deg = len(p)-1
    q = p[-1]
    for k in range(deg-1,-1,-1):
        q = rational.add(p[k],rational.mul(x,q))
    return q

def integrate(p):
    '''integrate a polynomial'''
    deg = len(p)-1
    assert deg>=0
    q = p.copy()
    q.insert(0,[0,1])
    for n in range(2,deg+2):
        q[n] = rational.mul([1,n],q[n])
    return _simplify(q)
