import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library

A = scipy.array([ [7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6] ])
P, L, U = scipy.linalg.lu(A.T)

print "A:"
pprint.pprint(A)

print "P:"
pprint.pprint(P.T)

print "L:"
pprint.pprint(L.T)

print "U:"
pprint.pprint(U.T)
