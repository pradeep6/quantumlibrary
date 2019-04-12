import unittest, cmath, numpy
from math import isclose


"""
This class is a test class used to test the tensor fuction.

Example:

print(tensor([[1,2-1j],[2 + 1j, 0]]))

Output
----------------------
True

"""

class tensorTest(unittest.TestCase):
    #Test positive real zero imaginary.
    def test_0(self):
        self.assertTrue(numpy.allclose(tensor([1,2j],[2+3j,4]),[(2+3j), (4+0j), (-6+4j), 8j]), "Test failed on vector")
    def test_1(self):
        self.assertTrue(numpy.allclose(tensor([[3,4j],[1+7j,0]],[2-17j,4]),[[(6-51j), (68+8j)], [(12+0j), 16j], [(121-3j), 0j], [(4+28j), 0j]]), "Test failed on matrix")
    def test_2(self):
        self.assertTrue(numpy.allclose(tensor([[1, 4+3j, 1j],[0,1,-2+1j]],[[2, 3 +1j, 1],[ 3- 1j, 5, 0],[-9j,1+1j,11j]]),[[(2+0j), (3+1j), (1+0j), (8+6j), (9+13j), (4+3j), 2j, (-1+3j), 1j], [(3-1j), (5+0j), 0j, (15+5j), (20+15j), 0j, (1+3j), 5j, 0j], [-9j, (1+1j), 11j, (27-36j), (1+7j), (-33+44j), (9-0j), (-1+1j), (-11+0j)], [0j, 0j, 0j, (2+0j), (3+1j), (1+0j), (-4+2j), (-7+1j), (-2+1j)], [0j, 0j, 0j, (3-1j), (5+0j), 0j, (-5+5j), (-10+5j), (-0+0j)], [-0j, 0j, 0j, -9j, (1+1j), 11j, (9+18j), (-3-1j), (-11-22j)]]), "Test failed matrix")
    def test_3(self):
        self.assertTrue(numpy.allclose(tensor([[2,1],[9,7],[2,8],[3,5]],[[2,3+1j],[3-1j,5],[-9j,1+1j]]),[[(4+0j), (6+2j), (2+0j), (3+1j)], [(6-2j), (10+0j), (3-1j), (5+0j)], [-18j, (2+2j), -9j, (1+1j)], [(18+0j), (27+9j), (14+0j), (21+7j)], [(27-9j), (45+0j), (21-7j), (35+0j)], [-81j, (9+9j), -63j, (7+7j)], [(4+0j), (6+2j), (16+0j), (24+8j)], [(6-2j), (10+0j), (24-8j), (40+0j)], [-18j, (2+2j), -72j, (8+8j)], [(6+0j), (9+3j), (10+0j), (15+5j)], [(9-3j), (15+0j), (15-5j), (25+0j)], [-27j, (3+3j), -45j, (5+5j)]]), "Test failed on matrix")
    def test_4(self):
        self.assertTrue(numpy.allclose(tensor([1,2,3,4,5],[1j,2j,3j,4j,5j]),[1j, 2j, 3j, 4j, 5j, 2j, 4j, 6j, 8j, 10j, 3j, 6j, 9j, 12j, 15j, 4j, 8j, 12j, 16j, 20j, 5j, 10j, 15j, 20j, 25j]), "Test failed on vector")
    def test_5(self):
        self.assertTrue(numpy.allclose(tensor([0],[1j,2j,3j,4j,5j]),[0j, 0j, 0j, 0j, 0j]), "Test failed vector")
    def test_6(self):
        self.assertTrue(numpy.allclose(tensor([1],[1j,2j,3j,4j,5j]),[1j,2j,3j,4j,5j]), "Test failed on vector")
    def test_7(self):
        self.assertTrue(numpy.allclose(tensor([[2+4j,82-354j],[3,0]],[1j,2j,3j,4j,5j]),[[(-4+2j), (354+82j)], [(-8+4j), (708+164j)], [(-12+6j), (1062+246j)], [(-16+8j), (1416+328j)], [(-20+10j), (1770+410j)], [3j, 0j], [6j, 0j], [9j, 0j], [12j, 0j], [15j, 0j]]), "Test failed matrix")


def testTensor():
    tensorTests = unittest.TestLoader().loadTestsFromTestCase(tensorTest)
    unittest.TextTestRunner(verbosity=1).run(tensorTests)

def runtests():
    testIsHermitian()
