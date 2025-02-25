import polynomial

def test_add_zero():
    '''Check that adding zero does not change polynomial'''
    p = [[2,3],[4,5],[-2,3]]
    p0 = [[0,1],]
    assert polynomial.add(p,p0) == p

def test_mul_zero():
    '''Check that multiplying by zero polynomial gives zero polynomial'''
    p = [[2,3],[4,5],[-2,3]]
    p0 = [[0,1],]
    assert polynomial.mul(p,p0) == p0

def test_mul_one():
    '''Check that multiplying by one-polynomal does not change polynomial'''
    p = [[2,3],[4,5],[-2,3]]
    p0 = [[1,1],]
    assert polynomial.mul(p,p0) == p

def test_add_constant():
    '''Check that adding two constant polynomial works'''
    p = [[1,3],]
    q = [[4,5],]
    assert polynomial.add(p,q) == [[17,15],]

def test_add_linear():
    '''Check that adding two linear polynomial works'''
    p = [[1,3],[-4,7]]
    q = [[2,9],[1,4]]
    assert polynomial.add(p,q) == [[5,9],[-9,28]]

def test_mul_constant():
    '''Check that multiplying two constant polynomial works'''
    '''Check that adding two constant polynomial works'''
    p = [[1,3],]
    q = [[4,5],]
    assert polynomial.mul(p,q) == [[4,15],]

def test_mul_linear():
    '''Check that multiplying two linear polynomial works'''
    p = [[1,3],[-4,7]]
    q = [[2,9],[1,4]]
    assert polynomial.mul(p,q) == [[2,27],[-11,252],[-1,7]]

def test_add_commutative():
    '''Check that addition is commutative'''
    p = [[1,4],[-5,6],[0,1],[1,4],[0,1],[2,7]]
    q = [[2,9],[-2,7],[1,6],[0,1],[-9,23]]
    assert polynomial.add(p,q) == polynomial.add(q,p)

def test_mul_commutative():
    '''Check that multiplication is commutative'''
    p = [[1,4],[-5,6],[0,1],[1,4],[0,1],[2,7]]
    q = [[2,9],[-2,7],[1,6],[0,1],[-9,23]]
    assert polynomial.mul(p,q) == polynomial.mul(q,p)

def test_add_linear_quadratic():
    '''Check that adding a linear and a quadratic polynomial works'''
    p = [[1,3],[-4,7]]
    q = [[2,9],[1,4],[2,3]]
    assert polynomial.add(p,q) == [[5,9],[-9,28],[2,3]]


def test_mul_linear_quadratic():
    '''Check that multiplying a linear and a quadratic polynomial works'''
    p = [[1,3],[-4,7]]
    q = [[2,9],[1,4],[2,3]]
    assert polynomial.mul(p,q) == [[2,27],[-11,252],[5,63],[-8,21]]

def test_evaluate_constant():
    '''Check that evaluation of constant polynomial works'''
    p = [[1,3],]
    x = [2,5]
    assert polynomial.evaluate(p,x) == [1,3]

def test_evaluate_linear():
    '''Check that evaluation of linear polynomial works'''
    p = [[1,3],[5,7]]
    x = [2,5]
    assert polynomial.evaluate(p,x) == [13,21]

def test_evaluate_quadratic():
    '''Check that evaluation of quadratic polynomial works'''
    p = [[1,3],[5,7],[2,9]]
    x = [2,5]
    assert polynomial.evaluate(p,x) == [1031,1575]

def test_integrate_zero():
    '''Check that integrating the zero polynomial works'''
    p = [[0,1],]
    assert polynomial.integrate(p) == p

def test_integrate_constant():
    '''Check that integrating a constant polynomial works'''
    p = [[1,3],]
    assert polynomial.integrate(p) == [[0,1],[1,3]]

def test_integrate_quadratic():
    '''Check that integrating a quadratic polynomial works'''
    p = [[1,3],[-2,5],[4,7]]
    assert polynomial.integrate(p) == [[0,1],[1,3],[-1,5],[4,21]]
