import rational

def test_add_rational():
    '''Check that 1/2 + 3/5 == 11/10'''
    assert rational.add([1,2],[3,5]) == [11,10]

def test_add_int_rational():
    assert rational.add_int(3,[7,8]) == [31,8]

def test_mul_rational():
    '''Check that 3/2 * 4/5 == 11/10'''
    assert rational.mul([3,2],[4,5]) == [6,5]

def test_mul_int_rational():
    '''Check that 10 * 7/15 == 14/3'''
    assert rational.mul_int(10,[7,15]) == [14,3]
