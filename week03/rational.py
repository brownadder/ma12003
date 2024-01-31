'''Algebra of rational numbers

This module provides functions for multiplying and adding rational numbers.
Rational numbers are represented as pairs of integers. For example, the rational
number a / b is stored as [a, b].
'''
import math

def _simplify_rational(q):
    '''Cancel common integer factors in numerator and denominator

    Input:
     * rational number q = [a, b] (= a/b)

    Output:
     * Simplified rational number q = (a'/b') with a' = a/g, b' = b/g where
       g = gcd(a,b)
    '''
    num, denom = q
    g = math.gcd(num,denom)
    return [num//g,denom//g]

def mul(p,q):
    '''Multiply two rational numbers

    Input:
      * rational number p = [a,b] (= a/b)
      * rational number q = [c,d] (= c/d)

    Output:
      * rational number r = [e,f] (= e/f) with r = p*q
    '''
    num_p, denom_p = p
    num_q, denom_q = q
    num_r = num_p*num_q
    denom_r = denom_p*denom_q
    return _simplify_rational([num_r,denom_r])

def mul_int(n,q):
    '''Multiply integer and rational number

    Input:
      * integer n
      * rational number q = [a,b] (= a/b)

    Output:
      * rational number r = [c,d] (= c/d) with r = n*q
    '''
    num_q, denom_q = q
    num_r = n*num_q
    denom_r = denom_q
    return _simplify_rational([num_r,denom_r])

def add(p,q):
    '''Add two rational numbers

    Input:
      * rational number p = [a,b] (= a/b)
      * rational number q = [c,d] (= c/d)

    Output:
      * rational number r = [e,f] (=e/f) with r = p + q
    '''
    num_p, denom_p = p
    num_q, denom_q = q
    num_r = num_p*denom_q + num_q*denom_p
    denom_r = denom_p*denom_q
    return _simplify_rational([num_r,denom_r])

def add_int(n,q):
    '''Add integer and rational number

    Input:
      * integer n
      * rational number q = [a,b] (= a/b)

    Output:
      * rational number r = [c,d] = (c,d) with r = n + q
    '''
    num_q, denom_q = q
    num_r = num_q + n*denom_q
    denom_r = denom_q
    return _simplify_rational([num_r,denom_r])

def to_str(q):
    '''Format rational number as a string of the form 'a / b'

    Input:
      * rational number q = [a,b] = (a/b)
    Output:
      * String of the form 'a / b'
    '''
    num_q, denom_q = q
    if denom_q == 1:
        return str(num_q)
    elif num_q == 0:
        return 0
    else:
        return str(num_q)+' / '+str(denom_q)
