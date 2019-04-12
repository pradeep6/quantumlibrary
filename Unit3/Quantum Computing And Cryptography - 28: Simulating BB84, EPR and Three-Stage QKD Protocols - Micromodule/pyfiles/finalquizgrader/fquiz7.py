import unittest, cmath, numpy
from math import isclose
"""
This class is a test class used to test the isHermitian fuction.

Example:

print(isHermitian([[1,2-1j],[2 + 1j, 0]]))

Output
----------------------
True

"""



class isHermitianTest(unittest.TestCase):
    #Test positive real zero imaginary.
    def test_0(self):
        self.assertTrue(isHermitian([[1,2-1j],[2 + 1j, 0]]), "Test failed on 2 X 2 Hermitian")
    def test_1(self):
        self.assertTrue(isHermitian([[2, -1j],[1j,1]]), "Test failed on 2 X 2 Hermitian")
    def test_2(self):
        self.assertTrue(isHermitian([[1, 1+1j,2j],[1-1j,5,-3],[-2j,-3,0]]), "Test failed on 3 X 3 Hermitian")
    def test_3(self):
        self.assertTrue(isHermitian([[-1,1-2j,0],[1+2j,0,-1j],[0,1j,1]]), "Test failed on 3 X 2 Hermitian")
    def test_4(self):
        self.assertFalse(isHermitian([-1j]), "Test failed on 1 X 1 Non-Hermitian")
    def test_5(self):
        self.assertFalse(isHermitian([[1, 1-1j,2j],[1+1j,5,-3],[+2j,-3,0]]), "Test failed on 3 X 3 Non-Hermitian")
    def test_6(self):
        self.assertFalse(isHermitian([[5, -3j],[2j,-3]]), "Test failed on 2 X 2 Non-Hermitian")
    def test_7(self):
        self.assertFalse(isHermitian([1j]), "Test failed on 1 X 1 Non-Hermitian")





"""
This class is a test class used to test the isUnitary fuction.

Example:

print(isUnitary([[.5+.5j,.5+.5j],[.5-.5j,-.5 + .5j]]))

Output
----------------------
True

"""

def test():
    print(norm_nvec([18,3,1]))
testtt = [[1+1j,1+1j],[1-1j,-1 + 1j]]
class isUnitaryTest(unittest.TestCase):

    #Test positive real zero imaginary.
    def test_0(self):
        self.assertTrue(isUnitary((numpy.array([[1+1j,1+1j],[1-1j,-1 + 1j]])*.5).tolist()), "Test failed on 2 X 2 Unitary")
    def test_1(self):
        self.assertTrue(isUnitary((numpy.array([[1, -1j, -1 + 1j],[1j, 1, 1 +1j],[1+1j, -1 +1j, 0]])*.5).tolist()), "Test failed on 3 X 3 Unitary")
    def test_2(self):
        self.assertTrue(isUnitary([[1,0],[0 ,1j]]), "Test failed on 2 X 2 Unitary")
    def test_3(self):
        self.assertTrue(isUnitary([[1j, 0],[0,1]]), "Test failed on 2 X 2 Unitary")
    def test_4(self):
        self.assertFalse(isUnitary([[1+1j,1+1j],[1-1j,-1 + 1j]]), "Test failed on 2 X 2 Non-Unitary")
    def test_5(self):
        self.assertFalse(isUnitary([[1, -1j, -1 + 1j],[1j, 1, 1 +1j],[1+1j, -1 +1j, 0]]), "Test failed on 3 X 3 Non-Unitary")
    def test_6(self):
        self.assertFalse(isUnitary([[5, -3j],[2j,-3]]), "Test failed on 2 X 2 Non-Unitary")
    def test_7(self):
        self.assertFalse(isUnitary([[1j, 1],[0,1]]), "Test failed on 2 X 2 Non-Unitary")


def testIsHermitian():
    isHermitianTests = unittest.TestLoader().loadTestsFromTestCase(isHermitianTest)
    unittest.TextTestRunner(verbosity=1).run(isHermitianTests)
def testIsUnitary():
    isUnitaryTests = unittest.TestLoader().loadTestsFromTestCase(isUnitaryTest)
    unittest.TextTestRunner(verbosity=1).run(isUnitaryTests)

def runtests():
    testIsHermitian()
    testIsUnitary()
