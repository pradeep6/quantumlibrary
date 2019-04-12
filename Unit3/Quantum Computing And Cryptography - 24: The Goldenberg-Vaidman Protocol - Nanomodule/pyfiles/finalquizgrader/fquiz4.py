import unittest, cmath, numpy
from math import isclose

"""
This class is a test class used to test the matAdd fuction.

Example:

m1 = [[4+2j,5+6j],[6+1j,7]]
m2 = [[5+2j,6-1j],[7,8+3j]]
print(numpy.allclose(matAdd(m1,m2), [[ 9.0+4.0j , 11.0+5.0j],[13.0+1.0j, 15.0+3.0j]]))

Output
----------------------
True

"""



class matAddTest(unittest.TestCase):
    #Test positive real zero imaginary.
    def test_0(self):
        self.assertTrue(numpy.allclose(matAdd([[0,0],[0,0]],[[0,0],[0,0]]), [[0,0],[0,0]]), "Test failed when 0 is given")
    def test_1(self):
        self.assertTrue(numpy.allclose(matAdd([[0,0],[0,0]],[[5+2j,6-1j],[7,8+3j]]), [[5+2j,6-1j],[7,8+3j]]), "Test failed when only postive real given ")
    def test_2(self):
        self.assertTrue(numpy.allclose(matAdd([[4+2j,5+6j],[6+1j,7]],[[5+2j,6-1j],[7,8+3j]]), [[ 9.0+4.0j , 11.0+5.0j],[13.0+1.0j, 15.0+3.0j]]), "Test failed when only positive imag given ")
    def test_3(self):
        self.assertTrue(numpy.allclose(matAdd([[1,2],[3,4]],[[4+2j,5+6j],[6+1j,7]]), [[ 5.0+2.0j , 7.0+6.0j],[ 9.0+1.0j ,11.0+0.0j]]), "Test failed complex matrix given")
    def test_4(self):
        self.assertTrue(numpy.allclose(matAdd([0],[0]), [0]), "Test failed when 0 in arr size one is given")
    def test_5(self):
        self.assertTrue(numpy.allclose(matAdd([1],[1]), [2]), "Test failed when arr size one is given")
    def test_6(self):
        self.assertTrue(numpy.allclose(matAdd([[[[5],[7]],[[0],[2]]]],[[[[10],[-8]],[[4+2j],[3+3j]]]]), [[[[15.0+0.0j],[-1.0+0.0j]],[[ 4.0+2.0j],[ 5.0+3.0j]]]]), "Test failed when complex matrix given")
    def test_7(self):
        self.assertTrue(numpy.allclose(matAdd([[1,2],[3,4]],[[4,6],[0,0]]), [[5,8],[3,4]]), "Test failed real numbers given")






"""
This class is a test class used to test the scalarMatMult fuction.

Example:

print(numpy.allclose(scalarMatMult([[4+2j,5+6j],[6+1j,7]],[[5+2j,6-1j],[7,8+3j]]), [[(51+60j), (48+71j)], [(77+17j), (93+21j)]]))

Output
----------------------
True

"""


