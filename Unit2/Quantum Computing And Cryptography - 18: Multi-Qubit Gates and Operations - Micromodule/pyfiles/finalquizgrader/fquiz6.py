import unittest, cmath, numpy
from math import isclose


"""
This class is a test class used to test the innerprod fuction.

Example:

print(numpy.allclose(innerprod([1 + 2j, -2 ,4j],[1j, -5+3j, 7]), (12-33j)))

Output
----------------------
True

"""



class innerprodTest(unittest.TestCase):
    #Test positive real zero imaginary.
    def test_0(self):
        self.assertTrue(numpy.allclose(innerprod([[0,0],[0,0]],[[0,0],[0,0]]), [[0,0],[0,0]]), "Test failed when 0 is given")
    def test_1(self):
        self.assertTrue(numpy.allclose(innerprod([[4,6],[0,0]],[[1,2],[3,4]]), 16), "Test failed when only positive real given ")
    def test_2(self):
        self.assertTrue(numpy.allclose(innerprod([1 + 2j, -2 ,4j],[1j, -5+3j, 7]), (12-33j)), "Test failed when complex matrix given ")
    def test_3(self):
        self.assertTrue(numpy.allclose(innerprod([[1 + 2j, 3 + 4j, 5], [1j,  -1 , -1-1j], [4,4-5j,3]], [[-2j,1,-5 +7j], [1, 2 - 1j, -1], [1,0,3 + 4j]]), (-14+40j)), "Test failed when complex matrix given")
    def test_4(self):
        self.assertTrue(numpy.allclose(innerprod([0],[0]), [0]), "Test failed when 0 is given")
    def test_5(self):
        self.assertTrue(numpy.allclose(innerprod([1],[1j]), [1j]), "Test failed when 1j is given")
    def test_6(self):
        self.assertTrue(numpy.allclose(innerprod([[4,6],[0,0]],[[4+2j,5+6j],[6+1j,7]]), (46+44j)), "Test failed when complex matrix given ")
    def test_7(self):
        self.assertTrue(numpy.allclose(innerprod([[5+2j,6-1j],[7,8+3j]],[[4+2j,5+6j],[6+1j,7]]), (146+29j)), "Test failed when complex matrix given ")





"""
This class is a test class used to test the norm_nvec fuction.

Example:

print(numpy.allclose(norm_nvec([9,64,-10]), 65.39877674696982))

Output
----------------------
True

"""

class norm_nvecTest(unittest.TestCase):

    #Test positive real zero imaginary.
    def test_0(self):
        self.assertTrue(numpy.allclose(norm_nvec([9,64,-10]), 65.39877674696982), "Test failed when positives and negatives given")
    def test_1(self):
        self.assertTrue(numpy.allclose(norm_nvec([0,0,0,0]), 0), "Test failed when only 0 given ")
    def test_2(self):
        self.assertTrue(numpy.allclose(norm_nvec([9,3,7,1,9,4,3]), 15.684387141358123), "Test failed when only positives given ")
    def test_3(self):
        self.assertTrue(numpy.allclose(norm_nvec([53,71,28,0,0,0,0,0]), 92.91931984253867), "Test failed when positives is given")
    def test_4(self):
        self.assertTrue(numpy.allclose(norm_nvec([0]), 0), "Test failed when 0 is given")
    def test_5(self):
        self.assertTrue(numpy.allclose(norm_nvec([1]), 1), "Test failed when 1 is given")
    def test_6(self):
        self.assertTrue(numpy.allclose(norm_nvec([3.123,71.578,28.435,0.11111,0.22222,0.1,0,0]), 77.08296935874033), "Test failed when decimals is given")
    def test_7(self):
        self.assertTrue(numpy.allclose(norm_nvec([18,3,1]), 18.275666882497067), "Test failed when positive is given")


def testInnerprod():
    innerprodTests = unittest.TestLoader().loadTestsFromTestCase(innerprodTest)
    unittest.TextTestRunner(verbosity=1).run(innerprodTests)
def testNorm_nvec():
    norm_nvecTests = unittest.TestLoader().loadTestsFromTestCase(norm_nvecTest)
    unittest.TextTestRunner(verbosity=1).run(norm_nvecTests)

def runtests():
    testInnerprod()
    testNorm_nvec()
