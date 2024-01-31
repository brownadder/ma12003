import rational
''' Compute the sum

1 + 1/2 + 1/4 + 1/8 + ... + 1/2^{15}

'''

q = [1,1]
for k in range(1,16):
    q = rational.add(q,[1,2**k])
print (q)