class scalarMatMultTest(unittest.TestCase):

    #Test positive real zero imaginary.
    def test_0(self):
        self.assertTrue(numpy.allclose(scalarMatMult([[0,0],[0,0]],[[0,0],[0,0]]), [[0,0],[0,0]]), "Test failed when 0 is given")
    def test_1(self):
        self.assertTrue(numpy.allclose(scalarMatMult([[0,0],[0,0]],[[5+2j,6-1j],[7,8+3j]]), [[0,0],[0,0]]), "Test failed when only postive real given ")
    def test_2(self):
        self.assertTrue(numpy.allclose(scalarMatMult([[4+2j,5+6j],[6+1j,7]],[[5+2j,6-1j],[7,8+3j]]), [[(51+60j), (48+71j)], [(77+17j), (93+21j)]]), "Test failed when complex matrix is given")
    def test_3(self):
        self.assertTrue(numpy.allclose(scalarMatMult([[1,2],[3,4]],[[4+2j,5+6j],[6+1j,7]]), [[(16+4j), (19+6j)], [(36+10j), (43+18j)]]), "Test failed when complex matrix is given")
    def test_4(self):
        self.assertTrue(numpy.allclose(scalarMatMult([0],[0]), [0]), "Test failed when 0 in arr size one is given")
    def test_5(self):
        self.assertTrue(numpy.allclose(scalarMatMult([2],[3]), [6]), "Test failed when arr size one given")
    def test_6(self):
        self.assertTrue(numpy.allclose(scalarMatMult([[1,3,4],[4,5,6j],[7,8,9]],[[9,8,7],[6,5,4],[3,2,1]]), [[(39+0j), (31+0j), (23+0j)], [(66+18j), (57+12j), (48+6j)], [(138+0j), (114+0j), (90+0j)]]), "Test failed when complex matrix is given")
    def test_7(self):
        self.assertTrue(numpy.allclose(scalarMatMult([[1,2],[3,4]],[[4,6],[0,0]]), [[4, 6], [12, 18]]), "Test failed real only given")

"""
This class is a test class used to test the transpose fuction.

Example:

print(numpy.allclose(transpose([[1,3,4],[4,5,6j],[7,8,9]]), [[1, 4, 7], [3, 5, 8], [4, 6j, 9]]))

Output
----------------------
True

"""

class transposeTest(unittest.TestCase):
    def test_0(self):
        self.assertTrue(numpy.allclose(transpose([[0,0],[0,0]]), [[0,0],[0,0]]), "Test failed when only 0 is given")
    def test_1(self):
        self.assertTrue(numpy.allclose(transpose([[4,6],[0,0]]), [[4,0],[6,0]]), "Test failed when only postive real given ")
    def test_2(self):
        self.assertTrue(numpy.allclose(transpose([[1,2],[3,4]]), [[1, 3], [2, 4]]), "Test failed when only positive imag given ")
    def test_3(self):
        self.assertTrue(numpy.allclose(transpose([[5+2j,6-1j],[7,8+3j]]), [[(5+2j), (7+0j)], [(6-1j), (8+3j)]]), "Test failed when pos and negative complex numbers given")
    def test_4(self):
        self.assertTrue(numpy.allclose(transpose([0]), [0]), "Test failed when 0 in arr size one given")
    def test_5(self):
        self.assertTrue(numpy.allclose(transpose([2]), [2]), "Test failed arr size one given")
    def test_6(self):
        self.assertTrue(numpy.allclose(transpose([[1,3,4],[4,5,6j],[7,8,9]]), [[1, 4, 7], [3, 5, 8], [4, 6j, 9]]), "Test failed when 2 X 3 matrix given")
    def test_7(self):
        self.assertTrue(numpy.allclose(transpose([[4+2j,5+6j],[6+1j,7]]), [[(4+2j), (6+1j)], [(5+6j), (7+0j)]]), "Test failed complex matrix given")

"""
This class is a test class used to test the conjugate fuction.

Example:

print(numpy.allclose(conjugate([[5+2j,6-1j],[7,8+3j]]), [[(5-2j), (6+1j)], [(7-0j), (8-3j)]]))

Output
----------------------
True

"""

