import numpy as np

class LinearFunction(object):
    '''Linear functions on R'''
    
    def __init__(self, a, b):
        '''Creates a LinearFunction ax+b'''
        self.a = a;
        self.b = b;
    
    def __str__(self):
        '''Returns a string representation of a LinearFunction'''
        return str(self.a) +'x + ' + str(self.b);
  
    def __repr__(self):
        '''Returns a string representation of a LinearFunction'''
        return str(self);

    def evaluate(self, x):
        '''Evaluates the linear function self at the point x and returns self(x)'''
        return self.a*x + self.b
    
    def __add__(self, g):
        '''Returns the sum of two LinearFunctions'''
        r = LinearFunction(self.a + g.a, self.b + g.b)
        return r

    def random():
        '''Returns a random LinearFunction'''
        g = LinearFunction(np.random.random(), np.random.random())
        return g    
    
    def scale(self, c):
        '''Scales the LinearFunction by a factor c'''
        self.a = c*self.a
        self.b = c*self.b
    
    def random_list(n):
        '''Returns a list of n random LinearFunctions'''
        lst = []
        for i in range(n):
            lst.append(LinearFunction.random())    
        return lst