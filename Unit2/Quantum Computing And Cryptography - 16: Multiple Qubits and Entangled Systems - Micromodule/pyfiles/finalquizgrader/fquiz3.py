import unittest, cmath
from math import isclose
"""
This class is a test class used to test the toPolar fuction.

Example:

num1 = 10 + 12j
num2 = 5 + 2j
print(toPolar(num1,num2))

Output
----------------------
(2.5517+1.3793j)

"""
class toPolarTest(unittest.TestCase):
    #Test positive real zero imaginary.
    def test_0(self):
        self.assertTrue((toPolar(0) == (0,0)), "Test failed when 0 is given")
    def test_1(self):
        self.assertTrue((toPolar(10) == (10,0)), "Test failed when only postive real given ")
    def test_2(self):
        self.assertTrue((toPolar(6j) == (6,90)), "Test failed when only positive imag given ")
    def test_3(self):
        self.assertTrue((toPolar(-6j) == (6,-90)), "Test failed when only negative imag given ")
    def test_8(self):
        self.assertTrue((toPolar(-6) == (6,180)), "Test failed when only negative real given ")
    def test_4(self):
        self.assertTrue( (isclose(toPolar(2+3j)[0],3.6055512754639896) and isclose(toPolar(2+3j)[1],56.309932474020215)) , "Test failed when all positive")
    def test_5(self):
        self.assertTrue( (isclose(toPolar(100-4j)[0],100.07996802557444) and isclose(toPolar(100-4j)[1],-2.2906100426385296)) , "Test failed when positive real negative imag ")
    def test_6(self):
        self.assertTrue( (toPolar(-3-4j)[0]==5 and isclose(toPolar(-3-4j)[1],-126.86989764584402)) , "Test failed when all negative")
    def test_7(self):
        self.assertTrue( (isclose(toPolar(-1+4j)[0],4.123105625617661) and isclose(toPolar(-1+4j)[1],104.03624346792648)) , "Test failed when negative real and positive imag ")






"""
This class is a test class used to test the toCart fuction.

Example:

print(((toCart(-3+4j) == 5))

Output
----------------------
True

"""
class toCartTest(unittest.TestCase):

    #Test positive real zero imaginary.
    def test_0(self):
        self.assertTrue((toCart(0,0) == (0)), "Test failed when 0 is given")
    def test_1(self):
        self.assertTrue((toCart(10,0) == (10)), "Test failed when only postive real given ")
    def test_2(self):
        self.assertAlmostEqual(toCart(6,90), (6j),7, "Test failed when only positive imag given ")
    def test_3(self):
        self.assertAlmostEqual(toCart(6,-90), (-6j),7, "Test failed when only positive imag given ")
    def test_8(self):
        self.assertAlmostEqual(toCart(6,180), (-6),7, "Test failed when only positive imag given ")
    def test_4(self):
        self.assertAlmostEqual(toCart(3.6055512754639896,56.309932474020215), (2+3j),7, "Test failed when only positive imag given ")
    def test_5(self):
        self.assertAlmostEqual(toCart(100.07996802557444,-2.2906100426385296), (100-4j),7, "Test failed when only positive imag given ")
    def test_6(self):
        self.assertAlmostEqual(toCart(5,-126.86989764584402), (-3-4j),7, "Test failed when only positive imag given ")
    def test_7(self):
        self.assertAlmostEqual(toCart(4.123105625617661,104.03624346792648), (-1+4j),7, "Test failed when only positive imag given ")

"""
This class is a test class used to test the multPolar fuction.

Example:


print((isclose(multPolar(5, 30, 4, -45)[0],20) and isclose(multPolar(5, 30, 4, -45)[1],-15)))

Output
----------------------
True

"""
class multPolarTest(unittest.TestCase):
    def test_0(self):
        self.assertTrue( (isclose(multPolar(5, 30, 4, -45)[0],20) and isclose(multPolar(5, 30, 4, -45)[1],-15)) , "Test failed general case ")
    def test_1(self):
        self.assertTrue( isclose(multPolar(0, 0, 0, 0)[0],0) , "Test failed when all zero")
    def test_2(self):
        self.assertTrue( (isclose(multPolar(-10,-20, 0, 0)[0],0)) , "Test failed when one magnitude is 0")
    def test_3(self):
        self.assertTrue( (isclose(multPolar(10, 0, 2, 0)[0],20) and isclose(multPolar(10, 0, 2, 0)[1],0)) , "Test failed 0 angle")
    def test_4(self):
        self.assertTrue( (isclose(multPolar(4, 90, 10, 0)[0],40) and isclose(multPolar(4, 90, 10, 0)[1],90)) , "Test failed when all positive")
    def test_6(self):
        self.assertTrue( (isclose(multPolar(20, -60, 10, 30)[0],200) and isclose(multPolar(20, -60, 10, 30)[1],-30)) , "Test failed general case")
    def test_7(self):
        self.assertTrue( (isclose(multPolar(60, -30, -1, -90)[0],60) and isclose(multPolar(60, -30, -1, -90)[1],60)) , "Test failed general case")
    def test_8(self):
        self.assertTrue( (isclose(multPolar(-40, 0, -10, 0)[0],400) and isclose(multPolar(-40, 0, -10, 0)[1],0)) , "Test failed when both magnitude negative")


def testToPolar():
    toPolarTests = unittest.TestLoader().loadTestsFromTestCase(toPolarTest)
    unittest.TextTestRunner(verbosity=1).run(toPolarTests)
def testToCart():
    toCartTests = unittest.TestLoader().loadTestsFromTestCase(toCartTest)
    unittest.TextTestRunner(verbosity=1).run(toCartTests)
def testMultPolar():
    multPolarTests = unittest.TestLoader().loadTestsFromTestCase(multPolarTest)
    unittest.TextTestRunner(verbosity=1).run(multPolarTests)

def runtests():
    testToPolar()
    testToCart()
    testMultPolar()