class conjugateTest(unittest.TestCase):
    def test_0(self):
        self.assertTrue(numpy.allclose(conjugate([[0,0],[0,0]]), [[0,0],[0,0]]), "Test failed when 0 is given")
    def test_1(self):
        self.assertTrue(numpy.allclose(conjugate([[4,6],[0,0]]), [[4,6],[0,0]]), "Test failed when only postive real given ")
    def test_2(self):
        self.assertTrue(numpy.allclose(conjugate([[1,2],[3,4]]), [[1,2],[3,4]]), "Test failed on 2 X 2 matrix of only real numbers ")
    def test_3(self):
        self.assertTrue(numpy.allclose(conjugate([[5+2j,6-1j],[7,8+3j]]), [[(5-2j), (6+1j)], [(7-0j), (8-3j)]]), "Test failed complex matrix given")
    def test_4(self):
        self.assertTrue(numpy.allclose(conjugate([0]), [0]), "Test failed when only 0 is given")
    def test_5(self):
        self.assertTrue(numpy.allclose(conjugate([2j]), [-2j]), "Test failed when only 2j is given")
    def test_6(self):
        self.assertTrue(numpy.allclose(conjugate([[[[-21j]]]]), [[[[21j]]]]), "Test failed on irregular matrix size")
    def test_7(self):
        self.assertTrue(numpy.allclose(conjugate([[4+2j,5+6j],[6+1j,7]]), [[(4-2j), (5-6j)], [(6-1j), (7-0j)]]), "Test failed complex matrix given")

"""
This class is a test class used to test the sumComplex fuction.

Example:

print(numpy.allclose(conjugTranspose([[4+2j,5+6j],[6+1j,7]]), [[(4-2j), (6-1j)], [(5-6j), (7-0j)]]))

Output
----------------------
True

"""


class conjugTransposeTest(unittest.TestCase):
    def test_0(self):
        self.assertTrue(numpy.allclose(conjugTranspose([[0,0],[0,0]]), [[0,0],[0,0]]), "Test failed when 0 is given")
    def test_1(self):
        self.assertTrue(numpy.allclose(conjugTranspose([[4,6],[0,0]]), [[4, 0], [6, 0]]), "Test failed when only postive real given ")
    def test_2(self):
        self.assertTrue(numpy.allclose(conjugTranspose([[1,2],[3,4]]), [[1, 3], [2, 4]]), "Test failed when only positive imag given ")
    def test_3(self):
        self.assertTrue(numpy.allclose(conjugTranspose([[5+2j,6-1j],[7,8+3j]]), [[(5-2j), (7-0j)], [(6+1j), (8-3j)]]), "Test failed complex matrix given")
    def test_4(self):
        self.assertTrue(numpy.allclose(conjugTranspose([0]), [0]), "Test failed when on 1X1 matrix when 0 is given")
    def test_5(self):
        self.assertTrue(numpy.allclose(conjugTranspose([2j]), [-2j]), "Test failed arr size one given")
    def test_6(self):
        self.assertTrue(numpy.allclose(conjugTranspose([[[[-21j,0]]]]), [[[[(-0+21j)]]], [[[-0j]]]]), "Test failed on irregular matrix size")
    def test_7(self):
        self.assertTrue(numpy.allclose(conjugTranspose([[4+2j,5+6j],[6+1j,7]]), [[(4-2j), (6-1j)], [(5-6j), (7-0j)]]), "Test failed complex matrix given")


def testMatAdd():
    matAddTests = unittest.TestLoader().loadTestsFromTestCase(matAddTest)
    unittest.TextTestRunner(verbosity=1).run(matAddTests)
def testScalarMatMult():
    scalarMatMultTests = unittest.TestLoader().loadTestsFromTestCase(scalarMatMultTest)
    unittest.TextTestRunner(verbosity=1).run(scalarMatMultTests)
def testTranspose():
    transposeTests = unittest.TestLoader().loadTestsFromTestCase(transposeTest)
    unittest.TextTestRunner(verbosity=1).run(transposeTests)
def testConjugate():
    conjugateTests = unittest.TestLoader().loadTestsFromTestCase(conjugateTest)
    unittest.TextTestRunner(verbosity=1).run(conjugateTests)
def testConjugTranspose():
    conjugTransposeTests = unittest.TestLoader().loadTestsFromTestCase(conjugTransposeTest)
    unittest.TextTestRunner(verbosity=1).run(conjugTransposeTests)

def runtests():
    testMatAdd()
    testScalarMatMult()
    testTranspose()
    testConjugate()
    testConjugTranspose()
